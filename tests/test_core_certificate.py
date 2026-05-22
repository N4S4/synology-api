"""Unit tests for core_certificate."""

import json
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_certificate import Certificate


def _make_instance(certs, dsm_version=7):
    """Create a Certificate instance with mocked auth/session."""
    with patch('synology_api.core_certificate.base_api.BaseApi.__init__', return_value=None):
        instance = Certificate.__new__(Certificate)

    session = MagicMock()
    session.app_api_list = {
        'SYNO.Core.Certificate.Service': {
            'path': 'entry.cgi',
            'minVersion': 1,
        }
    }
    session._version = dsm_version
    session._syno_token = 'token'
    session.verify_cert_enabled.return_value = False

    instance.session = session
    instance.base_url = 'https://nas.example/webapi/'
    instance._sid = 'sid'
    instance._debug = False
    instance.list_cert = MagicMock(
        return_value={'data': {'certificates': certs}})
    return instance


def _post_settings(mock_requests_session):
    post_call = mock_requests_session.return_value.post.call_args
    return json.loads(post_call.kwargs['data']['settings'])


class TestCoreCertificate(unittest.TestCase):
    """Tests for Certificate methods."""

    def test_set_certificate_for_default_service_keeps_dsm7_payload(self):
        certs = [{
            'id': 'old-cert',
            'services': [{'display_name': 'DSM Desktop Service'}],
        }]
        instance = _make_instance(certs)

        with patch('synology_api.core_certificate.requests.session') as mock_session:
            mock_session.return_value.post.return_value.status_code = 200
            mock_session.return_value.post.return_value.json.return_value = {
                'success': True}
            status_code, response = instance.set_certificate_for_service(
                'new-cert')

        self.assertEqual(status_code, 200)
        self.assertEqual(response, {'success': True})
        settings = _post_settings(mock_session)
        self.assertEqual(settings[0]['old_id'], 'old-cert')
        self.assertEqual(settings[0]['id'], 'new-cert')
        self.assertEqual(
            settings[0]['service']['display_name'], 'DSM Desktop Service')
        self.assertEqual(settings[0]['service']['service'], 'default')
        self.assertTrue(settings[0]['service']['multiple_cert'])
        self.assertTrue(settings[0]['service']['user_setable'])

    def test_set_certificate_for_non_default_service_uses_discovered_service(self):
        reverse_proxy_service = {
            'display_name': 'Reverse Proxy - photos.example.com',
            'display_name_i18n': 'reverse_proxy:photos.example.com',
            'isPkg': False,
            'owner': 'root',
            'service': 'ReverseProxy_1',
            'subscriber': 'reverse_proxy',
            'multiple_cert': True,
            'user_setable': True,
        }
        certs = [{
            'id': 'old-cert',
            'services': [reverse_proxy_service],
        }]
        instance = _make_instance(certs)

        with patch('synology_api.core_certificate.requests.session') as mock_session:
            mock_session.return_value.post.return_value.status_code = 200
            mock_session.return_value.post.return_value.json.return_value = {
                'success': True}
            status_code, response = instance.set_certificate_for_service(
                'new-cert', 'Reverse Proxy - photos.example.com')

        self.assertEqual(status_code, 200)
        self.assertEqual(response, {'success': True})
        settings = _post_settings(mock_session)
        self.assertEqual(settings[0]['old_id'], 'old-cert')
        self.assertEqual(settings[0]['id'], 'new-cert')
        self.assertEqual(settings[0]['service'], reverse_proxy_service)

    def test_set_certificate_for_missing_service_raises_clear_error(self):
        certs = [{'id': 'old-cert', 'services': []}]
        instance = _make_instance(certs)

        with self.assertRaisesRegex(ValueError, 'Service Missing Service not found'):
            instance.set_certificate_for_service('new-cert', 'Missing Service')

    def test_set_certificate_for_service_aborts_when_already_set(self):
        certs = [{
            'id': 'same-cert',
            'services': [{'display_name': 'DSM Desktop Service'}],
        }]
        instance = _make_instance(certs)

        with patch('synology_api.core_certificate.requests.session') as mock_session:
            result = instance.set_certificate_for_service('same-cert')

        self.assertEqual(result, (200, 'Certificate already set, aborting'))
        mock_session.assert_not_called()


if __name__ == '__main__':
    unittest.main()
