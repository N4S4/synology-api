"""Unit tests for core_service — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_service_hw import CoreServiceHW


def _make_instance():
    """Create a CoreServiceHW instance with mocked auth/session."""
    with patch('synology_api.core_service_hw.base_api.BaseApi.__init__', return_value=None):
        instance = CoreServiceHW.__new__(CoreServiceHW)

    api_list = {
        'SYNO.Core.Group.ExtraAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Group.Member': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Group.ValidLocalAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.LCM': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.Led.Brightness': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.MemoryLayout': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.NeedReboot': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.OOBManagement': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.RemoteFanStatus': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.SpectreMeltdown': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.VideoTranscoding': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.FCTarget': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Host': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Lunbkp': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Node': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Replication': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.VMware': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.IndexFolder': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.MediaConverter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.Scheduler': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.ThumbnailQuality': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Account': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Login': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Logout': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Purchase': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.NormalUser': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.NormalUser.LoginNotify': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OAuth.Scope': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OAuth.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.AutoUpgrade.Progress': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Control': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.FakeIFrame': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Feed': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Legal.PreRelease': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Log': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.MyDS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.MyDS.Purchase': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Progress': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Screenshot': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Screenshot.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Setting.Update': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Thumb': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Thumb.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Device': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Event': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Filter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Mobile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Settings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PhotoViewer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.Compatibility': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.RouterInfo': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.RouterList': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.Rules.Serv': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreServiceHW(unittest.TestCase):
    """Tests for CoreServiceHW methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_group_extra_admin_get(self):
        self.instance.group_extra_admin_get()
        self.instance.request_data.assert_called_once()

    def test_group_member_list(self):
        self.instance.group_member_list(group='test')
        self.instance.request_data.assert_called_once()

    def test_group_valid_local_admin_get(self):
        self.instance.group_valid_local_admin_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_lcm_get(self):
        self.instance.hardware_lcm_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_led_brightness_get(self):
        self.instance.hardware_led_brightness_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_led_brightness_set(self):
        self.instance.hardware_led_brightness_set(brightness=1)
        self.instance.request_data.assert_called_once()

    def test_hardware_memory_layout_get(self):
        self.instance.hardware_memory_layout_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_need_reboot_get(self):
        self.instance.hardware_need_reboot_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_oob_management_get(self):
        self.instance.hardware_oob_management_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_remote_fan_status_get(self):
        self.instance.hardware_remote_fan_status_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_spectre_meltdown_get(self):
        self.instance.hardware_spectre_meltdown_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_video_transcoding_get(self):
        self.instance.hardware_video_transcoding_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_fc_target_get(self):
        self.instance.iscsi_fc_target_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_host_get(self):
        self.instance.iscsi_host_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_lunbkp_get(self):
        self.instance.iscsi_lunbkp_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_node_get(self):
        self.instance.iscsi_node_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_replication_get(self):
        self.instance.iscsi_replication_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_vmware_get(self):
        self.instance.iscsi_vmware_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_get(self):
        self.instance.media_indexing_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_index_folder_get(self):
        self.instance.media_indexing_index_folder_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_media_converter_get(self):
        self.instance.media_indexing_media_converter_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_scheduler_get(self):
        self.instance.media_indexing_scheduler_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_set(self):
        self.instance.media_indexing_set()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_thumbnail_quality_get(self):
        self.instance.media_indexing_thumbnail_quality_get()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_account_get(self):
        self.instance.mydscenter_account_get()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_get(self):
        self.instance.mydscenter_get()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_login(self):
        self.instance.mydscenter_login(username='test', password='test')
        self.instance.request_data.assert_called_once()

    def test_mydscenter_logout(self):
        self.instance.mydscenter_logout()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_purchase_get(self):
        self.instance.mydscenter_purchase_get()
        self.instance.request_data.assert_called_once()

    def test_normal_user_get(self):
        self.instance.normal_user_get()
        self.instance.request_data.assert_called_once()

    def test_normal_user_login_notify_get(self):
        self.instance.normal_user_login_notify_get()
        self.instance.request_data.assert_called_once()

    def test_oauth_scope_get(self):
        self.instance.oauth_scope_get()
        self.instance.request_data.assert_called_once()

    def test_oauth_server_get(self):
        self.instance.oauth_server_get()
        self.instance.request_data.assert_called_once()

    def test_oauth_server_set(self):
        self.instance.oauth_server_set()
        self.instance.request_data.assert_called_once()

    def test_package_auto_upgrade_progress_get(self):
        self.instance.package_auto_upgrade_progress_get()
        self.instance.request_data.assert_called_once()

    def test_package_control(self):
        self.instance.package_control(package_id='test', action='test')
        self.instance.request_data.assert_called_once()

    def test_package_fake_iframe_get(self):
        self.instance.package_fake_iframe_get()
        self.instance.request_data.assert_called_once()

    def test_package_feed_list(self):
        self.instance.package_feed_list()
        self.instance.request_data.assert_called_once()

    def test_package_feed_set(self):
        self.instance.package_feed_set()
        self.instance.request_data.assert_called_once()

    def test_package_legal_prerelease_get(self):
        self.instance.package_legal_prerelease_get()
        self.instance.request_data.assert_called_once()

    def test_package_log_get(self):
        self.instance.package_log_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_myds_get(self):
        self.instance.package_myds_get()
        self.instance.request_data.assert_called_once()

    def test_package_myds_purchase_get(self):
        self.instance.package_myds_purchase_get()
        self.instance.request_data.assert_called_once()

    def test_package_progress_get(self):
        self.instance.package_progress_get(task_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_screenshot_get(self):
        self.instance.package_screenshot_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_screenshot_server_get(self):
        self.instance.package_screenshot_server_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_setting_update_get(self):
        self.instance.package_setting_update_get()
        self.instance.request_data.assert_called_once()

    def test_package_thumb_get(self):
        self.instance.package_thumb_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_thumb_server_get(self):
        self.instance.package_thumb_server_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_personal_notification_device_get(self):
        self.instance.personal_notification_device_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_event_get(self):
        self.instance.personal_notification_event_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_filter_get(self):
        self.instance.personal_notification_filter_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_filter_set(self):
        self.instance.personal_notification_filter_set()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_mobile_get(self):
        self.instance.personal_notification_mobile_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_settings_get(self):
        self.instance.personal_notification_settings_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_settings_set(self):
        self.instance.personal_notification_settings_set()
        self.instance.request_data.assert_called_once()

    def test_photo_viewer_get(self):
        self.instance.photo_viewer_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_compatibility_get(self):
        self.instance.port_forwarding_compatibility_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_get(self):
        self.instance.port_forwarding_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_router_info_get(self):
        self.instance.port_forwarding_router_info_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_router_list(self):
        self.instance.port_forwarding_router_list()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_rules_serv_get(self):
        self.instance.port_forwarding_rules_serv_get()
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
