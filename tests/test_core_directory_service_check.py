"""Unit tests for core_directory — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_directory_service_check import CoreDirectoryServiceCheck


def _make_instance():
    """Create a CoreDirectoryServiceCheck instance with mocked auth/session."""
    with patch('synology_api.core_directory_service_check.base_api.BaseApi.__init__', return_value=None):
        instance = CoreDirectoryServiceCheck.__new__(CoreDirectoryServiceCheck)

    api_list = {
        'SYNO.Core.DirectoryServiceCheck.Common': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Debug': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Domain': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.DomainJoin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.DomainService': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.DomainValidation': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.LDAP': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Progress': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreDirectoryServiceCheck(unittest.TestCase):
    """Tests for CoreDirectoryServiceCheck methods."""

    def setUp(self):
        self.instance = _make_instance()


    def test_directory_service_check_common_get(self):
        self.instance.directory_service_check_common_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_debug_get(self):
        self.instance.directory_service_check_debug_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_domain_get(self):
        self.instance.directory_service_check_domain_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_domain_join_get(self):
        self.instance.directory_service_check_domain_join_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_domain_service_get(self):
        self.instance.directory_service_check_domain_service_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_domain_validation_get(self):
        self.instance.directory_service_check_domain_validation_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_ldap_get(self):
        self.instance.directory_service_check_ldap_get()
        self.instance.request_data.assert_called_once()


    def test_directory_service_check_progress_get(self):
        self.instance.directory_service_check_progress_get()
        self.instance.request_data.assert_called_once()



if __name__ == '__main__':
    unittest.main()
