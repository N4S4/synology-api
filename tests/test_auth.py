"""Unit tests for authentication request headers."""

import json
import unittest
from unittest.mock import MagicMock, patch

from synology_api.auth import Authentication


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
        url, params = post.call_args.args[:2]
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


if __name__ == '__main__':
    unittest.main()
