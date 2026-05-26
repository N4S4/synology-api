"""Unit tests for synology_api.auth."""

import json
import unittest
from unittest.mock import MagicMock, patch

from synology_api.auth import Authentication
from synology_api.error_codes import CODE_SUCCESS, CODE_UNKNOWN


class FakeCipherState:
    """Small stand-in for noiseprotocol's outbound cipher state."""

    def __init__(self):
        self.n = 0
        self.calls = []

    def encrypt_with_ad(self, ad, plaintext):
        self.calls.append((ad, plaintext, self.n))
        self.n += 1
        return b'\x01\x02'


class FakeNoiseProtocol:
    """Small stand-in for noiseprotocol internals."""

    def __init__(self):
        self.cipher_state_encrypt = FakeCipherState()


class FakeNoiseConnection:
    """Small stand-in for a finished NoiseConnection."""

    def __init__(self):
        self.handshake_finished = True
        self.noise_protocol = FakeNoiseProtocol()
        self.read_payload = None

    def read_message(self, data):
        self.read_payload = data

    def get_handshake_hash(self):
        return b'\xff\xee'


def _make_auth():
    """Create an Authentication instance without running its constructor."""
    instance = Authentication.__new__(Authentication)
    instance._base_url = 'http://nas:5000/webapi/'
    instance._debug = False
    instance._sid = 'sid'
    instance._syno_token = 'token'
    instance._verify = False
    instance._noise_connection = None
    instance._noise_handshake_hash = None
    instance._requests_session = None
    instance._quickconnect_headers = {}
    return instance


class TestAuthenticationRequestHash(unittest.TestCase):
    """Tests for DSM Noise request hash generation."""

    def test_get_request_hash_uses_noise_cipher_and_nonce(self):
        auth = _make_auth()
        fake_noise = FakeNoiseConnection()
        auth._noise_connection = fake_noise
        auth._noise_handshake_hash = 'abcdefghijk'

        request_hash = auth._get_request_hash()

        self.assertEqual(request_hash, 'abcdefghAQI.MA')
        self.assertEqual(
            fake_noise.noise_protocol.cipher_state_encrypt.calls,
            [(b'', b'', 0)],
        )
        self.assertEqual(fake_noise.noise_protocol.cipher_state_encrypt.n, 1)

    def test_get_request_hash_omits_unfinished_noise_session(self):
        auth = _make_auth()
        fake_noise = FakeNoiseConnection()
        fake_noise.handshake_finished = False
        auth._noise_connection = fake_noise
        auth._noise_handshake_hash = 'abcdefghijk'

        self.assertIsNone(auth._get_request_hash())
        self.assertEqual(
            fake_noise.noise_protocol.cipher_state_encrypt.calls,
            [],
        )

    def test_get_request_headers_adds_request_hash_when_available(self):
        auth = _make_auth()
        auth._noise_connection = FakeNoiseConnection()
        auth._noise_handshake_hash = 'abcdefghijk'

        headers = auth._get_request_headers({'Content-Type': 'text/plain'})

        self.assertEqual(headers['X-SYNO-TOKEN'], 'token')
        self.assertEqual(headers['Content-Type'], 'text/plain')
        self.assertEqual(headers['X-SYNO-HASH'], 'abcdefghAQI.MA')

    def test_finish_noise_handshake_stores_handshake_hash(self):
        auth = _make_auth()
        fake_noise = FakeNoiseConnection()
        auth._noise_connection = fake_noise

        auth._finish_noise_handshake({
            'ik_message': Authentication.encode_ssid_cookie(b'reply')
        })

        self.assertEqual(fake_noise.read_payload, b'reply')
        self.assertEqual(
            auth._noise_handshake_hash,
            Authentication.encode_ssid_cookie(b'\xff\xee'),
        )

    @patch('synology_api.auth.requests.post')
    def test_request_webapi_data_uses_path_cookie_and_json_values(self, post):
        auth = _make_auth()
        response = MagicMock()
        response.json.return_value = {
            'success': True, 'data': {'name': 'share'}}
        post.return_value = response

        result = auth.request_webapi_data(
            'SYNO.Core.Share',
            'entry.cgi',
            {
                'method': 'create',
                'version': 1,
                'name': 'share',
                'shareinfo': {'name': 'share'},
            },
        )

        self.assertEqual(result, {'success': True, 'data': {'name': 'share'}})
        post.assert_called_once()
        url = post.call_args.args[0]
        params = post.call_args.kwargs['data']
        self.assertEqual(
            url, 'http://nas:5000/webapi/entry.cgi/SYNO.Core.Share')
        self.assertEqual(params['api'], 'SYNO.Core.Share')
        self.assertEqual(params['method'], 'create')
        self.assertEqual(params['version'], 1)
        self.assertEqual(params['name'], json.dumps('share'))
        self.assertEqual(params['shareinfo'], json.dumps({'name': 'share'}))
        headers = post.call_args.kwargs['headers']
        self.assertEqual(headers['Cookie'], 'id=sid')
        self.assertEqual(headers['X-SYNO-TOKEN'], 'token')
        response.raise_for_status.assert_called_once_with()


