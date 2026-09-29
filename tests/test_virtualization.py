"""Request-contract tests for Virtualization routes."""

import unittest
from unittest.mock import MagicMock, patch

from synology_api.virtualization import Virtualization


API_LIST = {
    'SYNO.Virtualization.API.Task.Info': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Virtualization.API.Network': {'path': 'entry.cgi', 'maxVersion': 2},
    'SYNO.Virtualization.API.Storage': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Virtualization.API.Host': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Virtualization.API.Guest': {'path': 'entry.cgi', 'maxVersion': 3},
    'SYNO.Virtualization.API.Guest.Action': {'path': 'entry.cgi', 'maxVersion': 2},
    'SYNO.Virtualization.API.Guest.Image': {'path': 'entry.cgi', 'maxVersion': 2},
    'SYNO.Virtualization.API.Guest.Info': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Core.System.Info': {'path': 'entry.cgi', 'maxVersion': 1},
}


def _make_virtualization(response=None):
    """Create a Virtualization instance without making a NAS connection."""
    with patch('synology_api.virtualization.base_api.BaseApi.__init__', return_value=None):
        instance = Virtualization.__new__(Virtualization)

    instance.file_station_list = API_LIST.copy()
    instance.request_data = MagicMock(return_value=response or {'success': True, 'data': {}})
    instance._taskid_list = []
    instance._network_group_list = []
    instance._storages_list = []
    instance._host_operation_list = []
    instance._vm_guest_id_list = []
    instance._vm_guest_name_list = []
    instance._vm_created_taskid_list = []
    return instance


class TestVirtualizationRouteDiscovery(unittest.TestCase):
    """Tests for runtime discovery and use of Virtualization routes."""

    def setUp(self):
        self.client = _make_virtualization()

    def test_unmapped_route_list_only_includes_unmapped_virtualization_apis(self):
        self.assertEqual(
            self.client.get_unmapped_api_list(),
            [{
                'api_name': 'SYNO.Virtualization.API.Guest.Info',
                'path': 'entry.cgi',
                'max_version': 1,
            }],
        )

    def test_request_api_uses_discovered_path_and_version(self):
        self.client.request_api(
            'SYNO.Virtualization.API.Guest.Info',
            'list',
            {'guest_id': 'vm-1'},
        )

        self.client.request_data.assert_called_once_with(
            'SYNO.Virtualization.API.Guest.Info',
            'entry.cgi',
            {'version': 1, 'method': 'list', 'guest_id': 'vm-1'},
            method='get',
        )

    def test_request_api_supports_post_transport(self):
        self.client.request_api(
            'SYNO.Virtualization.API.Guest.Info',
            'import',
            {'name': 'vm-1'},
            http_method='post',
        )

        self.assertEqual(
            self.client.request_data.call_args.kwargs['method'], 'post')

    def test_request_api_rejects_routes_outside_virtualization_namespace(self):
        with self.assertRaises(ValueError):
            self.client.request_api('SYNO.Core.System.Info', 'get')

        self.client.request_data.assert_not_called()

    def test_request_api_rejects_routes_not_advertised_by_nas(self):
        with self.assertRaises(ValueError):
            self.client.request_api('SYNO.Virtualization.API.Unknown', 'get')

        self.client.request_data.assert_not_called()

    def test_request_api_does_not_allow_overriding_version_or_method(self):
        for reserved in ('version', 'method'):
            with self.subTest(reserved=reserved):
                with self.assertRaises(ValueError):
                    self.client.request_api(
                        'SYNO.Virtualization.API.Guest.Info',
                        'get',
                        {reserved: 'override'},
                    )

        self.client.request_data.assert_not_called()


class TestVirtualizationExistingRoutes(unittest.TestCase):
    """Regression tests for existing Virtualization wrappers."""

    def test_task_list_returns_ids_from_response_data(self):
        response = {
            'success': True,
            'data': {'tasks': ['task-1', 'task-2']},
        }
        client = _make_virtualization(response)

        result = client.get_task_list()

        self.assertEqual(result, ['task-1', 'task-2'])
        self.assertEqual(client._taskid_list, ['task-1', 'task-2'])

    def test_task_list_preserves_api_error_response(self):
        response = {'success': False, 'error': {'code': 403}}
        client = _make_virtualization(response)

        result = client.get_task_list()

        self.assertEqual(result, response)

    def test_vm_list_extracts_ids_and_names_from_guest_records(self):
        response = {
            'success': True,
            'data': {
                'guests': [
                    {'guest_id': 'vm-1', 'guest_name': 'nas-test'},
                    {'guest_id': 'vm-2', 'guest_name': 'build-agent'},
                ]
            },
        }
        client = _make_virtualization(response)

        result = client.get_vm_operation()

        self.assertEqual(result, response)
        self.assertEqual(client._vm_guest_id_list, ['vm-1', 'vm-2'])
        self.assertEqual(client._vm_guest_name_list, ['nas-test', 'build-agent'])

    def test_vm_property_set_sends_valid_cpu_and_other_optional_fields(self):
        client = _make_virtualization()

        result = client.set_vm_property(
            guest_id='vm-1',
            autorun=1,
            description='test VM',
            new_guest_name='nas-test',
            vcpu_num=4,
            vram_size=8192,
        )

        self.assertEqual(result, {'success': True, 'data': {}})
        self.assertEqual(
            client.request_data.call_args.args[2],
            {
                'version': 3,
                'method': 'set',
                'guest_id': 'vm-1',
                'autorun': 1,
                'description': 'test VM',
                'new_guest_name': 'nas-test',
                'vcpu_num': 4,
                'vram_size': 8192,
            },
        )

    def test_vm_property_set_rejects_boolean_cpu_count(self):
        client = _make_virtualization()

        result = client.set_vm_property(guest_id='vm-1', vcpu_num=True)

        self.assertEqual(result, 'vcpu_num must be an integer')
        client.request_data.assert_not_called()

    def test_vm_property_set_rejects_float_cpu_count(self):
        client = _make_virtualization()

        result = client.set_vm_property(guest_id='vm-1', vcpu_num=4.0)

        self.assertEqual(result, 'vcpu_num must be an integer')
        client.request_data.assert_not_called()

    def test_vm_property_set_requires_at_least_one_property(self):
        client = _make_virtualization()

        result = client.set_vm_property(guest_id='vm-1')

        self.assertEqual(result, 'Specify at least one VM property to update')
        client.request_data.assert_not_called()

    def test_delete_image_uses_delete_method_and_selected_identifier(self):
        client = _make_virtualization()

        client.delete_image(image_id='image-1')

        self.assertEqual(
            client.request_data.call_args.args[2],
            {'version': 2, 'method': 'delete', 'image_id': 'image-1'},
        )

    def test_create_image_reports_correct_storage_parameter_name(self):
        client = _make_virtualization()

        result = client.create_image()

        self.assertEqual(
            result, 'Specify at least one of storage_names or storage_ids')
        client.request_data.assert_not_called()


if __name__ == '__main__':
    unittest.main()