---
sidebar_position: 28
title: 🚧 SurveillanceStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# SurveillanceStation
:::warning
 
This API is not documented yet.
 
:::
## Overview

## Methods
### `surveillance_station_info`



---


### `camera_save`



---


### `camera_list`



---


### `get_camera_info`
This function return information about a camera.  
cameraIds : This parameter is named cameraIds in the API documentation but it refer to 1 camera ID  
privCamType: int = 1
    SYNO.SS.CamPriv.LIVEVIEW = 1;
    SYNO.SS.CamPriv.PLAYBACK = 2;
    SYNO.SS.CamPriv.LENS = 4;
    SYNO.SS.CamPriv.AUDIO = 8;
    SYNO.SS.CamPriv.DIGIOUT = 16;  
All other parameters must be let to default value  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  



---


### `camera_list_group`



---


### `get_snapshot`
By default, the profileType is 1, which is the default profile.  
Binary data is returned, so the response is not a json object.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  



---


### `enable_camera`



---


### `disable_camera`



---


### `get_capability_by_cam_id`



---


### `count_occupied_size`



---


### `is_shortcut_valid`



---


### `get_live_path`



---


### `audio_event_enum`



---


### `alarm_event_enum`



---


### `md_parameter_save`



---


### `motion_event_enum`



---


### `motion_parameter_save`



---


### `di_parameter_save`



---


### `alarm_sts_polling`



---


### `td_parameter_save`



---


### `enumerate_camera_group`



---


### `save_specific_group`



---


### `delete_specific_groups`



---


### `enumerate_group_information`



---


### `enumerate_camera_from_archive`



---


### `enumerate_archive_from_folder`



---


### `check_available_size_of_sdcard`



---


### `check_licence_quota`



---


### `format_specific_sd_card`



---


### `quick_create_single_camera`



---


### `move_camera_lens`



---


### `camera_lens_zoom`



---


### `list_preset_ptz_camera`



---


### `move_camera_lens_to_preset_position`



---


### `list_patrol_cameras`



---


### `force_cam_to_execute_patrol`



---


### `focus_camera`



---


### `control_camera_iris_in_out`



---


### `auto_focus`



---


### `move_cam_lens_to_absolute_position`



---


### `move_cam_to_home_position`



---


### `auto_pan_camera`



---


### `start_stop_object_tracking`



---


### `start_stop_external_recording`



---


### `query_event_list_by_filter`



---


### `delete_recordings`



---


### `delete_events_by_filter`



---


### `delete_all_recordings`



---


### `apply_settings_advance_tab`



---


### `count_by_number_of_event`



---


### `keep_event_play_alive`



---


### `stop_recording_event`



---


### `load_settings_in_advanced_tab`



---


### `lock_selected_event`



---


### `unlock_selected_event`



---


### `unlock_selected_filter_event`



---


### `lock_selected_recordings`



---


### `download_recordings`



---


### `check_if_recording_playable`



---


### `play_specific_recording`



---


### `download_merged_recording_files`
Download the merged files of UTC time range recordings of target camera.  
If there are different resolution or codec within UTC time range, the recordings will merge as much as possible
and downlod file will be a zip file.  
This method will start a task which have keep-alive mechanism.
Use GetRangeExportProgress method to get newest progress and keep-alive.
After receiving progress 100, use OnRangeExportDone method to download exported recording within 1
minutes.
If you want to cancel range export task, just do not send GetRangeExportProgress method or
OnRangeExportDone method. System will cleanup processed files itself.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  



---


### `get_newest_progress_keep_alive`



---


### `download_recording_from_target`
Response  
MP4 or zip file data.
The response type can be found in fileExt of GetRangeExportProgress method response when progress 100.  
Note
GetRangeExportProgress method must be sent within 1 minute after corresponding RangeExport method task
is completed, otherwise the exported recordings will be cleared.  
2.3.11.20 API Error Code
Code Description
400 Execution failed.
401 Parameter invalid.
405 CMS server connection failed.
414 Some events not exist.
439 Too many items selected.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  



---


### `handle_load_event_export`



---


### `check_name_export_event`



---


### `get_camera_information_list`



---


### `check_destination_folder_availability`



---


### `handle_save_event_export`



---


### `get_event_export_info_from_recording_server`



---


### `load_event_mount`



---


### `redirect_webapi_to_target_ds`
webAPI Array of `webAPI_info`  
Example:
`webAPI={"api": "SYNO.SurveillanceStation.AddOns", "version": 1, "method":
"List"}`  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  



---


### `modify_share_privilege`



---


### `apply_option_settings`



---


### `get_cms_info`



---


### `get_log_recording_data_from_target_ds`



---


### `get_samba_service`



---


### `check_if_samba_on_and_rec_enabled`



---


### `get_encoded_single_image_of_camera`



---


