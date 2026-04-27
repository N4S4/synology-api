"""Unit tests for Core Share request construction."""

import json
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_share import Share


def _make_share_instance(secure=True, request_format=None):
    """Create a Share instance with mocked auth/session."""
    with patch('synology_api.core_share.base_api.BaseApi.__init__', return_value=None):
        instance = Share.__new__(Share)

    api_info = {'path': 'entry.cgi', 'minVersion': 1, 'maxVersion': 6}
    if request_format is not None:
        api_info['requestFormat'] = request_format

    session = MagicMock()
    session._secure = secure
    session.encrypt_params = MagicMock(
        return_value={'__cIpHeRtExT': json.dumps({'rsa': 'r', 'aes': 'a'})})

    instance.core_list = {'SYNO.Core.Share': api_info}
    instance.session = session
    instance.request_data = MagicMock(return_value={'success': True})
    session.request_webapi_data = MagicMock(return_value={'success': True})
    return instance


class TestShareCreateFolder(unittest.TestCase):
    """Tests for shared folder creation request contracts."""

    def test_create_folder_uses_browser_contract_for_json_request_format(self):
        share = _make_share_instance(secure=False, request_format='JSON')

        share.create_folder(
            name='TestShare',
            vol_path='/volume1',
            desc='Created from test',
            hidden=True,
            enable_recycle_bin=False,
            recycle_bin_admin_only=False,
            hide_unreadable=True,
            enable_share_cow=True,
            enable_share_compress=True,
            share_quota=123,
            name_org='OriginalShare',
            encryption=True,
            enc_passwd='encrypted-password',
        )

        share.session.encrypt_params.assert_called_once()
        encrypted_payload = share.session.encrypt_params.call_args.args[0]
        shareinfo = json.loads(encrypted_payload['shareinfo'])
        self.assertEqual(shareinfo['name'], 'TestShare')
        self.assertEqual(shareinfo['vol_path'], '/volume1')
        self.assertEqual(shareinfo['desc'], 'Created from test')
        self.assertTrue(shareinfo['hidden'])
        self.assertFalse(shareinfo['enable_recycle_bin'])
        self.assertFalse(shareinfo['recycle_bin_admin_only'])
        self.assertTrue(shareinfo['hide_unreadable'])
        self.assertTrue(shareinfo['enable_share_cow'])
        self.assertTrue(shareinfo['enable_share_compress'])
        self.assertEqual(shareinfo['share_quota'], 123)
        self.assertEqual(shareinfo['name_org'], 'OriginalShare')
        self.assertTrue(shareinfo['encryption'])
        self.assertEqual(shareinfo['enc_passwd'], 'encrypted-password')

        share.session.request_webapi_data.assert_called_once_with(
            'SYNO.Core.Share',
            'entry.cgi',
            {
                'method': 'create',
                'version': 6,
                'name': 'TestShare',
                '__cIpHeRtExT': {'rsa': 'r', 'aes': 'a'},
            },
            method='post',
        )
        share.request_data.assert_not_called()

    def test_create_folder_keeps_json_https_shareinfo_plain(self):
        share = _make_share_instance(secure=True, request_format='JSON')

        share.create_folder(name='SecureShare', vol_path='/volume1')

        share.session.encrypt_params.assert_not_called()
        request_params = share.session.request_webapi_data.call_args.args[2]
        self.assertEqual(request_params['name'], 'SecureShare')
        self.assertEqual(
            request_params['shareinfo'],
            {
                'name': 'SecureShare',
                'vol_path': '/volume1',
                'desc': '',
                'name_org': '',
                'enable_recycle_bin': True,
                'recycle_bin_admin_only': True,
            },
        )

    def test_create_folder_preserves_legacy_https_plain_shareinfo(self):
        share = _make_share_instance(secure=True)

        share.create_folder(name='LegacyShare', vol_path='/volume1')

        share.session.encrypt_params.assert_not_called()
        share.session.request_webapi_data.assert_not_called()
        request_params = share.request_data.call_args.args[2]
        self.assertEqual(request_params['name'], 'LegacyShare')
        self.assertIn('shareinfo', request_params)
        self.assertEqual(
            json.loads(request_params['shareinfo'])['name'],
            'LegacyShare',
        )

    def test_create_folder_still_encrypts_plain_http(self):
        share = _make_share_instance(secure=False)

        share.create_folder(name='HttpShare', vol_path='/volume1')

        share.session.encrypt_params.assert_called_once()
        share.session.request_webapi_data.assert_not_called()
        share.request_data.assert_called_once_with(
            'SYNO.Core.Share',
            'entry.cgi',
            {
                'method': 'create',
                'version': 6,
                'name': 'HttpShare',
                '__cIpHeRtExT': json.dumps({'rsa': 'r', 'aes': 'a'}),
            },
            method='post',
        )


if __name__ == '__main__':
    unittest.main()
