---
sidebar_position: 28
title: 🚧 SurveillanceStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# SurveillanceStation
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
API wrapper for Synology Surveillance Station.  
  
Provides methods to interact with Surveillance Station features such as retrieving
station information and saving camera configurations.  
  
## Methods
### `surveillance_station_info`
Retrieve information about the Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing Surveillance Station information, or a string
with error details if the request fails.  

</div>



---


### `camera_save`
Save or update camera configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `str`  
Camera ID.  
  
**_name_** `str`  
Camera name.  
  
**_dsld_** `int`  
Device slot ID.  
  
**_newName_** `str`  
New camera name.  
  
**_ip_** `str`  
Camera IP address.  
  
**_port_** `int`  
Camera port.  
  
**_vendor_** `str`  
Camera vendor.  
  
**_model_** `str`  
Camera model.  
  
**_userName_** `str`  
Username for camera authentication.  
  
**_password_** `str`  
Password for camera authentication.  
  
**_videoCodec_** `int`  
Video codec type.  
  
**_audioCodec_** `int`  
Audio codec type.  
  
**_tvStandard_** `int`  
TV standard.  
  
**_channel_** `str`  
Channel identifier.  
  
**_userDefinePath_** `str`  
User-defined path.  
  
**_fov_** `str`  
Field of view.  
  
**_streamXX_** `Any`  
Stream configuration.  
  
**_recordTime_** `int`  
Recording time.  
  
**_preRecordTime_** `int`  
Pre-recording time.  
  
**_postRecordTime_** `int`  
Post-recording time.  
  
**_enableRecordingKeepDays_** `bool`  
Enable recording retention by days.  
  
**_recordingKeepDays_** `int`  
Number of days to keep recordings.  
  
**_enableRecordingKeepSize_** `bool`  
Enable recording retention by size.  
  
**_recordingKeepSize_** `int`  
Maximum size for recordings.  
  
**_enableLowProfile_** `bool`  
Enable low profile recording.  
  
**_recordSchedule_** `list of int`  
Recording schedule.  
  
**_rtspPathTimeout_** `int`  
RTSP path timeout.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `camera_list`
Retrieve a list of cameras from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of camera IDs to filter.  
  
**_offset_** `int`  
The starting index for the camera list.  
  
**_limit_** `int`  
The maximum number of cameras to return.  
  
**_blFromCamList_** `bool`  
Whether to retrieve from the camera list.  
  
**_blIncludeDeletedCam_** `bool`  
Whether to include deleted cameras.  
  
**_privCamType_** `str`  
Filter by camera privilege type.  
  
**_basic_** `bool`  
Whether to return only basic information.  
  
**_streamInfo_** `bool`  
Whether to include stream information.  
  
**_blPrivilege_** `bool`  
Whether to include privilege information.  
  
**_camStm_** `int`  
Camera stream type.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing camera list information, or a string with error details.  

</div>



---


### `get_camera_info`
Return information about a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraIds_** `int`  
Camera ID. Although named cameraIds in the API, it refers to a single camera ID.  
  
**_privCamType_** `int, default=1`  
Camera privilege type. Possible values:
    1: LIVEVIEW
    2: PLAYBACK
    4: LENS
    8: AUDIO
    16: DIGIOUT  
  
**_blIncludeDeletedCam_** `bool, default=True`  
Whether to include deleted cameras.  
  
**_basic_** `bool, default=True`  
Whether to return only basic information.  
  
**_streamInfo_** `bool, default=True`  
Whether to include stream information.  
  
**_optimize_** `bool, default=True`  
Whether to optimize the returned data.  
  
**_ptz_** `bool, default=True`  
Whether to include PTZ (Pan-Tilt-Zoom) information.  
  
**_eventDetection_** `bool, default=True`  
Whether to include event detection information.  
  
**_deviceOutCap_** `bool, default=True`  
Whether to include device output capabilities.  
  
**_fisheye_** `bool, default=True`  
Whether to include fisheye camera information.  
  
**_camAppInfo_** `bool, default=True`  
Whether to include camera application information.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing camera information, or a string with error details.  

</div>



---


### `camera_list_group`
Retrieve a list of camera groups from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The starting index for the camera group list.  
  
**_limit_** `int`  
The maximum number of camera groups to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing camera group information, or a string with error details.  

</div>



---


### `get_snapshot`
Retrieve a snapshot image from a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `Any`  
Camera identifier.  
  
**_name_** `str`  
Camera name.  
  
**_dsld_** `int`  
Device slot ID.  
  
**_profileType_** `int, default=1`  
Profile type for the snapshot (1 is the default profile).  
  

</div>
#### Returns
<div class="padding-left--md">
`str`  
Binary data of the snapshot image. The response is not a JSON object.  

</div>



---


### `enable_camera`
Enable one or more cameras by their IDs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of camera IDs to enable.  
  
**_blIncludeDeletedCam_** `bool`  
Whether to include deleted cameras in the operation. Default is False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation as a dictionary, or a string with error details.  

</div>



---


### `disable_camera`
Disable one or more cameras by their IDs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of camera IDs to disable.  
  
**_blIncludeDeletedCam_** `bool`  
Whether to include deleted cameras in the operation. Default is False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the disable operation as a dictionary, or a string with error details.  

</div>



---


### `get_capability_by_cam_id`
Retrieve the capability information for a specific camera by its ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera for which to retrieve capability information.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing the camera's capability information, or a string with error details if the request fails.  

</div>



---


### `count_occupied_size`
Retrieve the occupied storage size for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to retrieve the occupied size.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing the occupied size information, or a string with error details if the request fails.  

</div>



---


### `is_shortcut_valid`
Check if a camera shortcut is valid.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `int`  
The ID of the camera to validate the shortcut for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary with the validation result, or a string with error details.  

</div>



---


### `get_live_path`
Retrieve the live view path for one or more cameras.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `int`  
Camera ID or comma-separated list of camera IDs for which to retrieve the live view path.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing the live view path information, or a string with error details.  

</div>



---


### `audio_event_enum`
Enumerate audio events for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to enumerate audio events.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing audio event enumeration, or a string with error details.  

</div>



---


### `alarm_event_enum`
Enumerate alarm events for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to enumerate alarm events.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing alarm event enumeration, or a string with error details.  

</div>



---


### `md_parameter_save`
Save motion detection parameters for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to save motion detection parameters.  
  
**_source_** `int`  
The source channel or stream index.  
  
**_mode_** `int`  
The motion detection mode.  
  
**_sensitivity_** `int`  
Sensitivity level for motion detection.  
  
**_threshold_** `int`  
Threshold value for motion detection.  
  
**_objectSize_** `int`  
Minimum object size to trigger detection.  
  
**_percentage_** `int`  
Minimum percentage of the detection area to trigger detection.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation as a dictionary, or a string with error details.  

</div>



---


### `motion_event_enum`
Enumerate motion events for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to enumerate motion events.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing motion event enumeration, or a string with error details.  

</div>



---


### `motion_parameter_save`
Save advanced motion detection parameters for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to save motion detection parameters.  
  
**_source_** `int`  
The source channel or stream index.  
  
**_mode_** `int`  
The motion detection mode.  
  
**_keep_** `bool`  
Whether to keep the current settings.  
  
**_level_** `int`  
Sensitivity level for advanced motion detection.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation as a dictionary, or a string with error details.  

</div>



---


### `di_parameter_save`
Save digital input (DI) parameters for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to save DI parameters.  
  
**_idx_** `int`  
The index of the DI channel.  
  
**_keep_** `bool`  
Whether to keep the current DI settings.  
  
**_normal_** `int`  
The normal state value for the DI channel.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation as a dictionary, or a string with error details.  

</div>



---


### `alarm_sts_polling`
Poll the alarm status for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to poll alarm status.  
  
**_timeOut_** `int`  
Timeout value for the polling operation.  
  