### `get_cms_status`



---


### `enable_smb_service`



---


### `notify_slave_ds_to_disconnect`



---


### `lock_recording_server_prevent_setting_change`



---


### `enable_ds_into_recording_server`



---


### `unpair_recording_servers`



---


### `get_free_memory_size`



---


### `handle_slave_ds`



---


### `get_target_ds_info`



---


### `logout_slave_ds`



---


### `pair_slave_ds`



---


### `login_slave_ds`
2.3.15.9 API Error Code  
Code Description
400 Execution failed.
401 Invalid parameter.
415 message connect failed.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  



---


### `save_slave_ds`



---


### `load_slave_ds_list`



---


### `count_number_of_logs`



---


### `clear_selected_logs`



---


### `get_information_log`



---


### `get_advanced_settings_logs`



---


### `set_advanced_setting_logs`



---


### `load_license_data`



---


### `check_license_quota`



---


### `get_http_video_stream`



---


### `save_action_rule`



---


### `download_action_rule`



---


### `send_data_2_player`



---


### `delete_all_histories_of_action_rule`



---


### `list_action_rules`



---


### `disable_action_rules`



---


### `enable_action_rules`



---


### `list_history_action_rules`



---


### `delete_action_rule`



---


### `get_list_of_emaps`



---


### `get_specific_emaps_setting`



---


### `get_emap_image`



---


### `get_autorized_ds_token`



---


### `set_message_event`



---


### `get_message_event`



---


### `set_notification_sender_name`



---


### `get_notification_sender_name`



---


### `set_advanced_notification_setting`



---


### `get_advanced_notification_setting`



---


### `send_test_mesg_to_primary_secondary_phone`



---


### `get_setting_notification_sms`



---


### `set_sms_service_setting`



---


### `send_test_sms`



---


### `send_test_mail`



---


### `list_mobile_paired_devices`



---


### `unpair_device`



---


### `get_controller_access_schedule`



---


### `get_camera_alarm_schedule`



---


### `get_sys_dependent_schedule`



---


### `set_batch_schedule`



---


### `get_access_ctrl_door_schedule`



---


### `get_camera_schedule`



---


### `set_sys_dependent_schedule`



---


### `set_controller_access_schedule`



---


### `set_camera_schedule`



---


### `get_notification_email_string`



---


### `set_adv_tab_info_filter`



---


### `create_sms_service_provider`



---


### `list_sms_provider`



---


### `delete_sms_service_provider`



---


### `get_addson_to_update`



---


### `enable_specific_addon`



---


### `get_specific_addon_update_info`



---


### `get_specific_addon_info`



---


### `get_total_addon_info`



---


### `update_addon_package`



---


### `check_addon_status`



---


### `disable_addon`



---


### `set_addon_autoupdate`



---


### `delete_specific_camera_recording_server`



---


### `get_camera_event_analytic`



---


### `delete_selected_events`



---


### `delete_specific_camera_events`



---


### `get_analytic_history`



---


### `get_analytic_history_by_filter`



---


### `unklock_selected_events`



---


### `set_camera_analytic_trigger`



---


### `flush_event_header`



---


### `lock_selected_events`



---


### `get_analytic_event_from_rec_server`



---


### `save_analytic_settings`



---


### `check_if_snapshot_exist`



---


### `save_snapshot_modification`



---


### `count_snapshot_by_category`



---


### `check_any_locked_snapshot`



---


### `unlock_snapshot_by_filter`



---


### `list_snapshot_information`



---


### `unlock_snapshot`



---


### `take_snapshot`



---


### `get_snapshot_setting_function`



---


### `delete_snapshot_by_filter`



---


### `get_snapshot_image`



---


### `lock_snapshot_image`



---


### `downld_single_snapshot`



---


### `save_new_snapshot_setting`



---


### `save_snapshot`



---


### `check_snapshot_status`



---


### `enable_visualstation`



---


### `update_vs_network_config`



---


### `lock_visualstation_by_id`



---


### `enumerate_vs_owner_info`



---


### `unlock_visualstation_by_id`



---


### `disable_visualstation_by_id`



---


### `delete_specific_visualstation`



---


### `enumerate_layout_visualstation`



---


### `save_layout_information`



---


### `delete_layout_visualstation`



---


### `clear_visualstation_search_result`



---


### `get_visualstation_ip_info`



---


### `stop_previous_visualstation_search`



---


### `get_visualstation_list`



---


### `get_number_of_controller`



---


### `get_cardholder_count`



---


### `enum_all_controllers_logger`



---


### `get_cardholder_photo`



---


### `get_log_count`



---


### `get_cardholder_info`



---


### `retrieve_last_access_credential`



---


### `enable_disable_controller`



---


### `acknowledge_all_alarm_level_log`



---


### `modify_controller_logger_config`



---


### `save_controller_settings`



