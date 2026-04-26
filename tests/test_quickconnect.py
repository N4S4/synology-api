"""Unit tests for QuickConnect transport support."""

import unittest
from unittest.mock import ANY, MagicMock, patch

from synology_api.auth import Authentication
from synology_api.base_api import BaseApi
from synology_api.filestation import FileStation


class FakeResponse:
    """Minimal requests response fake for transport tests."""

    def __init__(self, json_data=None):
        self._json_data = json_data
        self.cookies = {}
        self.status_code = 200

    def json(self):
        return self._json_data

    def raise_for_status(self):
        return None


def _quickconnect_post_responses():
    return [
        FakeResponse([{
            "errno": 0,
            "env": {"control_host": "control.quickconnect.to"},
            "server": {"ds_state": "CONNECTED"}
        }]),
        FakeResponse([{
            "errno": 0,
            "env": {"relay_region": "us"},
            "server": {"pingpong_path": "/webman/pingpong.cgi"}
        }])
    ]


class TestQuickConnect(unittest.TestCase):
    """Tests for QuickConnect request contracts."""

    def tearDown(self):
        BaseApi.shared_session = None

    @patch.object(Authentication, "get_ik_message", return_value="ik-message")
    @patch("synology_api.auth.requests.Session")
    @patch("synology_api.auth.requests.post")
    def test_authentication_resolves_quickconnect_and_logs_in(self, post, session_class, _get_ik):
        session = MagicMock()
        session.get.return_value = FakeResponse({"success": True})
        session.post.return_value = FakeResponse({
            "success": True,
            "data": {"sid": "sid-123", "synotoken": "token-123"}
        })
        session_class.return_value = session
        post.side_effect = _quickconnect_post_responses()

        auth = Authentication(
            username="user",
            password="pass",
            quickconnect_id="my-nas",
            cert_verify=False,
            debug=False
        )
        auth.login()

        self.assertEqual(
            auth.base_url,
            "https://my-nas.us.quickconnect.to/webapi/"
        )
        self.assertEqual(auth.sid, "sid-123")
        self.assertEqual(auth.syno_token, "token-123")
        self.assertTrue(auth._secure)

        post.assert_any_call(
            "https://global.quickconnect.to/Serv.php",
            json=[{
                "version": 1,
                "command": "get_server_info",
                "id": "mainapp_https",
                "serverID": "my-nas",
                "stop_when_error": False,
                "stop_when_success": False,
                "is_gofile": False,
                "path": ""
            }],
            verify=False
        )
        post.assert_any_call(
            "https://control.quickconnect.to/Serv.php",
            json=[{
                "version": 1,
                "command": "request_tunnel",
                "id": "mainapp_https",
                "serverID": "my-nas",
                "stop_when_error": False,
                "stop_when_success": True,
                "is_gofile": False,
                "path": ""
            }],
            verify=False
        )
        session.get.assert_called_once_with(
            "https://my-nas.us.quickconnect.to/webman/pingpong.cgi",
            params=None,
            verify=False,
            headers={
                "Origin": "https://my-nas.us.quickconnect.to",
                "Referer": "https://my-nas.us.quickconnect.to"
            }
        )
        login_call = session.post.call_args
        self.assertEqual(
            login_call.args[0],
            "https://my-nas.us.quickconnect.to/webapi/entry.cgi"
        )
        self.assertEqual(login_call.kwargs["data"]["api"], "SYNO.API.Auth")
        self.assertEqual(login_call.kwargs["data"]["ik_message"], "ik-message")
        self.assertEqual(login_call.kwargs["verify"], False)
        self.assertEqual(
            login_call.kwargs["headers"],
            {
                "Origin": "https://my-nas.us.quickconnect.to",
                "Referer": "https://my-nas.us.quickconnect.to"
            }
        )

    @patch.object(Authentication, "get_ik_message", return_value="ik-message")
    @patch("synology_api.auth.requests.Session")
    @patch("synology_api.auth.requests.post")
    def test_request_data_uses_quickconnect_session_headers(self, post, session_class, _get_ik):
        session = MagicMock()
        session.get.side_effect = [
            FakeResponse({"success": True}),
            FakeResponse({"success": True, "data": {"hostname": "nas"}})
        ]
        session.post.return_value = FakeResponse({
            "success": True,
            "data": {"sid": "sid-123", "synotoken": "token-123"}
        })
        session_class.return_value = session
        post.side_effect = _quickconnect_post_responses()

        auth = Authentication(
            username="user",
            password="pass",
            quickconnect_id="my-nas",
            cert_verify=False,
            debug=False
        )
        auth.login()
        response = auth.request_data(
            "SYNO.FileStation.Info",
            "entry.cgi",
            {"version": 2, "method": "get"}
        )

        self.assertEqual(response["data"]["hostname"], "nas")
        request_call = session.get.call_args_list[1]
        self.assertEqual(
            request_call.args[0],
            "https://my-nas.us.quickconnect.to/webapi/entry.cgi?api=SYNO.FileStation.Info"
        )
        self.assertEqual(
            request_call.kwargs["params"],
            {"version": 2, "method": "get", "_sid": "sid-123"}
        )
        self.assertEqual(
            request_call.kwargs["headers"],
            {
                "Origin": "https://my-nas.us.quickconnect.to",
                "Referer": "https://my-nas.us.quickconnect.to",
                "X-SYNO-TOKEN": "token-123"
            }
        )

    @patch("synology_api.base_api.syn.Authentication")
    def test_base_api_accepts_quickconnect_without_ip_or_port(self, auth_class):
        session = MagicMock()
        session.app_api_list = {"SYNO.Core.System": {"path": "entry.cgi"}}
        session.full_api_list = {"SYNO.API.Info": {"path": "query.cgi"}}
        session.sid = "sid-123"
        session.base_url = "https://my-nas.us.quickconnect.to/webapi/"
        auth_class.return_value = session

        api = BaseApi(
            username="user",
            password="pass",
            quickconnect_id="my-nas"
        )

        self.assertIs(api.session, session)
        auth_class.assert_called_once_with(
            None,
            None,
            "user",
            "pass",
            False,
            False,
            7,
            True,
            None,
            None,
            None,
            "my-nas"
        )
        session.login.assert_called_once()
        session.get_api_list.assert_any_call("Core")
        session.get_api_list.assert_any_call()

    @patch("synology_api.filestation.base_api.BaseApi.__init__", autospec=True)
    def test_filestation_passes_quickconnect_to_base_api(self, base_init):
        def fake_base_init(instance, *args, **kwargs):
            session = MagicMock()
            session.app_api_list = {}
            session.request_data = MagicMock()
            instance.session = session
            instance.request_data = session.request_data
            instance.core_list = {}
            instance.gen_list = {}
            instance._sid = "sid-123"
            instance.base_url = "https://my-nas.us.quickconnect.to/webapi/"

        base_init.side_effect = fake_base_init

        FileStation(
            username="user",
            password="pass",
            quickconnect_id="my-nas"
        )

        base_init.assert_called_once_with(
            ANY,
            None,
            None,
            "user",
            "pass",
            False,
            False,
            7,
            True,
            None,
            None,
            None,
            "FileStation",
            quickconnect_id="my-nas"
        )


if __name__ == "__main__":
    unittest.main()