class GetErrorCodeTests(unittest.TestCase):
    """Tests for Authentication._get_error_code (a @staticmethod)."""

    def _call(self, response):
        return Authentication._get_error_code(response)

    # --- success ---

    def test_success_true_returns_zero(self):
        self.assertEqual(self._call({'success': True}), CODE_SUCCESS)

    def test_success_true_with_extra_data(self):
        response = {'success': True, 'data': {'sid': 'x'}}
        self.assertEqual(self._call(response), CODE_SUCCESS)

    # --- normal error ---

    def test_normal_error_returns_code(self):
        response = {'success': False, 'error': {'code': 100}}
        self.assertEqual(self._call(response), 100)

    def test_normal_error_returns_code_with_extras(self):
        response = {'success': False, 'error': {'code': 401, 'errors': []}}
        self.assertEqual(self._call(response), 401)

    # --- malformed responses (regression for AttributeError on
    #     `response.get('error').get('code')` when 'error' is missing/None) ---

    def test_missing_error_key_returns_unknown(self):
        # Was: AttributeError because response.get('error') → None, then None.get('code').
        self.assertEqual(self._call({'success': False}), CODE_UNKNOWN)

    def test_error_is_none_returns_unknown(self):
        response = {'success': False, 'error': None}
        self.assertEqual(self._call(response), CODE_UNKNOWN)

    def test_error_is_empty_dict_returns_unknown(self):
        response = {'success': False, 'error': {}}
        self.assertEqual(self._call(response), CODE_UNKNOWN)

    def test_error_is_non_dict_returns_unknown(self):
        # Server returning a string/list where a dict is expected.
        self.assertEqual(
            self._call({'success': False, 'error': 'oops'}), CODE_UNKNOWN)
        self.assertEqual(
            self._call({'success': False, 'error': [1, 2, 3]}), CODE_UNKNOWN)

    def test_error_code_is_non_int_returns_unknown(self):
        response = {'success': False, 'error': {'code': 'NaN'}}
        self.assertEqual(self._call(response), CODE_UNKNOWN)

    def test_completely_empty_response_returns_unknown(self):
        self.assertEqual(self._call({}), CODE_UNKNOWN)


class GetErrorDetailsTests(unittest.TestCase):
    """Tests for Authentication._get_error_details (a @staticmethod)."""

    def _call(self, response):
        return Authentication._get_error_details(response)

    # --- valid error details ---

    def test_file_station_shape(self):
        # Per https://kb.synology.com/en-global/DG/DSM_Login_Web_API_Guide/2
        response = {
            'success': False,
            'error': {
                'code': 1100,
                'errors': [{'code': 408, 'path': '/test/:'}],
            },
        }
        expected = [{'code': 408, 'path': '/test/:'}]
        self.assertEqual(self._call(response), expected)

    def test_active_directory_shape(self):
        # Per docstrings in directory_server.py.
        response = {
            'success': False,
            'error': {
                'code': 10104,
                'errors': [{'code': 10237, 'msg': 'ldb updaterecords: modify'}],
            },
        }
        self.assertEqual(
            self._call(response),
            [{'code': 10237, 'msg': 'ldb updaterecords: modify'}],
        )

    def test_multiple_details_preserved_in_order(self):
        response = {
            'success': False,
            'error': {
                'code': 1100,
                'errors': [
                    {'code': 408, 'path': '/a'},
                    {'code': 414, 'path': '/b'},
                ],
            },
        }
        self.assertEqual(
            self._call(response),
            [{'code': 408, 'path': '/a'}, {'code': 414, 'path': '/b'}],
        )

    # --- absent / empty ---

    def test_success_response_returns_empty(self):
        self.assertEqual(self._call({'success': True, 'data': {}}), [])

    def test_error_without_errors_key_returns_empty(self):
        response = {'success': False, 'error': {'code': 100}}
        self.assertEqual(self._call(response), [])

    def test_empty_errors_list_returns_empty(self):
        response = {'success': False, 'error': {'code': 1100, 'errors': []}}
        self.assertEqual(self._call(response), [])

    # --- malformed responses (mirror the defensive style of _get_error_code) ---

    def test_missing_error_key_returns_empty(self):
        self.assertEqual(self._call({'success': False}), [])

    def test_error_is_none_returns_empty(self):
        self.assertEqual(self._call({'success': False, 'error': None}), [])

    def test_error_is_non_dict_returns_empty(self):
        self.assertEqual(self._call({'success': False, 'error': 'oops'}), [])
        self.assertEqual(
            self._call({'success': False, 'error': [1, 2, 3]}), [])

    def test_errors_is_non_list_returns_empty(self):
        # Server returning a dict/string where a list is expected.
        error = {'code': 1, 'errors': {'code': 2}}
        self.assertEqual(self._call({'success': False, 'error': error}), [])
        error = {'code': 1, 'errors': 'oops'}
        self.assertEqual(self._call({'success': False, 'error': error}), [])

    def test_non_dict_entries_are_filtered_out(self):
        response = {
            'success': False,
            'error': {
                'code': 1100,
                'errors': [
                    {'code': 408, 'path': '/a'},
                    'garbage',
                    None,
                    42,
                    {'code': 414, 'path': '/b'},
                ],
            },
        }
        self.assertEqual(
            self._call(response),
            [{'code': 408, 'path': '/a'}, {'code': 414, 'path': '/b'}],
        )

    def test_completely_empty_response_returns_empty(self):
        self.assertEqual(self._call({}), [])


if __name__ == '__main__':
    unittest.main()