---


### `download_filtered_logs`



---


### `get_door_name_from_controller`



---


### `test_connection_and_authentication`



---


### `enumerate_controller_list_info`



---


### `save_cardholder_setting`



---


### `enumerate_door_info`



---


### `clear_logs_surveillance_station`



---


### `list_all_user_privilege`



---


### `manual_lock_operation`



---


### `save_user_door_priv_setting`



---


### `list_all_logs`



---


### `delete_selected_controller`



---


### `retrieve_data_from_controller`



---


### `block_cardholder`



---


### `get_controller_count`



---


### `start_controller_search`



---


### `get_controller_search_result`



---


### `enumerate_digital_output`



---


### `save_digital_output_parameters`



---


### `long_polling_digital_output_status`



---


### `trigger_external_event`



---


### `get_list_io_modules`



---


### `get_io_port_list`



---


### `get_supported_list_io_modules`



---


### `save_setting_io_module`



---


### `enable_io_modules`



---


### `disable_io_modules`



---


### `delete_io_modules`



---


### `test_connection_to_io_module`



---


### `get_capability_io_module`



---


### `configure_io_port_setting`



---


### `poll_trigger_state_io_module`



---


### `poll_do_trigger_module`



---


### `get_number_of_devices`



---


### `get_category_count_io_module`



---


### `start_search_io_module`



---


### `get_search_io_module_info`



---


### `get_current_camera_status`



---


### `enum_preset_camera_list`



---


### `get_preset_camera_capability`



---


### `record_current_camera_position`



---


### `delete_list_preset_camera`



---


### `go_specific_preset_by_given_speed`



---


### `set_current_camera_position`



---


### `enum_patrol_list`



---


### `enum_patrol_name_list`



---


### `load_patrol_detail`



---


### `add_or_modify_patrol`



---


### `delete_specific_patrol`



---


### `run_patrol`



---


### `stop_patrol`



---


### `start_camera_search_process`



---


### `get_camera_search_info`



---


### `toggle_home_mode`



---


### `get_home_mode_settings`



---


### `get_transaction_list`



---


### `get_all_transaction_list`



---


### `lock_history_records`



---


### `unlock_history_records`



---


### `delete_history_records`



---


### `start_session_with_specified_session_id`



---


### `complete_session_with_specified_id`



---


### `cancel_session_with_specified_session_id`



---


### `carry_data_into_session_id`



---


### `add_edit_active_vault_task`



---


### `login_source_server_get_info`



---


### `delete_archive_vault_task`



---


### `list_exist_archive_vault`



---


### `enable_archive_vault_task`



---


### `disable_archive_vault_task`



---


### `disable_archive_vault_batchedit_task`



---


### `get_batch_edit_progress`



---


### `get_batchedit_proress_info`



---


### `clean_batchedit_progress_data`



---


### `get_youtube_live_broadcast_setting`



---


### `set_youtube_live_broadcast_info`



---


### `close_youtube_live_broadcast`



---


### `get_deep_video_analytic`



---


### `create_edit_DVA_task`



---


### `delete_dva_task`



---


### `enable_dva_task`



---


### `disable_dva_task`



---


### `reset_counter_people_counting_task`



---


### `get_people_enter_leave_count`



---


### `get_people_count_of_day`



---


### `list_people_counting_task`



---


### `delete_recording_file_of_detection`



---


### `get_info_of_task_and_frame`



---


### `lock_recording_file_of_detection`



---


### `unlock_recording_file_of_detection`



---


### `get_info_people_counting_task`



---


### `create_people_counting_task`



---


### `modify_setting_of_people_counting_task`



---


### `delete_task_group`



---


### `start_count_people_task_in_groups`



---


### `stop_count_people_task_in_groups`



---


### `get_number_counting_task_group`



---


### `lock_recording_file_result`



---


### `get_face_list_task`



---


### `create_or_edit_task`



---


### `delete_face_task`



---


### `enable_task_to_start_detection_recording`



---


### `disable_task_to_stop_detection_recording`



---


### `list_task_with_privilege_to_watch`



---


### `create_face_group`



---


### `disable_face_grooup`



---


### `edit_face_group`



---


### `get_face_group_list`



---


### `count_face_groups`



---


### `detect_faces_image`



---


### `create_registered_face`



---


### `delete_registered_face`



---


### `edit_registered_face`



---


### `list_registered_face`



---


### `count_registered_face`



---


### `search_registered_face`



---


### `get_face_result_list`



---


### `delete_face_result`



---


### `lock_face_result`



---


### `unlock_face_result`



---


### `get_recording_file_of_face_info`



---


### `get_recognition_face_information`



---


### `correct_face_result`



---


### `mark_face_result_as_stranger`



---


### `add_new_bookmark`



---


### `delete_bookmark`



---


### `list_bookmark_detail`



---