**_keep_** `Any`  
Reserved for future use or additional options (currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing alarm status polling result, or a string with error details.  

</div>



---


### `td_parameter_save`
Save tamper detection (TD) parameters for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Event` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The ID of the camera for which to save tamper detection parameters.  
  
**_source_** `int`  
The source channel or stream index.  
  
**_keep_** `Any`  
Whether to keep the current settings (reserved for future use).  
  
**_duration_** `int`  
Duration for the tamper detection event.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation as a dictionary, or a string with error details.  

</div>



---


### `enumerate_camera_group`
Enumerate camera groups in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_privCamType_** `int`  
Camera privilege type to filter groups.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing camera group enumeration, or a string with error details.  

</div>



---


### `save_specific_group`
Save or update a specific camera group in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_groupList_** `Any`  
The list of groups to be saved or updated.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation as a dictionary, or a string with error details.  

</div>



---


### `delete_specific_groups`
Delete specific camera groups in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_Id_** `int`  
The ID of the camera group to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation as a dictionary, or a string with error details.  

</div>



---


### `enumerate_group_information`
Enumerate group information for camera import in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Import` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camServerId_** `int`  
The ID of the camera server.  
  
**_shareName_** `str`  
The name of the shared folder.  
  
**_archiveName_** `str`  
The name of the archive.  
  
**_camlist_** `Any`  
List of cameras to include.  
  
**_actFromHost_** `bool`  
Whether the action is performed from the host. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the group information enumeration as a dictionary, or a string with error details.  

</div>



---


### `enumerate_camera_from_archive`
Enumerate cameras from a specified archive in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Import` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_shareName_** `str`  
The name of the shared folder containing the archive.  
  
**_archiveName_** `str`  
The name of the archive to enumerate cameras from.  
  
**_serverId_** `int`  
The ID of the server associated with the archive.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing camera enumeration details, or a string with error details if the request fails.  

</div>



---


### `enumerate_archive_from_folder`
Enumerate archives from a specified folder in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Import` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_shareName_** `str`  
The name of the shared folder containing the archives.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing archive enumeration details, or a string with error details if the request fails.  

</div>



---


### `check_available_size_of_sdcard`
Check the available size of the SD card for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Wizard` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
The ID of the camera.  
  
**_host_** `str`  
The host address of the camera.  
  
**_port_** `str`  
The port number for the camera connection.  
  
**_user_** `str`  
The username for authentication.  
  
**_passw_** `str`  
The password for authentication.  
  
**_vendor_** `str`  
The vendor of the camera.  
  
**_model_** `str`  
The model of the camera.  
  
**_ch_** `str`  
The channel identifier. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing the available size information, or a string with error details.  

</div>



---


### `check_licence_quota`
Check the license quota for Surveillance Station cameras.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Wizard` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing license quota information, or a string with error details if the request fails.  

</div>



---


### `format_specific_sd_card`
Format the SD card of a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Wizard` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
The ID of the camera whose SD card is to be formatted.  
  
**_host_** `str`  
The host address of the camera.  
  
**_port_** `str`  
The port number for the camera connection.  
  
**_user_** `str`  
The username for authentication.  
  
**_passw_** `str`  
The password for authentication.  
  
**_vendor_** `str`  
The vendor of the camera.  
  
**_model_** `str`  
The model of the camera.  
  
**_ch_** `str`  
The channel identifier.  
  
**_timeout_** `int`  
Timeout value for the formatting operation. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing the result of the format operation, or a string with error details.  

</div>



---


### `quick_create_single_camera`
Quickly create a single camera in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Wizard` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camServerId_** `Any`  
The ID of the camera server.  
  
**_actFromHost_** `bool`  
Whether the action is performed from the host.  
  
**_camStreamingType_** `str`  
The streaming type of the camera.  
  
**_camName_** `str`  
The name of the camera.  
  
**_camIP_** `str`  
The IP address of the camera.  
  
**_camPort_** `str`  
The port number of the camera.  
  
**_camVendor_** `str`  
The vendor of the camera.  
  
**_camModel_** `str`  
The model of the camera.  
  
**_camMountType_** `int`  
The mount type of the camera.  
  
**_camChannel_** `str`  
The channel of the camera.  
  
**_camVideoType_** `str`  
The video type of the camera.  
  
**_camAudioType_** `str`  
The audio type of the camera.  
  
**_camSourcePath_** `str`  
The source path for the camera stream.  
  
**_camUserName_** `str`  
The username for camera authentication.  
  
**_camPassWord_** `str`  
The password for camera authentication. (To be checked).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the quick create operation as a dictionary, or a string with error details.  

</div>



---


### `move_camera_lens`
Move the camera lens in a specified direction with an optional speed and move type.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control.  
  
**_direction_** `str`  
The direction to move the lens (e.g., 'up', 'down', 'left', 'right').  
  
**_speed_** `int`  
The speed at which to move the lens.  
  
**_moveType_** `str`  
The type of movement (reserved for future use, currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the move operation as a dictionary, or a string with error details.  

</div>



---


### `camera_lens_zoom`
Control the zoom function of a camera lens.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control.  
  
**_control_** `Any`  
The zoom control command or value.  
  
**_moveType_** `str`  
The type of movement (reserved for future use, currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the zoom operation as a dictionary, or a string with error details.  

</div>



---


### `list_preset_ptz_camera`
List preset positions for a PTZ (Pan-Tilt-Zoom) camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the PTZ camera to list presets for.  
  
**_offset_** `int`  
The starting index for the preset list.  
  
**_limit_** `int`  
The maximum number of presets to return. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing the list of PTZ presets, or a string with error details.  

</div>



---


### `move_camera_lens_to_preset_position`
Move the camera lens to a specified preset position.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control.  
  
**_presetId_** `Any`  
The ID of the preset position to move to.  
  
**_position_** `Any`  
The position value for the preset.  
  
**_speed_** `Any`  
The speed at which to move the lens.  
  
**_type_** `Any`  
The type of movement or preset.  
  
**_isPatrol_** `bool`  
Whether the movement is part of a patrol operation. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the move operation as a dictionary, or a string with error details.  

</div>



---


### `list_patrol_cameras`
List patrols for a PTZ (Pan-Tilt-Zoom) camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the PTZ camera to list patrols for.  
  
**_offset_** `int`  
The starting index for the patrol list.  
  
**_limit_** `int`  
The maximum number of patrols to return. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing the list of PTZ patrols, or a string with error details.  

</div>



---


### `force_cam_to_execute_patrol`
Force a camera to execute a specified patrol.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to execute the patrol.  
  
**_patrolId_** `Any`  
The ID of the patrol to execute. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the patrol execution as a dictionary, or a string with error details.  

</div>



---


### `focus_camera`
Control the focus function of a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control.  
  
**_control_** `Any`  
The focus control command or value.  
  
**_moveType_** `Any`  
The type of movement (reserved for future use, currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the focus operation as a dictionary, or a string with error details.  

</div>



---


### `control_camera_iris_in_out`
Control the iris (in/out) function of a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control.  
  
**_control_** `Any`  
The iris control command or value.  
  
**_moveType_** `Any`  
The type of movement (reserved for future use, currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the iris control operation as a dictionary, or a string with error details.  

</div>



---


### `auto_focus`
Perform an auto-focus operation on a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to auto-focus.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the auto-focus operation as a dictionary, or a string with error details.  

</div>



---


### `move_cam_lens_to_absolute_position`
Move the camera lens to an absolute position.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_posX_** `int`  
The X coordinate for the absolute position.  
  
**_posY_** `int`  
The Y coordinate for the absolute position. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the move operation as a dictionary, or a string with error details.  

</div>



---


### `move_cam_to_home_position`
Move the camera to its home position.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to move to the home position. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the move operation as a dictionary, or a string with error details.  

</div>



---


### `auto_pan_camera`
Automatically pan the camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to auto-pan.  
  
**_moveType_** `str`  
The type of movement (reserved for future use, currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the auto-pan operation as a dictionary, or a string with error details.  

</div>



---


### `start_stop_object_tracking`
Start or stop object tracking for a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control object tracking.  
  
**_moveType_** `str`  
The type of movement (reserved for future use, currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the object tracking operation as a dictionary, or a string with error details.  

</div>



---


### `start_stop_external_recording`
Start or stop external recording for a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ExternalRecording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
The ID of the camera to control external recording.  
  
**_action_** `str`  
The action to perform (e.g., 'start' or 'stop'). (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the external recording operation as a dictionary, or a string with error details.  

</div>



---


### `query_event_list_by_filter`
Query the event list by applying various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The starting index for the event list.  
  
**_limit_** `int`  
The maximum number of events to return.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs to filter events.  
  
**_fromTime_** `int`  
Start time (timestamp) for filtering events.  
  
**_toTime_** `int`  
End time (timestamp) for filtering events.  
  
**_dsld_** `int`  
Device slot ID to filter events.  
  
**_mountId_** `int`  
Mount ID to filter events.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing the filtered event list, or a string with error details.  

</div>



---


### `delete_recordings`
Delete specific recordings from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `int`  
The ID or comma-separated list of IDs of the recordings to delete.  
  
**_dsld_** `int`  
Device slot ID associated with the recordings.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation as a dictionary, or a string with error details.  

</div>



---


### `delete_events_by_filter`
Delete events from Surveillance Station by applying various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_reason_** `str`  
The reason for deleting the events.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs to filter events.  
  
**_fromTime_** `Any`  
Start time (timestamp) for filtering events.  
  
**_toTime_** `Any`  
End time (timestamp) for filtering events.  
  
**_locked_** `int`  
Whether to include locked events.  
  
**_evtSrcType_** `int`  
Event source type.  
  
**_evtSrcId_** `int`  
Event source ID.  
  
**_blIncludeSnapshot_** `bool`  
Whether to include snapshots in the deletion.  
  
**_includeAllCam_** `bool`  
Whether to include all cameras.  
  
**_from_end_** `int`  
End index for the filter range.  
  
**_from_start_** `int`  
Start index for the filter range. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation as a dictionary, or a string with error details.  

</div>



---


### `delete_all_recordings`
Delete all recordings from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation as a dictionary, or a string with error details.  

</div>



---


### `apply_settings_advance_tab`
Apply advanced settings in the Surveillance Station recording tab.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_rotateUnrecogCam_** `bool`  
Whether to rotate unrecognized cameras. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the apply operation as a dictionary, or a string with error details.  

</div>



---


### `count_by_number_of_event`
Count the number of events by category, with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `bool`  
Whether to offset the results.  
  
**_limit_** `int`  
The maximum number of results to return.  
  
**_reason_** `str`  
The reason for filtering events.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs to filter events.  
  
**_fromTime_** `int`  
Start time (timestamp) for filtering events.  
  
**_toTime_** `int`  
End time (timestamp) for filtering events.  
  
**_locked_** `int`  
Whether to include locked events.  
  
**_evtSrcType_** `int`  
Event source type.  
  
**_evtSrcId_** `int`  
Event source ID.  
  
**_blIncludeSnapshot_** `bool`  
Whether to include snapshots in the count.  
  
**_includeAllCam_** `bool`  
Whether to include all cameras. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing the event count by category, or a string with error details.  

</div>



---


### `keep_event_play_alive`
Keep the event play session alive.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the keepalive operation as a dictionary, or a string with error details.  

</div>



---


### `stop_recording_event`
Stop a recording event for the specified event IDs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `Any`  
The ID or list of IDs of the events to stop recording. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the stop operation as a dictionary, or a string with error details.  

</div>



---


### `load_settings_in_advanced_tab`
Load settings from the advanced tab in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Dictionary containing the advanced settings, or a string with error details.  

</div>



---


### `lock_selected_event`
Lock selected events by applying various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_reason_** `str`  
The reason for locking the events.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs to filter events.  
  
**_fromTime_** `int`  
Start time (timestamp) for filtering events.  
  
**_toTime_** `int`  
End time (timestamp) for filtering events.  
  
**_locked_** `int`  
Whether to lock the events.  
  
**_evtSrcType_** `int`  
Event source type.  
  
**_evtSrcId_** `int`  
Event source ID.  
  
**_blIncludeSnapshot_** `bool`  
Whether to include snapshots in the lock operation.  
  
**_includeAllCam_** `bool`  
Whether to include all cameras.  
  
**_from_end_** `int`  
End index for the filter range.  
  
**_from_start_** `int`  
Start index for the filter range. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation as a dictionary, or a string with error details.  

</div>



---


### `unlock_selected_event`
Unlock selected events by their IDs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of event IDs to unlock.  
  
**_dsld_** `int`  
Device slot ID associated with the events. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation as a dictionary, or a string with error details.  

</div>



---


### `unlock_selected_filter_event`
Unlock events by applying various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_reason_** `str`  
The reason for unlocking the events.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs to filter events.  
  
**_fromTime_** `int`  
Start time (timestamp) for filtering events.  
  
**_toTime_** `int`  
End time (timestamp) for filtering events.  
  
**_locked_** `int`  
Whether to unlock only locked events.  
  
**_evtSrcType_** `int`  
Event source type.  
  
**_evtSrcId_** `int`  
Event source ID. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation as a dictionary, or a string with error details.  

</div>



---


### `lock_selected_recordings`
Lock selected recordings by their IDs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of recording IDs to lock.  
  
**_dsld_** `int`  
Device slot ID associated with the recordings.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation as a dictionary, or a string with error details.  

</div>



---


### `download_recordings`
Download recordings by specifying recording ID and optional parameters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
The ID of the recording to download.  
  
**_mountId_** `int`  
The mount ID associated with the recording.  
  
**_offsetTimeMs_** `int`  
Offset time in milliseconds for the download.  
  
**_playTimeMs_** `int`  
Playback time in milliseconds for the download.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The downloaded recording as a binary response, or a string with error details.  

</div>



---


### `check_if_recording_playable`
Check if a recording is playable by event ID and optional parameters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventId_** `int`  
The event ID of the recording to check.  
  
**_chkDetail_** `bool`  
Whether to check detailed information.  
  
**_mountId_** `int`  
The mount ID associated with the recording.  
  
**_dsld_** `int`  
Device slot ID. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the check as a dictionary, or a string with error details.  

</div>



---


### `play_specific_recording`
Stream a specific recording from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_recordingId_** `int`  
The ID of the recording to play.  
  
**_alertRecording_** `bool`  
Whether the recording is an alert recording.  
  
**_mountId_** `int`  
The mount ID associated with the recording.  
  
**_dsld_** `int`  
Device slot ID.  
  
**_videoCodec_** `int`  
Video codec to use for streaming. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Streaming information or error details.  

</div>



---


### `download_merged_recording_files`
Download merged files of recordings within a UTC time range for a target camera.  
If there are different resolutions or codecs within the time range, recordings will be merged as much as possible,
and the download file will be a zip file.  
This method starts a task with a keep-alive mechanism.
Use GetRangeExportProgress to get the latest progress and keep-alive.
After receiving progress 100, use OnRangeExportDone to download the exported recording within 1 minute.
To cancel the export task, do not send GetRangeExportProgress or OnRangeExportDone; the system will clean up processed files.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
The camera ID to export recordings from.  
  
**_fromTime_** `int`  
Start UTC timestamp for the export range.  
  
**_toTime_** `int`  
End UTC timestamp for the export range.  
  
**_fileName_** `str`  
Name of the output file. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task information for the export or error details.  

</div>



---


### `get_newest_progress_keep_alive`
Get the latest progress of a range export task and keep the task alive.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dlid_** `int`  
The download task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Progress information or error details.  

</div>



---


### `download_recording_from_target`
Download the exported recording file from a completed range export task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dlid_** `int`  
The download task ID.  
  
**_fileName_** `str`  
Name of the file to download. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Downloaded file data or error details.  

</div>



---


### `handle_load_event_export`
Load exported event recordings with optional pagination.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Export` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
The starting index for loading events.  
  
**_limit_** `bool`  
The maximum number of events to load.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Exported event information or error details.  

</div>



---


### `check_name_export_event`
Check if an export event name is valid or already exists.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Export` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
The data source ID.  
  
**_name_** `int`  
The name to check for the export event.  
  
**_share_** `str`  
The share name associated with the export event.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the name check or error details.  

</div>



---


### `get_camera_information_list`
Retrieve the list of camera information for event export.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Export` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dslld_** `int`  
The ID of the data source (recording server) to query cameras from.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Camera information list or error details.  

</div>



---


### `check_destination_folder_availability`
Check if the destination folder has enough available space for export.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Export` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_freeSize_** `int`  
Required free size in bytes.  
  
**_startTime_** `int`  
Start time of the export range (UTC timestamp).  
  
**_stopTime_** `int`  
End time of the export range (UTC timestamp).  
  
**_camIdList_** `str`  
Comma-separated list of camera IDs to check.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Availability information or error details.  

</div>



---


### `handle_save_event_export`
Save an event export task with the specified parameters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Export` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Name of the export task.  
  
**_srcDsId_** `int`  
Source data source ID.  
  
**_dstDsId_** `int`  
Destination data source ID.  
  
**_dstdir_** `str`  
Destination directory for export.  
  
**_freesize_** `int`  
Required free size in bytes.  
  
**_start_time_** `int`  
Start time of the export range (UTC timestamp).  
  
**_stop_time_** `int`  
End time of the export range (UTC timestamp).  
  
**_isoverwrite_** `int`  
Whether to overwrite existing files (1 for true, 0 for false).  
  
**_camlistid_** `str`  
Comma-separated list of camera IDs to export.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `get_event_export_info_from_recording_server`
Retrieve event export information from the recording server.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Export` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_time_** `int`  
Start time of the export range (UTC timestamp).  
  
**_stop_time_** `int`  
End time of the export range (UTC timestamp).  
  
**_camlistid_** `str`  
Comma-separated list of camera IDs.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Export information or error details.  

</div>



---


### `load_event_mount`
Load event mount information for export.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Mount` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Mount information or error details.  

</div>



---


### `redirect_webapi_to_target_ds`
Redirect a WebAPI request to a target DiskStation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
Target DiskStation ID.  
  
**_webAPI_** `Any`  
WebAPI information to redirect (array of webAPI_info).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the redirect operation or error details.  

</div>



---


### `modify_share_privilege`
Modify the share privilege settings in Surveillance Station CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_privSet_** `int`  
Privilege set value.  
  
**_shareName_** `str`  
Name of the share to modify.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the privilege modification or error details.  

</div>



---


### `apply_option_settings`
Apply option settings for Surveillance Station CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_central_auto_video_relay_** `bool`  
Enable or disable central auto video relay.  
  
**_central_enable_** `bool`  
Enable or disable central management.  
  
**_central_mode_** `str`  
Set the central management mode.  
  
**_central_rec_mask_mode_** `bool`  
Enable or disable central recording mask mode.  
  
**_central_rec_sync_time_** `bool`  
Enable or disable central recording time synchronization.  
  
**_nvr_enable_** `bool`  
Enable or disable NVR.  
  
**_nvr_lang_** `str`  
Set the NVR language. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the apply operation or error details.  

</div>



---


### `get_cms_info`
Retrieve CMS (Central Management System) information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_isPolling_** `bool`  
Whether to poll for CMS information. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
CMS information or error details.  

</div>



---


### `get_log_recording_data_from_target_ds`
Retrieve log recording data from a target DiskStation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_syncType_** `int`  
Type of synchronization.  
  
**_syncTargetId_** `int`  
ID of the target DiskStation for synchronization.  
  
**_limit_** `int`  
Limit the number of records returned. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Log recording data or error details.  

</div>



---


### `get_samba_service`
Check if the Samba service is enabled on the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Samba service status or error details.  

</div>



---


### `check_if_samba_on_and_rec_enabled`
Check if Samba is enabled and recording is enabled on the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Status of Samba and recording or error details.  

</div>



---


### `get_encoded_single_image_of_camera`
Retrieve an encoded single image (snapshot) from a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
ID of the camera to get the snapshot from.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Encoded image data or error details.  

</div>



---


### `get_cms_status`
Retrieve the status of the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
ID of the camera to check status for. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
CMS status or error details.  

</div>



---


### `enable_smb_service`
Enable the Samba service on the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation or error details.  

</div>



---


### `notify_slave_ds_to_disconnect`
Notify a slave DiskStation to disconnect from the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the notification or error details.  

</div>



---


### `lock_recording_server_prevent_setting_change`
Lock the recording server to prevent setting changes.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_locked_** `bool`  
Whether to lock the server. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation or error details.  

</div>



---


### `enable_ds_into_recording_server`
Enable a DiskStation as a recording server in the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_adminUsername_** `str`  
Administrator username.  
  
**_adminPasswd_** `str`  
Administrator password.  
  
**_central_rec_mask_mode_** `str`  
Central recording mask mode.  
  
**_central_rec_sync_time_** `str`  
Central recording synchronization time.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation or error details.  

</div>



---


### `unpair_recording_servers`
Unpair recording servers from the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_adminUsername_** `str`  
Administrator username.  
  
**_key_** `str`  
Key for unpairing.  
  
**_mac_** `str`  
MAC address of the server.  
  
**_cmsMode_** `int`  
CMS mode.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unpair operation or error details.  

</div>



---


### `get_free_memory_size`
Retrieve the free memory size from the target DiskStation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Free memory size information or error details.  

</div>



---


### `handle_slave_ds`
Handle slave DiskStation operations such as locking or authentication.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_lock_** `bool`  
Whether to lock the slave DiskStation.  
  
**_adminUsername_** `str`  
Administrator username.  
  
**_key_** `str`  
Authentication key.  
  
**_mac_** `str`  
MAC address of the slave DiskStation.  
  
**_masterAuthKey_** `str`  
Master authentication key. (To check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the operation or error details.  

</div>



---


### `get_target_ds_info`
Retrieve information about the target slave DiskStation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_slaveDslp_** `str`  
Slave DiskStation IP or identifier.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Target DiskStation information or error details.  

</div>



---


### `logout_slave_ds`
Log out a slave DiskStation from the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_adminUsername_** `str`  
Administrator username.  
  
**_key_** `str`  
Authentication key.  
  
**_mac_** `str`  
MAC address of the slave DiskStation.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the logout operation or error details.  

</div>



---


### `pair_slave_ds`
Pair a slave DiskStation with the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsname_** `str`  
Name of the slave DiskStation.  
  
**_slaveDslp_** `str`  
Slave DiskStation IP or identifier.  
  
**_port_** `int`  
Port number for connection.  
  
**_masterAuthKey_** `str`  
Master authentication key.  
  
**_model_** `str`  
Model of the slave DiskStation.  
  
**_mac_** `str`  
MAC address of the slave DiskStation.  
  
**_cms_locked_** `bool`  
Whether the CMS is locked.  
  
**_cms_masked_** `bool`  
Whether the CMS is masked.  
  
**_cms_sync_time_** `bool`  
Synchronize time with CMS. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the pairing operation or error details.  

</div>



---


### `login_slave_ds`
Log in a slave DiskStation to the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_adminUsername_** `str`  
Administrator username.  
  
**_key_** `str`  
Authentication key.  
  
**_mac_** `str`  
MAC address of the slave DiskStation.  
  
**_masterAuthKey_** `str`  
Master authentication key.  
  
**_hostName_** `str`  
Hostname of the slave DiskStation.  
  
**_hostPort_** `int`  
Port number for connection.  
  
**_ignoreAuthError_** `str`  
Ignore authentication errors.  
  
**_hostDisconnect_** `bool`  
Whether to disconnect the host.  
  
**_blUpdateVolSpace_** `bool`  
Update volume space information.  
  
**_enable_rec_** `bool`  
Enable recording.  
  
**_cms_locked_** `bool`  
Whether the CMS is locked.  
  
**_cms_masked_** `bool`  
Whether the CMS is masked.  
  
**_cms_sync_time_** `bool`  
Synchronize time with CMS. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the login operation or error details.  

</div>



---


### `save_slave_ds`
Save or update a slave DiskStation's configuration in the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_slavedsName_** `str`  
Name of the slave DiskStation.  
  
**_slavedsModel_** `str`  
Model of the slave DiskStation.  
  
**_slavedsPort_** `int`  
Port number used by the slave DiskStation.  
  
**_slavedsVersion_** `str`  
Version of the slave DiskStation.  
  
**_slavedsMaxCamNum_** `int`  
Maximum number of cameras supported by the slave DiskStation.  
  
**_slavedsId_** `str`  
Identifier for the slave DiskStation.  
  
**_slavedsIP_** `str`  
IP address of the slave DiskStation.  
  
**_slavedsEnable_** `int`  
Enable status of the slave DiskStation.  
  
**_slavedsCamCnt_** `bool`  
Number of cameras currently connected to the slave DiskStation.  
  
**_adminUsername_** `str`  
Administrator username for authentication.  
  
**_adminPasswd_** `str`  
Administrator password for authentication.  
  
**_cms_locked_** `bool`  
Whether the CMS is locked.  
  
**_cms_masked_** `bool`  
Whether the CMS is masked.  
  
**_cms_sync_time_** `bool`  
Synchronize time with CMS. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `load_slave_ds_list`
Load the list of slave DiskStations from the CMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.SlavedsList` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_blNeedStatus_** `bool`  
Whether to include status information.  
  
**_blGetSortInfo_** `bool`  
Whether to include sorting information.  
  
**_blRuntimeInfo_** `bool`  
Whether to include runtime information.  
  
**_dslds_** `str`  
Comma-separated list of DiskStation IDs to load.  
  
**_sortInfo_** `int`  
Sorting information.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of slave DiskStations or error details.  

</div>



---


### `count_number_of_logs`
Count the number of logs in Surveillance Station based on various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_slavedsName_** `str`  
Name of the slave DiskStation.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of logs to count.  
  
**_level_** `str`  
Log level filter.  
  
**_filterCamera_** `str`  
Filter by camera.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs.  
  
**_dsfrom_** `int`  
Start time (timestamp).  
  
**_to_** `int`  
End time (timestamp).  
  
**_keyword_** `str`  
Keyword to search in logs.  
  
**_keywordDsId_** `str`  
DiskStation ID for keyword search.  
  
**_time2String_** `str`  
Time string for filtering.  
  
**_dsId_** `str`  
DiskStation ID.  
  
**_srcType_** `int`  
Source type filter.  
  
**_timezoneOffset_** `int`  
Timezone offset.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Count of logs or error details.  

</div>



---


### `clear_selected_logs`
Clear selected logs from Surveillance Station based on various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_blClearAll_** `bool`  
Whether to clear all logs.  
  
**_level_** `int`  
Log level filter.  
  
**_dsId_** `int`  
DiskStation ID.  
  
**_filterCamera_** `str`  
Filter by camera.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs.  
  
**_dsfrom_** `int`  
Start time (timestamp).  
  
**_to_** `int`  
End time (timestamp).  
  
**_keyword_** `str`  
Keyword to search in logs.  
  
**_keywordDsId_** `str`  
DiskStation ID for keyword search.  
  
**_srcType_** `int`  
Source type filter.  
  
**_timezoneOffset_** `int`  
Timezone offset.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the clear operation or error details.  

</div>



---


### `get_information_log`
Retrieve information logs from Surveillance Station based on various filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of logs to retrieve.  
  
**_level_** `str`  
Log level filter.  
  
**_filterCamera_** `str`  
Filter by camera.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs.  
  
**_dsfrom_** `int`  
Start time (timestamp).  
  
**_to_** `int`  
End time (timestamp).  
  
**_keyword_** `str`  
Keyword to search in logs.  
  
**_keywordDsId_** `str`  
DiskStation ID for keyword search.  
  
**_time2String_** `str`  
Time string for filtering.  
  
**_dsId_** `int`  
DiskStation ID.  
  
**_srcType_** `int`  
Source type filter.  
  
**_all_** `bool`  
Whether to retrieve all logs.  
  
**_blIncludeRecCnt_** `str`  
Include recording count information.  
  
**_blIncludeAuInfo_** `str`  
Include additional information.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of information logs or error details.  

</div>



---


### `get_advanced_settings_logs`
Retrieve advanced log settings from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Log` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Advanced log settings or error details.  

</div>



---


### `set_advanced_setting_logs`
Set advanced log settings in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_data_** `Any`  
List of log type settings to apply.
Example:
    data=\[\{"SSLogType":321912835,"enable":1\},\{"SSLogType":321912836,"enable":0\}\]  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `load_license_data`
Load license data from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.License` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_num_only_** `int`  
If set, only the number of licenses will be returned.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
License data or error details.  

</div>



---


### `check_license_quota`
Check the license quota for cameras in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.License` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camList_** `Any`  
List of camera information dictionaries.
Example:
    camList = \[\{"ip": "10.13.22.141", "model": "DCS-3110", "vendor": "DLink", "port": 80\}\]  
  
**_camServerId_** `int`  
Camera server ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
License quota information or error details.  

</div>



---


### `get_http_video_stream`
Retrieve an HTTP video event stream from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Stream` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_writeHeader_** `bool`  
Whether to include headers in the stream.  
  
**_analyevent_** `bool`  
Whether to analyze events in the stream.  
  
**_mountId_** `int`  
Mount ID for the stream.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Video stream data or error details.  

</div>



---


### `save_action_rule`
Save or update an action rule in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Action rule ID.  
  
**_name_** `str`  
Name of the action rule.  
  
**_ruleType_** `int`  
Type of the rule.  
  
**_actType_** `int`  
Action type.  
  
**_evtSrc_** `int`  
Event source.  
  
**_evtDsId_** `int`  
Event DiskStation ID.  
  
**_evtDevId_** `int`  
Event device ID.  
  
**_evtId_** `int`  
Event ID.  
  
**_evtItem_** `int`  
Event item.  
  
**_evtMinIntvl_** `int`  
Minimum interval between events.  
  
**_Actions_** `Any`  
List of actions to perform.  
  
**_actSchedule_** `str`  
Action schedule.  
  
**_Id_** `int`  
Alternative action rule ID.  
  
**_actSrc_** `int`  
Action source.  
  
**_actDsId_** `int`  
Action DiskStation ID.  
  
**_actDevId_** `int`  
Action device ID.  
  
**_actId_** `int`  
Action ID.  
  
**_actTimes_** `int`  
Number of times to perform the action.  
  
**_actTimeUnit_** `int`  
Time unit for the action.  
  
**_actTimeDur_** `int`  
Duration for the action.  
  
**_actItemId_** `int`  
Action item ID.  
  
**_actRetPos_** `int`  
Action return position.  
  
**_extUrl_** `str`  
External URL for the action.  
  
**_userName_** `str`  
Username for authentication.  
  
**_password_** `str`  
Password for authentication. (Currently not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `download_action_rule`
Download the history of action rules from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Downloaded action rule history or error details.  

</div>



---


### `send_data_2_player`
Send data to the Surveillance Station player.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the send operation or error details.  

</div>



---


### `delete_all_histories_of_action_rule`
Delete all histories of specified action rules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of action rule IDs to delete histories for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `list_action_rules`
List action rules in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `str`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of action rules to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of action rules or error details.  

</div>



---


### `disable_action_rules`
Disable specified action rules in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of action rule IDs to disable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the disable operation or error details.  

</div>



---


### `enable_action_rules`
Enable specified action rules in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of action rule IDs to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation or error details.  

</div>



---


### `list_history_action_rules`
List the history of action rules in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of history records to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of action rule histories or error details.  

</div>



---


### `delete_action_rule`
Delete specified action rules from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ActionRule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of action rule IDs to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `get_list_of_emaps`
Retrieve a list of eMaps from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Emap` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `str`  
Maximum number of eMaps to return.  
  
**_emapIds_** `int`  
Specific eMap IDs to retrieve.  
  
**_includeItems_** `int`  
Whether to include items in the eMap.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of eMaps or error details.  

</div>



---


### `get_specific_emaps_setting`
Retrieve specific eMap settings from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Emap` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_emapIds_** `int`  
The ID(s) of the eMap(s) to retrieve settings for.  
  
**_includeImage_** `int`  
Whether to include the eMap image in the response.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The eMap settings or error details.  

</div>



---


### `get_emap_image`
Retrieve an eMap image from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Emap.Image` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filename_** `str`  
The filename of the eMap image to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The eMap image data or error details.  

</div>



---


### `get_autorized_ds_token`
Retrieve an authorized DiskStation token for notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The authorized token or error details.  

</div>



---


### `set_message_event`
Set a customized message event in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventTypes_** `str`  
The type(s) of event(s) to set the message for.  
  
**_subject_** `str`  
The subject of the message.  
  
**_content_** `str`  
The content of the message.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `get_message_event`
Retrieve a customized message event from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventTypes_** `int`  
The type(s) of event(s) to retrieve the message for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The message event data or error details.  

</div>



---


### `set_notification_sender_name`
Set the sender name for Surveillance Station notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ss_pkg_name_** `str`  
The sender name to set.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `get_notification_sender_name`
Retrieve the sender name for Surveillance Station notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The sender name or error details.  

</div>



---


### `set_advanced_notification_setting`
Set advanced notification settings in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_blSyncDSMNotify_** `bool`  
Whether to synchronize DSM notifications.  
  
**_blCompactMsg_** `bool`  
Whether to enable compact message format.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `get_advanced_notification_setting`
Retrieve advanced notification settings from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The advanced notification settings or error details.  

</div>



---


### `send_test_mesg_to_primary_secondary_phone`
Send a test message to the primary and secondary phone numbers via SMS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_smsEnable_** `bool`  
Whether SMS notifications are enabled.  
  
**_smsMethod_** `int`  
The SMS sending method.  
  
**_smsProvider_** `str`  
The SMS provider name.  
  
**_userName_** `str`  
Username for SMS provider authentication.  
  
**_password_** `str`  
Password for SMS provider authentication.  
  
**_confirmPassword_** `str`  
Confirmation of the password.  
  
**_primaryPhoneCode_** `str`  
Country code for the primary phone.  
  
**_primaryPhonePrefix_** `str`  
Prefix for the primary phone.  
  
**_secondaryPhoneCode_** `str`  
Country code for the secondary phone.  
  
**_secondaryPhonePrefix_** `str`  
Prefix for the secondary phone.  
  
**_secondaryPhoneNumber_** `str`  
The secondary phone number.  
  
**_setMinMessageInterval_** `bool`  
Whether to set a minimum message interval.  
  
**_minMessageInterval_** `int`  
The minimum interval between messages.  
  
**_hasSysSms_** `bool`  
Whether system SMS is enabled.  
  
**_apiId_** `str`  
The API ID for the SMS provider.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the test message operation or error details.  

</div>



---


### `get_setting_notification_sms`
Retrieve the SMS notification settings from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The SMS notification settings or error details.  

</div>



---


### `set_sms_service_setting`
Set the SMS service settings for Surveillance Station notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_smsEnable_** `bool`  
Whether SMS notifications are enabled.  
  
**_smsMethod_** `int`  
The SMS sending method.  
  
**_smsProvider_** `str`  
The SMS provider name.  
  
**_userName_** `str`  
Username for SMS provider authentication.  
  
**_password_** `str`  
Password for SMS provider authentication.  
  
**_confirmPassword_** `str`  
Confirmation of the password.  
  
**_primaryPhoneCode_** `str`  
Country code for the primary phone.  
  
**_primaryPhonePrefix_** `str`  
Prefix for the primary phone.  
  
**_secondaryPhoneCode_** `str`  
Country code for the secondary phone.  
  
**_secondaryPhonePrefix_** `str`  
Prefix for the secondary phone.  
  
**_secondaryPhoneNumber_** `str`  
The secondary phone number.  
  
**_setMinMessageInterval_** `bool`  
Whether to set a minimum message interval.  
  
**_minMessageInterval_** `int`  
The minimum interval between messages.  
  
**_hasSysSms_** `bool`  
Whether system SMS is enabled.  
  
**_apiId_** `str`  
The API ID for the SMS provider.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `send_test_sms`
Send a test SMS notification from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_attachSnapshot_** `bool`  
Whether to attach a snapshot to the SMS.  
  
**_enableInterval_** `bool`  
Whether to enable message interval.  
  
**_mobileEnable_** `bool`  
Whether to enable mobile notifications.  
  
**_msgInterval_** `str`  
The interval between messages.  
  
**_primaryEmail_** `str`  
The primary email address for notifications.  
  
**_secondaryEmail_** `str`  
The secondary email address for notifications.  
  
**_synoMailEnable_** `bool`  
Whether to enable Synology Mail notifications.  
  
**_mail_recipient_** `str`  
The recipient of the test mail.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the test SMS operation or error details.  

</div>



---


### `send_test_mail`
Send a test verification mail for Surveillance Station notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.PushService` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_attachSnapshot_** `bool`  
Whether to attach a snapshot to the email.  
  
**_enableInterval_** `bool`  
Whether to enable message interval.  
  
**_mobileEnable_** `bool`  
Whether to enable mobile notifications.  
  
**_msgInterval_** `str`  
The interval between messages.  
  
**_primaryEmail_** `str`  
The primary email address for notifications.  
  
**_secondaryEmail_** `str`  
The secondary email address for notifications.  
  
**_synoMailEnable_** `bool`  
Whether to enable Synology Mail notifications.  
  
**_mail_recipient_** `str`  
The recipient of the test mail.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the test mail operation or error details.  

</div>



---


### `list_mobile_paired_devices`
List mobile devices paired with Surveillance Station for push notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.PushService` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_attachSnapshot_** `bool`  
Whether to attach a snapshot to the notification.  
  
**_enableInterval_** `bool`  
Whether to enable message interval.  
  
**_mobileEnable_** `bool`  
Whether to enable mobile notifications.  
  
**_msgInterval_** `str`  
The interval between messages.  
  
**_primaryEmail_** `str`  
The primary email address for notifications.  
  
**_secondaryEmail_** `str`  
The secondary email address for notifications.  
  
**_synoMailEnable_** `bool`  
Whether to enable Synology Mail notifications.  
  
**_mail_recipient_** `str`  
The recipient of the notification.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of paired mobile devices or error details.  

</div>



---


### `unpair_device`
Unpair a mobile device from Surveillance Station notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.PushService` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_targetIds_** `str`  
The ID(s) of the device(s) to unpair.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unpair operation or error details.  

</div>



---


### `get_controller_access_schedule`
Retrieve the access control controller schedule from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_targetIds_** `str`  
The ID(s) of the controllers to retrieve the schedule for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The controller access schedule or error details.  

</div>



---


### `get_camera_alarm_schedule`
Retrieve the alarm schedule for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `int`  
The ID of the camera.  
  
**_alarmdx_** `int`  
Additional alarm parameter (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The camera alarm schedule or error details.  

</div>



---


### `get_sys_dependent_schedule`
Retrieve the system dependent schedule for Surveillance Station events.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventGroupTypes_** `int`  
The type(s) of event groups to retrieve the schedule for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The system dependent schedule or error details.  

</div>



---


### `set_batch_schedule`
Set batch schedules for events, cameras, or camera groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventTypes_** `str`  
The type(s) of events to schedule.  
  
**_schedule_** `Any`  
The schedule data to apply.  
  
**_cameraIds_** `str`  
The IDs of cameras to apply the schedule to.  
  
**_cameraGroupIds_** `str`  
The IDs of camera groups to apply the schedule to.  
  
**_filter_** `int`  
Additional filter parameter (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the batch schedule operation or error details.  

</div>



---


### `get_access_ctrl_door_schedule`
Retrieve the access control door schedule from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_doorId_** `str`  
The ID of the door to retrieve the schedule for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The door schedule or error details.  

</div>



---


### `get_camera_schedule`
Retrieve the schedule for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `str`  
The ID of the camera to retrieve the schedule for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The camera schedule or error details.  

</div>



---


### `set_sys_dependent_schedule`
Set the system dependent schedule for Surveillance Station events.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventType_** `int`  
The type of event to set the schedule for.  
  
**_schedule_** `Any`  
The schedule data to apply.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `set_controller_access_schedule`
Set the access control schedule for a controller or door.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventType_** `int`  
The type of event to set the schedule for.  
  
**_schedule_** `Any`  
The schedule data to apply.  
  
**_doorId_** `int`  
The ID of the door to set the schedule for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `set_camera_schedule`
Set the schedule for a specific camera in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventType_** `int`  
The type of event to set the schedule for.  
  
**_schedule_** `Any`  
The schedule data to apply.  
  
**_cameraId_** `Any`  
The ID of the camera to set the schedule for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `get_notification_email_string`
Retrieve the notification email settings string from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Email` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The notification email settings or error details.  

</div>



---


### `set_adv_tab_info_filter`
Set the advanced tab information filter for notification emails.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.Email` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_X_** `int`  
The filter value to set (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `create_sms_service_provider`
Create a new SMS service provider for Surveillance Station notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS.ServiceProvider` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_providerName_** `str`  
The name of the SMS provider.  
  
**_providerPort_** `int`  
The port used by the provider.  
  
**_providerUrl_** `str`  
The URL of the provider.  
  
**_providerTemplate_** `str`  
The message template for the provider.  
  
**_providerSepChar_** `str`  
The separator character used by the provider.  
  
**_providerNeedSSL_** `bool`  
Whether SSL is required for the provider.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the create operation or error details.  

</div>



---


### `list_sms_provider`
List all SMS service providers configured in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS.ServiceProvider` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of SMS providers or error details.  

</div>



---


### `delete_sms_service_provider`
Delete an SMS service provider from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Notification.SMS.ServiceProvider` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_providerName_** `str`  
The name of the SMS provider to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `get_addson_to_update`
Retrieve information about add-ons that require updates in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Add-on update information or error details.  

</div>



---


### `enable_specific_addon`
Enable a specific add-on in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to enable.  
  
**_servicename_** `str`  
The name of the add-on service to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation or error details.  

</div>



---


### `get_specific_addon_update_info`
Retrieve update information for a specific add-on in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to check for updates.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Update information or error details.  

</div>



---


### `get_specific_addon_info`
Retrieve information for a specific add-on in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to retrieve information for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Add-on information or error details.  

</div>



---


### `get_total_addon_info`
Retrieve information about all add-ons in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of all add-ons or error details.  

</div>



---


### `update_addon_package`
Update an add-on package in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to update.  
  
**_filePath_** `str`  
The file path to the add-on package (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the update operation or error details.  

</div>



---


### `check_addon_status`
Check the enable status of a specific add-on in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to check (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Status information or error details.  

</div>



---


### `disable_addon`
Disable a specific add-on in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to disable.  
  
**_serviceName_** `str`  
The name of the add-on service to disable (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the disable operation or error details.  

</div>



---


### `set_addon_autoupdate`
Set the auto-update setting for a specific add-on in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AddOns` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_service_** `int`  
The ID of the add-on service to configure.  
  
**_BlEnabled_** `Any`  
Whether auto-update is enabled (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `delete_specific_camera_recording_server`
Delete a specific camera recording server in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camIdList_** `str`  
List of camera IDs to delete from the recording server (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `get_camera_event_analytic`
Retrieve camera event analytics from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camIdList_** `str`  
List of camera IDs to retrieve analytics for (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Analytics data or error details.  

</div>



---


### `delete_selected_events`
Delete selected events from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsIdList_** `str`  
List of DS IDs for which to delete events.  
  
**_idList_** `str`  
List of event IDs to delete (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `delete_specific_camera_events`
Delete events for specific cameras in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camIdList_** `str`  
List of camera IDs for which to delete events (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `get_analytic_history`
Retrieve analytic history for cameras in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camIdList_** `str`  
List of camera IDs to retrieve history for.  
  
**_typeListstring_** `str`  
List of analytic types as a string (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Analytic history data or error details.  

</div>



---


### `get_analytic_history_by_filter`
Retrieve analytic history for cameras by filter in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camIdList_** `str`  
List of camera IDs to filter.  
  
**_dsId_** `int`  
The DS ID to filter.  
  
**_lock_** `int`  
Lock status to filter.  
  
**_typeList_** `str`  
List of analytic types as a string (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Filtered analytic history data or error details.  

</div>



---


### `unklock_selected_events`
Unlock selected events in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
The DS ID for which to unlock events.  
  
**_idList_** `str`  
List of event IDs to unlock (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation or error details.  

</div>



---


### `set_camera_analytic_trigger`
Trigger camera analytics for specified cameras in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_trigCamIdList_** `str`  
List of camera IDs to trigger analytics for (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the trigger operation or error details.  

</div>



---


### `flush_event_header`
Flush the header of a specific event in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventId_** `str`  
The ID of the event to flush the header for (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the flush operation or error details.  

</div>



---


### `lock_selected_events`
Lock selected events in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
The DS ID for which to lock events.  
  
**_idList_** `str`  
List of event IDs to lock (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation or error details.  

</div>



---


### `get_analytic_event_from_rec_server`
Retrieve analytic event counts from the recording server for specified cameras.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camIdList_** `str`  
Comma-separated list of camera IDs to query.  
  
**_idList_** `int`  
Additional ID list parameter (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Analytic event count data or error details.  

</div>



---


### `save_analytic_settings`
Save analytic settings for a specific camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Alert.Setting` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
Camera ID to apply settings to.  
  
**_type_** `int`  
Type of analytic.  
  
**_showFrame_** `bool`  
Whether to display the frame.  
  
**_showLine_** `bool`  
Whether to display lines.  
  
**_showVirtualFence_** `bool`  
Whether to display virtual fences.  
  
**_beep_** `bool`  
Whether to enable beep on event.  
  
**_sens_** `int`  
Sensitivity setting.  
  
**_dwellTime_** `int`  
Dwell time setting.  
  
**_direction_** `int`  
Direction setting.  
  
**_objSize_** `int`  
Object size setting.  
  
**_region_** `str`  
Region definition (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `check_if_snapshot_exist`
Check if a snapshot exists for a given ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Snapshot ID to check (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Existence status or error details.  

</div>



---


### `save_snapshot_modification`
Save modifications to a snapshot.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Snapshot ID to modify.  
  
**_createCopy_** `bool`  
Whether to create a copy of the snapshot.  
  
**_width_** `int`  
Width of the snapshot.  
  
**_height_** `int`  
Height of the snapshot.  
  
**_byteSize_** `int`  
Size of the snapshot in bytes.  
  
**_imageData_** `str`  
Image data (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the modification or error details.  

</div>



---


### `count_snapshot_by_category`
Count snapshots by category within a specified range.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_keyword_** `str`  
Keyword to filter snapshots.  
  
**_dsfrom_** `int`  
Start timestamp.  
  
**_to_** `int`  
End timestamp.  
  
**_timezoneOffset_** `int`  
Timezone offset.  
  
**_byteSize_** `int`  
Size of the snapshot in bytes.  
  
**_imageData_** `str`  
Image data (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Count data or error details.  

</div>



---


### `check_any_locked_snapshot`
Check if any locked snapshots exist within a specified range.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `str`  
Snapshot ID(s) to check.  
  
**_dsfrom_** `int`  
Start timestamp.  
  
**_to_** `int`  
End timestamp.  
  
**_keyword_** `str`  
Keyword to filter snapshots (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Lock status or error details.  

</div>



---


### `unlock_snapshot_by_filter`
Unlock snapshots by filter within a specified range.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsfrom_** `int`  
Start timestamp.  
  
**_to_** `int`  
End timestamp.  
  
**_keyword_** `str`  
Keyword to filter snapshots (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation or error details.  

</div>



---


### `list_snapshot_information`
List snapshot information with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
Comma-separated list of snapshot IDs.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_dsfrom_** `int`  
Start timestamp.  
  
**_to_** `int`  
End timestamp.  
  
**_keyword_** `str`  
Keyword to filter snapshots.  
  
**_imgSize_** `int`  
Image size filter.  
  
**_blIncludeAuInfo_** `bool`  
Whether to include additional info.  
  
**_blIncludeRecCnt_** `bool`  
Whether to include recording count.  
  
**_camId_** `int`  
Camera ID filter (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of snapshot information or error details.  

</div>



---


### `unlock_snapshot`
Unlock specific snapshots.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_objList_** `Any`  
List of snapshot objects to unlock (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation or error details.  

</div>



---


### `take_snapshot`
Take a snapshot for a specific camera and DS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
DS ID for the snapshot.  
  
**_camId_** `int`  
Camera ID for the snapshot.  
  
**_blSave_** `bool`  
Whether to save the snapshot (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the snapshot operation or error details.  

</div>



---


### `get_snapshot_setting_function`
Retrieve the snapshot setting function.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Snapshot setting information or error details.  

</div>



---


### `delete_snapshot_by_filter`
Delete snapshots by filter within a specified range.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_deleteAllCommand_** `bool`  
Whether to delete all snapshots.  
  
**_dsfrom_** `int`  
Start timestamp.  
  
**_to_** `int`  
End timestamp.  
  
**_keyword_** `str`  
Keyword to filter snapshots (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `get_snapshot_image`
Retrieve a snapshot image by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Snapshot ID to retrieve.  
  
**_imgSize_** `int`  
Image size (to modify for download?).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Snapshot image data or error details.  

</div>



---


### `lock_snapshot_image`
Lock specific snapshot images.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_objList_** `Any`  
List of snapshot objects to lock.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation or error details.  

</div>



---


### `downld_single_snapshot`
Download a single snapshot by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Snapshot ID to download (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Download result or error details.  

</div>



---


### `save_new_snapshot_setting`
Save new snapshot settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dispSnapshot_** `bool`  
Whether to display snapshots.  
  
**_dispDuration_** `int`  
Display duration for snapshots.  
  
**_limitTotalSize_** `bool`  
Whether to limit total snapshot size.  
  
**_limitSizeInGb_** `int`  
Limit size in GB.  
  
**_addTimestamp_** `bool`  
Whether to add a timestamp to snapshots.  
  
**_timestampPosition_** `int`  
Position of the timestamp.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `save_snapshot`
Save a new snapshot.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camName_** `str`  
Name of the camera.  
  
**_createdTm_** `int`  
Creation timestamp.  
  
**_width_** `int`  
Width of the snapshot.  
  
**_height_** `int`  
Height of the snapshot.  
  
**_byteSize_** `int`  
Size of the snapshot in bytes.  
  
**_imageData_** `str`  
Image data (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `check_snapshot_status`
Check the status of snapshot display.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.SnapShot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dispSnapshot_** `bool`  
Whether to display snapshots.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Status information or error details.  

</div>



---


### `enable_visualstation`
Enable VisualStation devices.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vslist_** `str`  
Comma-separated list of VisualStation IDs to enable (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation or error details.  

</div>



---


### `update_vs_network_config`
Update the network configuration for a VisualStation device.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vsMAc_** `str`  
MAC address of the VisualStation.  
  
**_ip_** `str`  
IP address to assign.  
  
**_mask_** `str`  
Subnet mask.  
  
**_gateway_** `str`  
Gateway address.  
  
**_blDhcp_** `bool`  
Whether to use DHCP.  
  
**_name_** `str`  
Name of the VisualStation (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the update operation or error details.  

</div>



---


### `lock_visualstation_by_id`
Lock VisualStation devices by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vslist_** `str`  
Comma-separated list of VisualStation IDs to lock (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation or error details.  

</div>



---


### `enumerate_vs_owner_info`
Enumerate VisualStation owner information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Owner information or error details.  

</div>



---


### `unlock_visualstation_by_id`
Unlock VisualStation devices by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vslist_** `str`  
Comma-separated list of VisualStation IDs to unlock (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation or error details.  

</div>



---


### `disable_visualstation_by_id`
Disable VisualStation devices by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vslist_** `str`  
Comma-separated list of VisualStation IDs to disable (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the disable operation or error details.  

</div>



---


### `delete_specific_visualstation`
Delete specific VisualStation devices by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vslist_** `str`  
Comma-separated list of VisualStation IDs to delete (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `enumerate_layout_visualstation`
Enumerate VisualStation layouts.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Layout` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vsId_** `int`  
VisualStation ID to filter layouts (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Layout information or error details.  

</div>



---


### `save_layout_information`
Save layout information for a VisualStation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Layout` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Layout ID.  
  
**_vsId_** `int`  
VisualStation ID.  
  
**_name_** `str`  
Name of the layout.  
  
**_canGrpId_** `int`  
Camera group ID.  
  
**_isDefault_** `int`  
Whether this is the default layout.  
  
**_isFixAspectRatio_** `int`  
Whether to fix the aspect ratio.  
  
**_layoutType_** `int`  
Type of the layout.  
  
**_channelList_** `Any`  
List of channels in the layout.  
  
**_customPosList_** `str`  
Custom position list (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `delete_layout_visualstation`
Delete a VisualStation layout.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Layout` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Layout ID to delete.  
  
**_vsId_** `int`  
VisualStation ID (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `clear_visualstation_search_result`
Clear VisualStation search results.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the clear operation or error details.  

</div>



---


### `get_visualstation_ip_info`
Retrieve VisualStation IP information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ip_** `int`  
IP address to search for (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
IP information or error details.  

</div>



---


### `stop_previous_visualstation_search`
Stop the previous VisualStation search operation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the stop operation or error details.  

</div>



---


### `get_visualstation_list`
Retrieve the list of VisualStation devices.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.VisualStation.Layout` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Offset for pagination (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of VisualStation devices or error details.  

</div>



---


### `get_number_of_controller`
Get the number of controllers in the system.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Number of controllers or error details.  

</div>



---


### `get_cardholder_count`
Get the count of cardholders, optionally filtered by keyword.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterKeyword_** `str`  
Keyword to filter cardholders.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Cardholder count or error details.  

</div>



---


### `enum_all_controllers_logger`
Enumerate all controller logger configurations.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Logger configuration information or error details.  

</div>



---


### `get_cardholder_photo`
Retrieve a cardholder's photo.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_photo_name_** `str`  
Name of the photo file.  
  
**_isRedirectCgi_** `bool`  
Whether to redirect to CGI for the photo (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Photo data or error details.  

</div>



---


### `get_log_count`
Get the count of logs with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_filterType_** `int`  
Type of filter to apply.  
  
**_filterEventSource_** `Any`  
Event source filter.  
  
**_filterSource_** `int`  
Source filter.  
  
**_filterEventSourceItem_** `int`  
Event source item filter.  
  
**_filterTimeFrom_** `int`  
Start time for filtering.  
  
**_filterTimeTo_** `int`  
End time for filtering.  
  
**_filterKeyword_** `str`  
Keyword to filter logs.  
  
**_timezoneOffset_** `int`  
Timezone offset.  
  
**_doorIds_** `str`  
Door IDs filter.  
  
**_eventTypes_** `str`  
Event types filter.  
  
**_update_** `int`  
Update flag.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Log count or error details.  

</div>



---


### `get_cardholder_info`
Retrieve cardholder information with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_filterKeyword_** `str`  
Keyword to filter cardholders.  
  
**_filterStatus_** `int`  
Status filter.  
  
**_filterCtrlerId_** `int`  
Controller ID filter.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Cardholder information or error details.  

</div>



---


### `retrieve_last_access_credential`
Retrieve the last access credential for a controller.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ctrlerId_** `int`  
Controller ID.  
  
**_idPtId_** `int`  
ID/point ID (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Last access credential information or error details.  

</div>



---


### `enable_disable_controller`
Enable or disable controllers.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_blEnable_** `bool`  
Whether to enable (True) or disable (False) controllers.  
  
**_arrayJson_** `str`  
JSON array of controller IDs.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the operation or error details.  

</div>



---


### `acknowledge_all_alarm_level_log`
Acknowledge all alarm level logs with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_filterEventSource_** `Any`  
Event source filter.  
  
**_filterSource_** `int`  
Source filter.  
  
**_filterEventSourceItem_** `str`  
Event source item filter.  
  
**_filterTimeFrom_** `int`  
Start time for filtering.  
  
**_filterKeyword_** `str`  
Keyword to filter logs.  
  
**_doorIds_** `str`  
Door IDs filter.  
  
**_eventTypes_** `str`  
Event types filter.  
  
**_update_** `int`  
Update flag.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the acknowledge operation or error details.  

</div>



---


### `modify_controller_logger_config`
Modify the logger configuration for a controller.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_data_** `Any`  
Logger configuration data (see example in docstring).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `save_controller_settings`
Save controller settings for Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_arrayJson_** `str`  
JSON string representing controller settings. Example:
\[\{"enable": true, "id": 97, "name": "ctrler1", "host": "10.13.12.173", "port": 80,
  "model": "A1001", "username": "root", "password": "Q__Q-__-", "time_server":
  "SurveillanceStation", "time_zone": "Fiji", "door": \[\{"id": 231, "name": "FrontDoor",
  "enable_cam": true, "cam_ds_id": 0, "cam_id": 13\}\]\}\]  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `download_filtered_logs`
Download filtered logs from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_filterType_** `int`  
Type of filter to apply.  
  
**_filterEventSource_** `int`  
Event source filter.  
  
**_filterSource_** `int`  
Source filter.  
  
**_filterEventSourceItem_** `str`  
Event source item filter.  
  
**_filterTimeFrom_** `int`  
Start time for filtering.  
  
**_filterTimeTo_** `int`  
End time for filtering.  
  
**_filterKeyword_** `str`  
Keyword to filter logs.  
  
**_doorIds_** `str`  
Door IDs filter.  
  
**_eventTypes_** `str`  
Event types filter.  
  
**_update_** `int`  
Update flag.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Downloaded log data or error details.  

</div>



---


### `get_door_name_from_controller`
Retrieve door names from a specific controller.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ctrlerId_** `int`  
Controller ID.  
  
**_ip_** `str`  
Controller IP address.  
  
**_port_** `int`  
Controller port.  
  
**_userName_** `str`  
Username for authentication.  
  
**_password_** `int`  
Password for authentication (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Door names or error details.  

</div>



---


### `test_connection_and_authentication`
Test connection and authentication to a controller.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ctrlerId_** `int`  
Controller ID.  
  
**_ip_** `str`  
Controller IP address.  
  
**_port_** `int`  
Controller port.  
  
**_userName_** `str`  
Username for authentication.  
  
**_password_** `int`  
Password for authentication (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the test or error details.  

</div>



---


### `enumerate_controller_list_info`
Enumerate controller list information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_update_** `int`  
Update flag.  
  
**_blIncludeRecCnt_** `bool`  
Whether to include record count.  
  
**_blIncludeAuInfo_** `bool`  
Whether to include additional info (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Controller list information or error details.  

</div>



---


### `save_cardholder_setting`
Save cardholder settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_arrayJson_** `str`  
JSON string representing cardholder settings.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `enumerate_door_info`
Enumerate door information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_DoorIds_** `str`  
Comma-separated list of door IDs.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Door information or error details.  

</div>



---


### `clear_logs_surveillance_station`
Clear logs in Surveillance Station with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterType_** `int`  
Type of filter to apply.  
  
**_filterEventSource_** `Any`  
Event source filter.  
  
**_filterSource_** `int`  
Source filter.  
  
**_filterEventSourceItem_** `str`  
Event source item filter.  
  
**_filterTimeFrom_** `int`  
Start time for filtering.  
  
**_filterTimeTo_** `int`  
End time for filtering.  
  
**_filterKeyword_** `str`  
Keyword to filter logs.  
  
**_doorIds_** `str`  
Door IDs filter.  
  
**_eventTypes_** `str`  
Event types filter.  
  
**_update_** `int`  
Update flag.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the clear operation or error details.  

</div>



---


### `list_all_user_privilege`
List all user privileges in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of user privileges or error details.  

</div>



---


### `manual_lock_operation`
Perform a manual lock or unlock operation on a door.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_doorId_** `int`  
Door ID to operate on.  
  
**_operation_** `int`  
Operation code (to check).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the operation or error details.  

</div>



---


### `save_user_door_priv_setting`
Save user door privilege settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_arrayJson_** `str`  
JSON string representing user door privilege settings.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `list_all_logs`
List all logs in Surveillance Station with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_filterType_** `int`  
Type of filter to apply.  
  
**_filterEventSource_** `Any`  
Event source filter.  
  
**_filterSource_** `int`  
Source filter.  
  
**_filterEventSourceItem_** `str`  
Event source item filter.  
  
**_filterTimeFrom_** `int`  
Start time for filtering.  
  
**_filterTimeTo_** `int`  
End time for filtering.  
  
**_filterKeyword_** `str`  
Keyword to filter logs.  
  
**_timezoneOffset_** `int`  
Timezone offset.  
  
**_doorIds_** `str`  
Door IDs filter.  
  
**_eventTypes_** `str`  
Event types filter.  
  
**_update_** `int`  
Update flag.  
  
**_blIncludeRecCnt_** `bool`  
Whether to include record count.  
  
**_blIncludeAuInfo_** `bool`  
Whether to include additional info.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of logs or error details.  

</div>



---


### `delete_selected_controller`
Delete selected controllers from Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated string of controller IDs to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `retrieve_data_from_controller`
Retrieve data from a specific controller.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ctrlerId_** `str`  
ID of the controller to retrieve data from.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Retrieved data or error details.  

</div>



---


### `block_cardholder`
Block cardholders in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_arrayJson_** `str`  
JSON string representing cardholder(s) to block.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the block operation or error details.  

</div>



---


### `get_controller_count`
Get the count of controllers by category.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Controller count or error details.  

</div>



---


### `start_controller_search`
Start searching for controllers.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the search operation or error details.  

</div>



---


### `get_controller_search_info`
Get information about the current controller search.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AxisAcsCtrler.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
Process ID of the search.  
  
**_offset_** `int`  
Offset for paginated results.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Search information or error details.  

</div>



---


### `enumerate_digital_output`
Enumerate digital output devices.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.DigitalOutput` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
Camera ID to filter digital outputs.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of digital outputs or error details.  

</div>



---


### `save_digital_output_parameters`
Save parameters for a digital output device.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.DigitalOutput` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
Camera ID.  
  
**_idx_** `int`  
Index of the digital output.  
  
**_keep_setting_** `bool`  
Whether to keep the current setting.  
  
**_normal_state_** `int`  
Normal state value.  
  
**_trigger_state_** `bool`  
Trigger state value.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `long_polling_digital_output_status`
Perform long polling to get the status of a digital output.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.DigitalOutput` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `int`  
Camera ID.  
  
**_idx_** `int`  
Index of the digital output.  
  
**_keep_** `bool`  
Whether to keep polling.  
  
**_setNormalCap_** `bool`  
Set normal capability.  
  
**_normal_** `int`  
Normal state value.  
  
**_trigger_** `bool`  
Trigger state value.  
  
**_timeOut_** `int`  
Timeout for polling.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Status information or error details.  

</div>



---


### `trigger_external_event`
Trigger an external event in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.ExternalEvent` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventId_** `int`  
ID of the event to trigger.  
  
**_eventName_** `str`  
Name of the event to trigger.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the trigger operation or error details.  

</div>



---


### `get_list_io_modules`
Get a list of I/O modules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_blFromList_** `bool`  
Whether to get from list.  
  
**_ownerDsId_** `int`  
Owner device station ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of I/O modules or error details.  

</div>



---


### `get_io_port_list`
Get a list of I/O ports for a module.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_Id_** `int`  
Module ID.  
  
**_Port_** `int`  
Port number.  
  
**_IP_** `str`  
IP address.  
  
**_User_** `str`  
Username.  
  
**_Pass_** `str`  
Password.  
  
**_Vendor_** `str`  
Vendor name.  
  
**_Model_** `str`  
Model name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of I/O ports or error details.  

</div>



---


### `get_supported_list_io_modules`
Get a list of supported I/O module vendor models.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of supported vendor models or error details.  

</div>



---


### `save_setting_io_module`
Save or update the settings for an I/O module in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Name of the I/O module.  
  
**_id_** `int`  
ID of the I/O module.  
  
**_ownerDsId_** `int`  
Owner device station ID.  
  
**_vendor_** `str`  
Vendor name of the I/O module.  
  
**_model_** `str`  
Model name of the I/O module.  
  
**_ip_** `str`  
IP address of the I/O module.  
  
**_port_** `int`  
Port number for the I/O module.  
  
**_userName_** `str`  
Username for authentication.  
  
**_enabled_** `bool`  
Whether the I/O module is enabled.  
  
**_status_** `int`  
Status code of the I/O module.  
  
**_timeServer_** `str`  
Time server address.  
  
**_passWord_** `str`  
Password for authentication.  
  
**_ntpEnable_** `bool`  
Whether NTP is enabled.  
  
**_DIOdata_** `Any`  
Digital I/O data (structure to be checked).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the save operation or error details.  

</div>



---


### `enable_io_modules`
Enable specified I/O modules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_iomlist_** `str`  
Comma-separated list of I/O module IDs to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the enable operation or error details.  

</div>



---


### `disable_io_modules`
Disable specified I/O modules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_iomlist_** `str`  
Comma-separated list of I/O module IDs to disable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the disable operation or error details.  

</div>



---


### `delete_io_modules`
Delete specified I/O modules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_iomlist_** `str`  
Comma-separated list of I/O module IDs to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `test_connection_to_io_module`
Test the connection to a specified I/O module.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the I/O module.  
  
**_port_** `str`  
Port number for the I/O module.  
  
**_ip_** `str`  
IP address of the I/O module.  
  
**_userName_** `str`  
Username for authentication.  
  
**_passWord_** `str`  
Password for authentication.  
  
**_model_** `str`  
Model name of the I/O module.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the connection test or error details.  

</div>



---


### `get_capability_io_module`
Get the capability information for a specified I/O module.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_vendor_** `str`  
Vendor name of the I/O module.  
  
**_model_** `str`  
Model name of the I/O module.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Capability information or error details.  

</div>



---


### `configure_io_port_setting`
Configure the port settings for a specified I/O module.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the I/O module.  
  
**_DIOdata_** `Any`  
Digital I/O data for port configuration (structure to be checked).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the configuration or error details.  

</div>



---


### `poll_trigger_state_io_module`
Poll the trigger state of digital input (DI) ports for a specified I/O module.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_Id_** `int`  
ID of the I/O module.  
  
**_list_** `Any`  
List of DI ports to poll (structure to be checked).  
  
**_timeOut_** `int`  
Timeout for polling operation.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Polling result or error details.  

</div>



---


### `poll_do_trigger_module`
Poll the trigger state of digital output (DO) ports for a specified I/O module.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the I/O module.  
  
**_idx_** `int`  
Index of the DO port.  
  
**_normal_** `int`  
Normal state value.  
  
**_trigger_** `bool`  
Trigger state.  
  
**_timeOut_** `int`  
Timeout for polling operation.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Polling result or error details.  

</div>



---


### `get_number_of_devices`
Get the number of I/O devices for each device station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Number of devices or error details.  

</div>



---


### `get_category_count_io_module`
Get the count of I/O modules by category.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_ownerDsId_** `int`  
Owner device station ID.  
  
**_blFromList_** `bool`  
Whether to get count from a list (to be checked).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Count by category or error details.  

</div>



---


### `start_search_io_module`
Start searching for I/O modules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the search operation or error details.  

</div>



---


### `get_search_io_module_info`
Get information about the current I/O module search.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IOModule.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
Process ID of the search.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Search information or error details.  

</div>



---


### `get_current_camera_status`
Get the current status of specified cameras.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Status` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_list_** `str`  
Comma-separated list of camera IDs.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Camera status information or error details.  

</div>



---


### `enum_preset_camera_list`
Enumerate the list of presets for a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Preset` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
ID of the camera.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of camera presets or error details.  

</div>



---


### `get_preset_camera_capability`
Get the capability information for camera presets.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Preset` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `int`  
ID of the camera.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Preset capability information or error details.  

</div>



---


### `record_current_camera_position`
Record the current position of a camera as a preset.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Preset` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `int`  
ID of the camera.  
  
**_position_** `int`  
Preset position index.  
  
**_speed_** `int`  
Speed for moving to the preset.  
  
**_name_** `str`  
Name for the preset.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the record operation or error details.  

</div>



---


### `delete_list_preset_camera`
Delete specified presets from a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Preset` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
ID of the camera.  
  
**_position_** `str`  
Preset position(s) to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `go_specific_preset_by_given_speed`
Move a camera to a specific preset position at a given speed.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Preset` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
ID of the camera.  
  
**_position_** `int`  
Preset position index.  
  
**_speed_** `int`  
Speed for moving to the preset.  
  
**_type_** `int`  
Type of preset move (to be checked).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the move operation or error details.  

</div>



---


### `set_current_camera_position`
Set the current position of a camera as the home position.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Preset` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cameraId_** `Any`  
ID of the camera.  
  
**_bindPosition_** `int`  
Position to bind as home.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error details.  

</div>



---


### `enum_patrol_list`
Enumerate the list of patrols for a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cam_** `Any`  
Camera identifier.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of patrols or error details.  

</div>



---


### `enum_patrol_name_list`
Enumerate the list of patrol names for a specified camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
Camera identifier.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of patrol names or error details.  

</div>



---


### `load_patrol_detail`
Load the details of a specific patrol.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Patrol ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Patrol details or error information.  

</div>



---


### `add_or_modify_patrol`
Add or modify a patrol for a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
Camera identifier.  
  
**_id_** `int`  
Patrol ID.  
  
**_stayTime_** `int`  
Stay time at each preset.  
  
**_speed_** `int`  
Patrol speed.  
  
**_name_** `str`  
Name of the patrol.  
  
**_presetList_** `Any`  
List of presets for the patrol (structure to be checked).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the add/modify operation or error details.  

</div>



---


### `delete_specific_patrol`
Delete a specific patrol from a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
Camera identifier.  
  
**_patrolId_** `str`  
Patrol ID to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `run_patrol`
Run a specified patrol on a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
Camera identifier.  
  
**_id_** `int`  
Patrol ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the run operation or error details.  

</div>



---


### `stop_patrol`
Stop the currently running patrol on a camera.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.PTZ.Patrol` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camId_** `Any`  
Camera identifier.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the stop operation or error details.  

</div>



---


### `start_camera_search_process`
Start searching for cameras.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the search operation or error details.  

</div>



---


### `get_camera_search_info`
Get information about the current camera search.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
Process ID of the search.  
  
**_offset_** `int`  
Offset for pagination.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Search information or error details.  

</div>



---


### `toggle_home_mode`
Toggle the Home Mode in Surveillance Station.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.HomeMode` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_on_** `bool`  
Whether to enable (True) or disable (False) Home Mode.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the toggle operation or error details.  

</div>



---


### `get_home_mode_settings`
Get the current Home Mode settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.HomeMode` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_need_mobiles_** `bool`  
Whether to include mobile device information.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Home Mode settings or error details.  

</div>



---


### `get_transaction_list`
Get a list of device transactions with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Device` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterIds_** `str`  
Comma-separated list of transaction IDs to filter.  
  
**_filterDsIds_** `str`  
Comma-separated list of device station IDs to filter.  
  
**_filterEnable_** `bool`  
Filter by enabled status.  
  
**_filterStatus_** `int`  
Filter by status code.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of transactions or error details.  

</div>



---


### `get_all_transaction_list`
Get a list of all transactions with optional filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterIds_** `str`  
Comma-separated list of transaction IDs to filter.  
  
**_dsId_** `int`  
Device station ID.  
  
**_filterTimeFrom_** `Any`  
Start time for filtering.  
  
**_filterStatus_** `int`  
Filter by status code.  
  
**_filterLock_** `bool`  
Filter by lock status.  
  
**_filterTimeTo_** `Any`  
End time for filtering.  
  
**_filterTimeRangeIntersect_** `bool`  
Whether to intersect time ranges.  
  
**_filterKeyword_** `str`  
Keyword for filtering.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of transactions or error details.  

</div>



---


### `lock_history_records`
Lock specified history records.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterIds_** `str`  
Comma-separated list of record IDs to lock.  
  
**_dsId_** `int`  
Device station ID.  
  
**_filterStatus_** `int`  
Filter by status code.  
  
**_filterLock_** `bool`  
Filter by lock status.  
  
**_filterTimeFrom_** `Any`  
Start time for filtering.  
  
**_filterTimeTo_** `Any`  
End time for filtering.  
  
**_filterTimeRangeIntersect_** `bool`  
Whether to intersect time ranges.  
  
**_filterKeyword_** `str`  
Keyword for filtering.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the lock operation or error details.  

</div>



---


### `unlock_history_records`
Unlock specified history records.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterIds_** `str`  
Comma-separated list of record IDs to unlock.  
  
**_dsId_** `int`  
Device station ID.  
  
**_filterStatus_** `int`  
Filter by status code.  
  
**_filterLock_** `bool`  
Filter by lock status.  
  
**_filterTimeFrom_** `Any`  
Start time for filtering.  
  
**_filterTimeTo_** `Any`  
End time for filtering.  
  
**_filterTimeRangeIntersect_** `bool`  
Whether to intersect time ranges.  
  
**_filterKeyword_** `str`  
Keyword for filtering.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the unlock operation or error details.  

</div>



---


### `delete_history_records`
Delete specified history records.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filterIds_** `str`  
Comma-separated list of record IDs to delete.  
  
**_dsId_** `int`  
Device station ID.  
  
**_filterStatus_** `int`  
Filter by status code.  
  
**_filterLock_** `bool`  
Filter by lock status.  
  
**_filterTimeFrom_** `Any`  
Start time for filtering.  
  
**_filterTimeTo_** `Any`  
End time for filtering.  
  
**_filterTimeRangeIntersect_** `bool`  
Whether to intersect time ranges.  
  
**_filterKeyword_** `str`  
Keyword for filtering.  
  
**_start_** `int`  
Start index for pagination.  
  
**_limit_** `int`  
Maximum number of results to return.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error details.  

</div>



---


### `start_session_with_specified_session_id`
Start a session with a specified session ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_device_name_** `str`  
Name of the device.  
  
**_session_id_** `str`  
Session ID to start.  
  
**_timeout_** `int`  
Timeout for the session.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the start operation or error details.  

</div>



---


### `complete_session_with_specified_id`
Complete a session with a specified session ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_device_name_** `str`  
Name of the device.  
  
**_session_id_** `str`  
Session ID to complete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the complete operation or error details.  

</div>



---


### `cancel_session_with_specified_session_id`
Cancel a session with a specified session ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_device_name_** `str`  
Name of the device.  
  
**_session_id_** `str`  
Session ID to cancel.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the cancel operation or error details.  

</div>



---


### `carry_data_into_session_id`
Append data to a session with a specified session ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Transactions.Transaction` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_device_name_** `str`  
Name of the device.  
  
**_session_id_** `str`  
Session ID to append data to.  
  
**_content_** `str`  
Data content to append.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the append operation or error details.  

</div>



---


### `add_edit_active_vault_task`
Add or edit an active vault task for archiving.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_blCustomFolder_** `bool`  
Whether to use a custom folder for storage.  
  
**_blLimitBySize_** `bool`  
Whether to limit the archive by size.  
  
**_blRotateFile_** `bool`  
Whether to enable file rotation.  
  
**_blSrcRecNoOverlap_** `bool`  
Whether to avoid overlapping source recordings.  
  
**_blUseRecDet_** `bool`  
Whether to use recording detection.  
  
**_camId_** `Any`  
Camera ID.  
  
**_camInfo_** `Any`  
Camera information.  
  
**_dayLimit_** `int`  
Day limit for the archive.  
  
**_didCode_** `str`  
Device code.  
  
**_dsSerial_** `str`  
Device serial number.  
  
**_execTime_** `Any`  
Execution time.  
  
**_hostname_** `str`  
Hostname of the source server.  
  
**_id_** `int`  
Task ID (for editing).  
  
**_name_** `str`  
Name of the task.  
  
**_passwd_** `str`  
Password for authentication.  
  
**_port_** `str`  
Port number.  
  
**_recEndTm_** `Any`  
Recording end time.  
  
**_recMode_** `str`  
Recording mode.  
  
**_recSchedule_** `str`  
Recording schedule.  
  
**_recStartTm_** `Any`  
Recording start time.  
  
**_schedule_** `str`  
Task schedule.  
  
**_storagePath_** `str`  
Path for storage.  
  
**_type_** `int`  
Type of the task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `login_source_server_get_info`
Log in to the source server and retrieve information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_port_** `str`  
Port number of the source server.  
  
**_hostname_** `str`  
Hostname of the source server.  
  
**_protocol_** `bool`  
Protocol to use (e.g., HTTPS).  
  
**_username_** `str`  
Username for authentication.  
  
**_passwd_** `str`  
Password for authentication.  
  
**_archId_** `int`  
Archive ID.  
  
**_didCode_** `str`  
Device code.  
  
**_srcDsId_** `int`  
Source device ID (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `delete_archive_vault_task`
Delete an archive vault task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Task ID to delete.  
  
**_keepRec_** `bool`  
Whether to keep the recordings.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `list_exist_archive_vault`
List all existing archive vault tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `enable_archive_vault_task`
Enable an archive vault task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Task ID to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `disable_archive_vault_task`
Disable an archive vault task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Task ID to disable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `disable_archive_vault_batchedit_task`
Batch edit (disable) archive vault tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskIds_** `str`  
Comma-separated list of task IDs.  
  
**_attrs_** `Any`  
Additional attributes for batch edit (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_batch_edit_progress`
Get the progress of a batch edit operation.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
Process ID of the batch edit operation (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_batchedit_proress_info`
Get detailed information about batch edit progress.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
Process ID of the batch edit operation (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `clean_batchedit_progress_data`
Clean up batch edit progress data.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Archiving.Pull` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
Process ID of the batch edit operation.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_youtube_live_broadcast_setting`
Get the current YouTube Live broadcast settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.YoutubeLive` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `set_youtube_live_broadcast_info`
Set YouTube Live broadcast information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.YoutubeLive` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_rtmp_path_** `str`  
RTMP path for the broadcast.  
  
**_key_** `str`  
Stream key.  
  
**_cam_id_** `int`  
Camera ID.  
  
**_stream_profile_** `int`  
Stream profile.  
  
**_live_on_** `bool`  
Whether to enable live broadcast.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `close_youtube_live_broadcast`
Close the current YouTube Live broadcast.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.YoutubeLive` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_deep_video_analytic`
Get the list of deep video analytic tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `create_edit_DVA_task`
Create or edit a Deep Video Analytics (DVA) task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_analyze_type_** `int`  
Type of analysis to perform.  
  
**_actFromHost_** `bool`  
Whether the action is triggered from the host.  
  
**_name_** `str`  
Name of the DVA task.  
  
**_camera_id_** `int`  
ID of the camera associated with the task.  
  
**_enable_** `bool`  
Whether to enable the task.  
  
**_enable_recording_** `bool`  
Whether to enable recording for the task.  
  
**_pre_rec_time_** `int`  
Pre-recording time in seconds.  
  
**_post_rec_time_** `int`  
Post-recording time in seconds.  
  
**_event_integration_** `int`  
Event integration setting.  
  
**_region_type_** `int`  
Type of detection region.  
  
**_det_region_cnt_** `int`  
Number of detection regions.  
  
**_det_region_** `int`  
Detection region configuration.  
  
**_people_mode_** `int`  
People counting mode.  
  
**_reset_cnt_frequency_** `int`  
Frequency for resetting the counter.  
  
**_reset_weekday_** `int`  
Weekday for counter reset.  
  
**_reset_date_** `int`  
Date for counter reset.  
  
**_reset_time_minute_** `int`  
Minute for counter reset.  
  
**_reset_time_hour_** `int`  
Hour for counter reset.  
  
**_fence_dir_flag_** `int`  
Fence direction flag.  
  
**_people_display_pos_** `int`  
Display position for people counting.  
  
**_stream_profile_** `int`  
Stream profile to use.  
  
**_people_enable_stay_max_** `bool`  
Whether to enable maximum stay for people.  
  
**_intrusion_detect_target_** `int`  
Target for intrusion detection.  
  
**_min_obj_size_** `Any`  
Minimum object size for detection.  
  
**_min_obj_size_option_** `int`  
Option for minimum object size.  
  
**_enable_min_duration_** `int`  
Enable minimum duration for detection.  
  
**_people_display_info_** `int`  
Display information for people counting.  
  
**_people_enter_** `int`  
Number of people entering.  
  
**_people_stay_max_** `int`  
Maximum number of people staying.  
  
**_people_region_** `str`  
Region for people counting.  
  
**_people_hint_pos_** `str`  
Hint position for people counting.  
  
**_blEditMode_** `bool`  
Edit mode flag (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `delete_dva_task`
Delete a Deep Video Analytics (DVA) task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of DVA task IDs to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `enable_dva_task`
Enable one or more Deep Video Analytics (DVA) tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of DVA task IDs to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `disable_dva_task`
Disable one or more Deep Video Analytics (DVA) tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of DVA task IDs to disable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `reset_counter_people_counting_task`
Reset the people counting counter for a specific DVA task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskId_** `str`  
ID of the people counting task to reset.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_people_enter_leave_count`
Get the count of people entering and leaving for specified DVA tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Report` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of DVA task IDs.  
  
**_timeStart_** `str`  
Start time for the count (ISO format or timestamp).  
  
**_timeEnd_** `str`  
End time for the count (ISO format or timestamp).  
  
**_timezone_** `int`  
Timezone offset.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_people_count_of_day`
Get the people count report for a specific day.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Report` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of DVA task IDs.  
  
**_interval_** `int`  
Interval for the report.  
  
**_intervalUnit_** `int`  
Unit for the interval.  
  
**_timezone_** `int`  
Timezone offset.  
  
**_timestamp_** `int`  
Timestamp for the report.  
  
**_blOccupancy_** `int`  
Occupancy flag (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `list_people_counting_task`
List people counting tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskList_** `str`  
Comma-separated list of task IDs to list.  
  
**_limit_** `int`  
Limit the number of tasks returned (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `delete_recording_file_of_detection`
Delete recording files associated with detection events.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_slaveDsParam_** `str`  
Parameters for the slave device.  
  
**_deleteMethod_** `int`  
Method for deletion (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_info_of_task_and_frame`
Get analytic result information for a specific task and frame.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_eventId_** `int`  
Event ID to query.  
  
**_taskId_** `int`  
Task ID to query.  
  
**_blAlertEvt_** `bool`  
Alert event flag (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `lock_recording_file_of_detection`
Lock recording files associated with detection events.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
Device server ID.  
  
**_idList_** `int`  
List of recording file IDs to lock (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `unlock_recording_file_of_detection`
Unlock recording files associated with detection events.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.Recording` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dsId_** `int`  
Device server ID.  
  
**_idList_** `str`  
List of recording file IDs to unlock (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_info_people_counting_task`
Get information about people counting tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `create_people_counting_task`
Create a new people counting task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_** `bool`  
Whether to enable the task.  
  
**_task_ids_** `str`  
Comma-separated list of task IDs.  
  
**_owner_ds_id_** `int`  
Owner device server ID.  
  
**_name_** `str`  
Name of the task.  
  
**_people_display_info_** `str`  
Display information for people counting.  
  
**_people_enable_stay_max_** `int`  
Enable maximum stay for people.  
  
**_reset_cnt_frequency_** `int`  
Frequency for resetting the counter.  
  
**_resert_date_** `int`  
Date for counter reset.  
  
**_resert_weekday_** `int`  
Weekday for counter reset.  
  
**_resert_tome_hour_** `int`  
Hour for counter reset.  
  
**_resert_tome_minute_** `int`  
Minute for counter reset (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `modify_setting_of_people_counting_task`
Modify the settings of an existing people counting task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_** `bool`  
Whether to enable the task.  
  
**_id_** `int`  
ID of the task to modify.  
  
**_task_ids_** `str`  
Comma-separated list of task IDs.  
  
**_name_** `str`  
Name of the task.  
  
**_people_display_info_** `int`  
Display information for people counting.  
  
**_people_enable_max_** `int`  
Enable maximum stay for people.  
  
**_reset_cnt_frequency_** `int`  
Frequency for resetting the counter.  
  
**_resert_date_** `int`  
Date for counter reset.  
  
**_resert_weekday_** `int`  
Weekday for counter reset.  
  
**_resert_tome_hour_** `int`  
Hour for counter reset.  
  
**_resert_tome_minute_** `int`  
Minute for counter reset (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `delete_task_group`
Delete a people counting task group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task group IDs to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `start_count_people_task_in_groups`
Enable people counting tasks in specified groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task group IDs to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `stop_count_people_task_in_groups`
Disable people counting tasks in specified groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task group IDs to disable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_number_counting_task_group`
Get the people count for a specific task group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the task group.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `lock_recording_file_result`
Reset the people count for a specific IVA task group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.IVA.TaskGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the IVA task group.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_face_list_task`
Retrieve the list of face detection tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task IDs to filter.  
  
**_ownerDsId_** `int`  
ID of the owner DiskStation.  
  
**_blOnlyEnableDs_** `bool`  
Whether to include only enabled DiskStations.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `create_or_edit_task`
Create or edit a face detection task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Task ID.  
  
**_id_on_rec_server_** `int`  
Task ID on the recording server.  
  
**_camera_id_** `int`  
Camera ID.  
  
**_camera_id_on_rec_** `int`  
Camera ID on the recording server.  
  
**_owner_ds_id_** `int`  
Owner DiskStation ID.  
  
**_enable_** `bool`  
Whether to enable the task.  
  
**_blEditMode_** `bool`  
Edit mode flag.  
  
**_stream_profile_** `int`  
Stream profile index.  
  
**_name_** `str`  
Name of the task.  
  
**_similarity_** `float`  
Similarity threshold for face recognition.  
  
**_allowed_color_** `int`  
Color code for allowed faces.  
  
**_allowed_list_** `Any`  
List of allowed faces.  
  
**_blocked_color_** `int`  
Color code for blocked faces.  
  
**_blocked_list_** `Any`  
List of blocked faces.  
  
**_vip_color_** `int`  
Color code for VIP faces.  
  
**_vip_list_** `Any`  
List of VIP faces.  
  
**_recognized_color_** `int`  
Color code for recognized faces.  
  
**_unrecognized_color_** `int`  
Color code for unrecognized faces.  
  
**_deleted_** `bool`  
Whether the task is deleted.  
  
**_det_region_** `str`  
Detection region.  
  
**_det_region_cnt_** `int`  
Number of detection regions.  
  
**_region_type_** `int`  
Type of region.  
  
**_display_info_** `int`  
Display information.  
  
**_display_type_** `int`  
Display type.  
  
**_frame_display_info_** `int`  
Frame display information.  
  
**_enable_min_ogj_size_** `bool`  
Enable minimum object size.  
  
**_min_ogj_size_** `float`  
Minimum object size.  
  
**_post_rec_time_** `int`  
Post-recording time in seconds.  
  
**_pre_rec_time_** `int`  
Pre-recording time in seconds.  
  
**_schedule_** `str`  
Task schedule.  
  
**_scheduleOn_** `bool`  
Whether the schedule is enabled.  
  
**_ignore_bad_quality_** `bool`  
Ignore bad quality flag (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `delete_face_task`
Delete one or more face detection tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task IDs to delete.  
  
**_keepRecording_** `bool`  
Whether to keep the associated recordings (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `enable_task_to_start_detection_recording`
Enable face detection tasks to start detection and recording.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task IDs to enable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `disable_task_to_stop_detection_recording`
Disable face detection tasks to stop detection and recording.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of task IDs to disable.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `list_task_with_privilege_to_watch`
List face detection tasks with privilege to watch.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `int`  
Task group ID to filter.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `create_face_group`
Create a new face group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Name of the face group.  
  
**_description_** `str`  
Description of the face group.  
  
**_update_registered_face_** `Any`  
Registered face update information (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `disable_face_grooup`
Delete (disable) one or more face groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `Any`  
IDs of the face groups to delete (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `edit_face_group`
Edit an existing face group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Name of the face group.  
  
**_description_** `str`  
Description of the face group.  
  
**_update_registered_face_** `Any`  
Registered face update information.  
  
**_id_** `int`  
ID of the face group to edit.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_face_group_list`
Retrieve the list of face groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_only_** `bool`  
Whether to return only IDs.  
  
**_filter_** `Any`  
Filter criteria (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `count_face_groups`
Count the number of face groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_** `Any`  
Filter criteria (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `detect_faces_image`
Detect faces in an image.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_image_data_** `str`  
Base64-encoded image data.  
  
**_image_size_** `int`  
Size of the image (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `create_registered_face`
Create a new registered face.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_account_** `str`  
Account associated with the face.  
  
**_name_** `str`  
Name of the person.  
  
**_description_** `str`  
Description of the face.  
  
**_image_data_** `str`  
Base64-encoded image data.  
  
**_image_size_** `int`  
Size of the image.  
  
**_face_** `Any`  
Face data.  
  
**_update_face_group_** `Any`  
Face group update information.  
  
**_captured_face_id_** `int`  
ID of the captured face.  
  
**_update_unrecognized_captured_face_** `bool`  
Whether to update unrecognized captured face.  
  
**_append_image_data_** `bool`  
Append image data flag (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `delete_registered_face`
Delete one or more registered faces.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `Any`  
IDs of the registered faces to delete (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `edit_registered_face`
Edit an existing registered face.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the registered face.  
  
**_account_** `str`  
Account associated with the face.  
  
**_name_** `str`  
Name of the person.  
  
**_description_** `str`  
Description of the face.  
  
**_image_data_** `str`  
Base64-encoded image data.  
  
**_image_size_** `int`  
Size of the image.  
  
**_face_** `Any`  
Face data.  
  
**_update_face_group_** `Any`  
Face group update information.  
  
**_captured_face_id_** `int`  
ID of the captured face.  
  
**_update_unrecognized_captured_face_** `bool`  
Whether to update unrecognized captured face.  
  
**_append_image_data_** `bool`  
Append image data flag.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `list_registered_face`
List registered faces.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_only_** `bool`  
Whether to return only IDs.  
  
**_filter_** `Any`  
Filter criteria.  
  
**_append_image_data_** `bool`  
Whether to append image data (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `count_registered_face`
Count the number of registered faces.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_** `Any`  
Filter criteria (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `search_registered_face`
Search for registered faces by keywords.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_keywords_** `str`  
Search keywords.  
  
**_append_image_data_** `bool`  
Whether to append image data (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response from the request.  

</div>



---


### `get_face_result_list`
Retrieve a list of face recognition results.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_** `Any`  
Filter criteria for the face results.  
  
**_blIncludeSnapshot_** `bool`  
Whether to include snapshot images in the results.  
  
**_blIncludeRegisteredFace_** `bool`  
Whether to include registered face information.  
  
**_limit_** `int`  
Maximum number of results to return.  
  
**_slaveDsParam_** `int`  
Additional parameter for slave DiskStation (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response containing the list of face recognition results.  

</div>



---


### `delete_face_result`
Delete face recognition results.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_** `Any`  
Filter criteria for selecting face results to delete.  
  
**_slaveDsParam_** `Any`  
Additional parameter for slave DiskStation (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the delete operation.  

</div>



---


### `lock_face_result`
Lock face recognition results to prevent modification or deletion.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_** `Any`  
Filter criteria for selecting face results to lock.  
  
**_slaveDsParam_** `Any`  
Additional parameter for slave DiskStation (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the lock operation.  

</div>



---


### `unlock_face_result`
Unlock face recognition results to allow modification or deletion.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_** `Any`  
Filter criteria for selecting face results to unlock.  
  
**_slaveDsParam_** `Any`  
Additional parameter for slave DiskStation (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the unlock operation.  

</div>



---


### `get_recording_file_of_face_info`
Retrieve the recording file associated with a specific captured face.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_capturedFaceId_** `int`  
ID of the captured face (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response containing the recording file information.  

</div>



---


### `get_recognition_face_information`
Retrieve analytic results for face recognition events.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskId_** `int`  
ID of the face recognition task.  
  
**_eventId_** `int`  
ID of the event.  
  
**_startTime_** `int`  
Start time for the query (timestamp).  
  
**_endTime_** `int`  
End time for the query (timestamp).  
  
**_blIncludeRegisteredFace_** `int`  
Whether to include registered face information (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response containing analytic results.  

</div>



---


### `correct_face_result`
Correct the result of a face recognition event by associating it with a registered face.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the face recognition result to correct.  
  
**_registered_face_id_** `int`  
ID of the registered face to associate (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the correction.  

</div>



---


### `mark_face_result_as_stranger`
Mark one or more face recognition results as strangers.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Face.Result` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str`  
Comma-separated list of face result IDs to mark as strangers (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the operation.  

</div>



---


### `add_new_bookmark`
Add a new bookmark to a recording.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Bookmark` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
ID of the bookmark.  
  
**_eventId_** `int`  
ID of the associated event.  
  
**_cameraId_** `int`  
ID of the camera.  
  
**_archId_** `int`  
ID of the archive.  
  
**_name_** `str`  
Name of the bookmark.  
  
**_timestamp_** `Any`  
Timestamp for the bookmark.  
  
**_comment_** `str`  
Comment for the bookmark.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the add operation.  

</div>



---


### `delete_bookmark`
Delete one or more bookmarks from recordings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Bookmark` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_bookmarkIds_** `Any`  
IDs of the bookmarks to delete (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response indicating the result of the delete operation.  

</div>



---


### `list_bookmark_detail`
List details of bookmarks for recordings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording.Bookmark` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Maximum number of bookmarks to return.  
  
**_cameraIds_** `str`  
Comma-separated list of camera IDs to filter.  
  
**_fromTime_** `int`  
Start time for filtering bookmarks (timestamp).  
  
**_toTime_** `int`  
End time for filtering bookmarks (not working).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict of str to object or str`  
API response containing bookmark details.  

</div>



---


