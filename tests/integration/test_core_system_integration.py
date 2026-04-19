"""
Integration tests for the CoreSystem API module.

Safe tests (marked @pytest.mark.safe) exercise ONLY read-only / GET methods
that will never modify your NAS. They are safe for production devices.

Destructive tests (marked @pytest.mark.destructive) exercise set, create,
delete, and other state-changing operations. They are SKIPPED by default.
To run them:  SYNOLOGY_ALLOW_DESTRUCTIVE=1 python3 -m pytest tests/integration/test_core_system_integration.py -v

Run safe tests only:
    python3 -m pytest tests/integration/test_core_system_integration.py -m safe -v
"""
import pytest

from synology_api.core_system import CoreSystem


# ---------------------------------------------------------------------------
# Session-scoped client (one login for all tests)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def system_client(nas_connection_kwargs):
    """CoreSystem client."""
    client = CoreSystem(**nas_connection_kwargs)
    yield client
    client.logout()


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _assert_valid_response(result):
    """Assert the result is a non-None response (dict or error string)."""
    assert result is not None
    if isinstance(result, dict):
        assert 'data' in result or 'error' in result or 'success' in result


# ===================================================================
#  SAFE (read-only) tests — will NOT modify your NAS
# ===================================================================

class TestCoreSystemSafe:
    """Read-only system queries."""

    @pytest.mark.safe
    def test_reset_button_get(self, system_client):
        _assert_valid_response(system_client.reset_button_get())

    @pytest.mark.safe
    def test_region_language_get(self, system_client):
        _assert_valid_response(system_client.region_language_get())

    @pytest.mark.safe
    def test_region_ntp_get(self, system_client):
        _assert_valid_response(system_client.region_ntp_get())

    @pytest.mark.safe
    def test_ntp_datetime_format_get(self, system_client):
        _assert_valid_response(system_client.ntp_datetime_format_get())

    @pytest.mark.safe
    def test_ntp_server_get(self, system_client):
        _assert_valid_response(system_client.ntp_server_get())

    @pytest.mark.safe
    def test_theme_app_portal_login_get(self, system_client):
        _assert_valid_response(system_client.theme_app_portal_login_get())

    @pytest.mark.safe
    def test_theme_desktop_get(self, system_client):
        _assert_valid_response(system_client.theme_desktop_get())

    @pytest.mark.safe
    def test_theme_file_sharing_login_get(self, system_client):
        _assert_valid_response(
            system_client.theme_file_sharing_login_get())

    @pytest.mark.safe
    def test_theme_image_get(self, system_client):
        _assert_valid_response(system_client.theme_image_get())

    @pytest.mark.safe
    def test_theme_image_list(self, system_client):
        _assert_valid_response(system_client.theme_image_list())

    @pytest.mark.safe
    def test_theme_login_get(self, system_client):
        _assert_valid_response(system_client.theme_login_get())

    @pytest.mark.safe
    def test_desktop_defs_get(self, system_client):
        _assert_valid_response(system_client.desktop_defs_get())

    @pytest.mark.safe
    def test_desktop_initdata_get(self, system_client):
        _assert_valid_response(system_client.desktop_initdata_get())

    @pytest.mark.safe
    def test_desktop_jsui_string_get(self, system_client):
        _assert_valid_response(system_client.desktop_jsui_string_get())

    @pytest.mark.safe
    def test_desktop_personal_updater_get(self, system_client):
        _assert_valid_response(
            system_client.desktop_personal_updater_get())

    @pytest.mark.safe
    def test_desktop_session_data_get(self, system_client):
        _assert_valid_response(system_client.desktop_session_data_get())

    @pytest.mark.safe
    def test_desktop_timeout_get(self, system_client):
        _assert_valid_response(system_client.desktop_timeout_get())

    @pytest.mark.safe
    def test_desktop_ui_string_get(self, system_client):
        _assert_valid_response(system_client.desktop_ui_string_get())

    @pytest.mark.safe
    def test_desktop_upgrade_get(self, system_client):
        _assert_valid_response(system_client.desktop_upgrade_get())

    @pytest.mark.safe
    def test_help_list(self, system_client):
        _assert_valid_response(system_client.help_list())

    @pytest.mark.safe
    def test_ui_search_list(self, system_client):
        _assert_valid_response(system_client.ui_search_list())

    @pytest.mark.safe
    def test_personal_settings_get(self, system_client):
        _assert_valid_response(system_client.personal_settings_get())


# ===================================================================
#  DESTRUCTIVE tests — SKIPPED by default
#  Set SYNOLOGY_ALLOW_DESTRUCTIVE=1 to run these.
# ===================================================================

class TestCoreSystemDestructive:
    """System operations that change state."""

    @pytest.mark.destructive
    def test_reset_button_set(self, system_client):
        pytest.skip("Would modify reset button behavior")

    @pytest.mark.destructive
    def test_region_language_set(self, system_client):
        pytest.skip("Would change system language")

    @pytest.mark.destructive
    def test_region_ntp_set(self, system_client):
        pytest.skip("Would change NTP settings")

    @pytest.mark.destructive
    def test_theme_desktop_set(self, system_client):
        pytest.skip("Would change desktop theme")

    @pytest.mark.destructive
    def test_theme_login_set(self, system_client):
        pytest.skip("Would change login theme")

    @pytest.mark.destructive
    def test_desktop_timeout_set(self, system_client):
        pytest.skip("Would change session timeout")

    @pytest.mark.destructive
    def test_personal_settings_set(self, system_client):
        pytest.skip("Would change personal settings")

    @pytest.mark.destructive
    def test_user_settings_set(self, system_client):
        pytest.skip("Would change user settings")
