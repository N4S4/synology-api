"""Synology Surveillance Station API Wrapper."""
from __future__ import annotations
from typing import Optional, Any
from . import base_api


class SurveillanceStation(base_api.BaseApi):
    """
    API wrapper for Synology Surveillance Station.

    Provides methods to interact with Surveillance Station features such as retrieving
    station information and saving camera configurations.
    """

    def surveillance_station_info(self) -> dict[str, object] | str:
        """
        Retrieve information about the Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing Surveillance Station information, or a string
            with error details if the request fails.
        """
        api_name = 'SYNO.SurveillanceStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        return self.request_data(api_name, api_path, req_param)

    def camera_save(self, id: str = None,
                    name: str = None,
                    dsld: int = None,
                    newName: str = None,
                    ip: str = None,
                    port: int = None,
                    vendor: str = None,
                    model: str = None,
                    userName: str = None,
                    password: str = None,
                    videoCodec: int = None,
                    audioCodec: int = None,
                    tvStandard: int = None,
                    channel: str = None,
                    userDefinePath: str = None,
                    fov: str = None,
                    streamXX: Any = None,
                    recordTime: int = None,
                    preRecordTime: int = None,
                    postRecordTime: int = None,
                    enableRecordingKeepDays: bool = None,
                    recordingKeepDays: int = None,
                    enableRecordingKeepSize: bool = None,
                    recordingKeepSize: int = None,
                    enableLowProfile: bool = None,
                    recordSchedule: list[int] = None,
                    rtspPathTimeout: int = None) -> dict[str, object] | str:
        """
        Save or update camera configuration.

        Parameters
        ----------
        id : str, optional
            Camera ID.
        name : str, optional
            Camera name.
        dsld : int, optional
            Device slot ID.
        newName : str, optional
            New camera name.
        ip : str, optional
            Camera IP address.
        port : int, optional
            Camera port.
        vendor : str, optional
            Camera vendor.
        model : str, optional
            Camera model.
        userName : str, optional
            Username for camera authentication.
        password : str, optional
            Password for camera authentication.
        videoCodec : int, optional
            Video codec type.
        audioCodec : int, optional
            Audio codec type.
        tvStandard : int, optional
            TV standard.
        channel : str, optional
            Channel identifier.
        userDefinePath : str, optional
            User-defined path.
        fov : str, optional
            Field of view.
        streamXX : Any, optional
            Stream configuration.
        recordTime : int, optional
            Recording time.
        preRecordTime : int, optional
            Pre-recording time.
        postRecordTime : int, optional
            Post-recording time.
        enableRecordingKeepDays : bool, optional
            Enable recording retention by days.
        recordingKeepDays : int, optional
            Number of days to keep recordings.
        enableRecordingKeepSize : bool, optional
            Enable recording retention by size.
        recordingKeepSize : int, optional
            Maximum size for recordings.
        enableLowProfile : bool, optional
            Enable low profile recording.
        recordSchedule : list of int, optional
            Recording schedule.
        rtspPathTimeout : int, optional
            RTSP path timeout.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def camera_list(self, idList: str = None,
                    offset: int = None,
                    limit: int = None,
                    blFromCamList: bool = None,
                    blIncludeDeletedCam: bool = None,
                    privCamType: str = None,
                    basic: bool = None,
                    streamInfo: bool = None,
                    blPrivilege: bool = None,
                    camStm: int = None) -> dict[str, object] | str:
        """
        Retrieve a list of cameras from Surveillance Station.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of camera IDs to filter.
        offset : int, optional
            The starting index for the camera list.
        limit : int, optional
            The maximum number of cameras to return.
        blFromCamList : bool, optional
            Whether to retrieve from the camera list.
        blIncludeDeletedCam : bool, optional
            Whether to include deleted cameras.
        privCamType : str, optional
            Filter by camera privilege type.
        basic : bool, optional
            Whether to return only basic information.
        streamInfo : bool, optional
            Whether to include stream information.
        blPrivilege : bool, optional
            Whether to include privilege information.
        camStm : int, optional
            Camera stream type.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing camera list information, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_info(self,
                        cameraIds: int = None,
                        privCamType: int = 1,
                        blIncludeDeletedCam: bool = True,
                        basic: bool = True,
                        streamInfo: bool = True,
                        optimize: bool = True,
                        ptz: bool = True,
                        eventDetection: bool = True,
                        deviceOutCap: bool = True,
                        fisheye: bool = True,
                        camAppInfo: bool = True) -> dict[str, object] | str:
        """
        Return information about a camera.

        Parameters
        ----------
        cameraIds : int, optional
            Camera ID. Although named cameraIds in the API, it refers to a single camera ID.
        privCamType : int, default=1
            Camera privilege type. Possible values:
                1: LIVEVIEW
                2: PLAYBACK
                4: LENS
                8: AUDIO
                16: DIGIOUT
        blIncludeDeletedCam : bool, default=True
            Whether to include deleted cameras.
        basic : bool, default=True
            Whether to return only basic information.
        streamInfo : bool, default=True
            Whether to include stream information.
        optimize : bool, default=True
            Whether to optimize the returned data.
        ptz : bool, default=True
            Whether to include PTZ (Pan-Tilt-Zoom) information.
        eventDetection : bool, default=True
            Whether to include event detection information.
        deviceOutCap : bool, default=True
            Whether to include device output capabilities.
        fisheye : bool, default=True
            Whether to include fisheye camera information.
        camAppInfo : bool, default=True
            Whether to include camera application information.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing camera information, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def camera_list_group(self,
                          offset: int = None,
                          limit: int = None) -> dict[str, object] | str:
        """
        Retrieve a list of camera groups from Surveillance Station.

        Parameters
        ----------
        offset : int, optional
            The starting index for the camera group list.
        limit : int, optional
            The maximum number of camera groups to return.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing camera group information, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_snapshot(self,
                     id: Any = None,
                     name: str = None,
                     dsld: int = None,
                     profileType: int = 1) -> str:
        """
        Retrieve a snapshot image from a camera.

        Parameters
        ----------
        id : Any, optional
            Camera identifier.
        name : str, optional
            Camera name.
        dsld : int, optional
            Device slot ID.
        profileType : int, default=1
            Profile type for the snapshot (1 is the default profile).

        Returns
        -------
        str
            Binary data of the snapshot image. The response is not a JSON object.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val
        # Make sure to disable json response, as the response is a binary file
        # Return only the content of the response where binary data is stored
        return self.request_data(api_name, api_path, req_param, response_json=False).content

    def enable_camera(self,
                      idList: str = None,
                      blIncludeDeletedCam: bool = False) -> dict[str, object] | str:
        """
        Enable one or more cameras by their IDs.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of camera IDs to enable.
        blIncludeDeletedCam : bool, optional
            Whether to include deleted cameras in the operation. Default is False.

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_camera(self,
                       idList: str = None,
                       blIncludeDeletedCam: bool = False) -> dict[str, object] | str:
        """
        Disable one or more cameras by their IDs.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of camera IDs to disable.
        blIncludeDeletedCam : bool, optional
            Whether to include deleted cameras in the operation. Default is False.

        Returns
        -------
        dict[str, object] or str
            Result of the disable operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def get_capability_by_cam_id(self, cameraId: Any = None) -> dict[str, object] | str:
        """
        Retrieve the capability information for a specific camera by its ID.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera for which to retrieve capability information.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the camera's capability information, or a string with error details if the request fails.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetCapabilityByCamId', 'cameraId': cameraId}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def count_occupied_size(self, camId: int = None) -> dict[str, object] | str:
        """
        Retrieve the occupied storage size for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to retrieve the occupied size.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the occupied size information, or a string with error details if the request fails.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetOccupiedSize', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def is_shortcut_valid(self, cameraId: int = None) -> dict[str, object] | str:
        """
        Check if a camera shortcut is valid.

        Parameters
        ----------
        cameraId : int, optional
            The ID of the camera to validate the shortcut for.

        Returns
        -------
        dict[str, object] or str
            A dictionary with the validation result, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CheckCamValid', 'cameraId': cameraId}

        return self.request_data(api_name, api_path, req_param)

    def get_live_path(self, idList: int = None) -> dict[str, object] | str:
        """
        Retrieve the live view path for one or more cameras.

        Parameters
        ----------
        idList : int, optional
            Camera ID or comma-separated list of camera IDs for which to retrieve the live view path.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing the live view path information, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetLiveViewPath', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def audio_event_enum(self, camId: int = None) -> dict[str, object] | str:
        """
        Enumerate audio events for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to enumerate audio events.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing audio event enumeration, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'AudioEnum', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def alarm_event_enum(self, camId: int = None) -> dict[str, object] | str:
        """
        Enumerate alarm events for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to enumerate alarm events.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing alarm event enumeration, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'AlarmEnum', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    def md_parameter_save(self, camId: int = None,
                          source: int = None,
                          mode: int = None,
                          sensitivity: int = None,
                          threshold: int = None,
                          objectSize: int = None,
                          percentage: int = None) -> dict[str, object] | str:
        """
        Save motion detection parameters for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to save motion detection parameters.
        source : int, optional
            The source channel or stream index.
        mode : int, optional
            The motion detection mode.
        sensitivity : int, optional
            Sensitivity level for motion detection.
        threshold : int, optional
            Threshold value for motion detection.
        objectSize : int, optional
            Minimum object size to trigger detection.
        percentage : int, optional
            Minimum percentage of the detection area to trigger detection.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'MDParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def motion_event_enum(self, camId: int = None) -> dict[str, object] | str:
        """
        Enumerate motion events for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to enumerate motion events.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing motion event enumeration, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'MotionEnum', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    def motion_parameter_save(self,
                              camId: int = None,
                              source: int = None,
                              mode: int = None,
                              keep: bool = None,
                              level: int = None) -> dict[str, object] | str:
        """
        Save advanced motion detection parameters for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to save motion detection parameters.
        source : int, optional
            The source channel or stream index.
        mode : int, optional
            The motion detection mode.
        keep : bool, optional
            Whether to keep the current settings.
        level : int, optional
            Sensitivity level for advanced motion detection.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ADParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def di_parameter_save(self,
                          camId: int = None,
                          idx: int = None,
                          keep: bool = None,
                          normal: int = None) -> dict[str, object] | str:
        """
        Save digital input (DI) parameters for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to save DI parameters.
        idx : int, optional
            The index of the DI channel.
        keep : bool, optional
            Whether to keep the current DI settings.
        normal : int, optional
            The normal state value for the DI channel.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DIParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def alarm_sts_polling(self,
                          camId: int = None,
                          timeOut: int = None,
                          # TODO not working
                          keep: Any = None) -> dict[str, object] | str:
        """
        Poll the alarm status for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to poll alarm status.
        timeOut : int, optional
            Timeout value for the polling operation.
        keep : Any, optional
            Reserved for future use or additional options (currently not working).

        Returns
        -------
        dict[str, object] or str
            Dictionary containing alarm status polling result, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'AlarmStsPolling'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def td_parameter_save(self,
                          camId: int = None,
                          source: int = None,
                          keep: Any = None,
                          duration: int = None) -> dict[str, object] | str:
        """
        Save tamper detection (TD) parameters for a specific camera.

        Parameters
        ----------
        camId : int, optional
            The ID of the camera for which to save tamper detection parameters.
        source : int, optional
            The source channel or stream index.
        keep : Any, optional
            Whether to keep the current settings (reserved for future use).
        duration : int, optional
            Duration for the tamper detection event.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TDParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_camera_group(self, privCamType: int = None) -> dict[str, object] | str:
        """
        Enumerate camera groups in Surveillance Station.

        Parameters
        ----------
        privCamType : int, optional
            Camera privilege type to filter groups.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing camera group enumeration, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Group'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Enum', 'privCamType': privCamType}

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def save_specific_group(self, groupList: Any = None) -> dict[str, object] | str:
        """
        Save or update a specific camera group in Surveillance Station.

        Parameters
        ----------
        groupList : Any, optional
            The list of groups to be saved or updated.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Group'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Save', 'groupList': groupList}

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_groups(self, Id: int = None) -> dict[str, object] | str:
        """
        Delete specific camera groups in Surveillance Station.

        Parameters
        ----------
        Id : int, optional
            The ID of the camera group to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Group'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Delete', 'id': Id}

        return self.request_data(api_name, api_path, req_param)

    def enumerate_group_information(self, camServerId: int = None,
                                    shareName: str = None,
                                    archiveName: str = None,
                                    camlist: Any = None,
                                    # TODO not working
                                    actFromHost: bool = None) -> dict[str, object] | str:
        """
        Enumerate group information for camera import in Surveillance Station.

        Parameters
        ----------
        camServerId : int, optional
            The ID of the camera server.
        shareName : str, optional
            The name of the shared folder.
        archiveName : str, optional
            The name of the archive.
        camlist : Any, optional
            List of cameras to include.
        actFromHost : bool, optional
            Whether the action is performed from the host. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the group information enumeration as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Import'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_camera_from_archive(self,
                                      shareName: str = None,
                                      archiveName: str = None,
                                      serverId: int = None) -> dict[str, object] | str:
        """
        Enumerate cameras from a specified archive in Surveillance Station.

        Parameters
        ----------
        shareName : str, optional
            The name of the shared folder containing the archive.
        archiveName : str, optional
            The name of the archive to enumerate cameras from.
        serverId : int, optional
            The ID of the server associated with the archive.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing camera enumeration details, or a string with error details if the request fails.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Import'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ArchiveCamEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_archive_from_folder(self,
                                      # TODO not working
                                      shareName: str = None) -> dict[str, object] | str:
        """
        Enumerate archives from a specified folder in Surveillance Station.

        Parameters
        ----------
        shareName : str, optional
            The name of the shared folder containing the archives.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing archive enumeration details, or a string with error details if the request fails.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Import'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ArchiveEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_available_size_of_sdcard(self,
                                       camId: Any = None,
                                       host: str = None,
                                       port: str = None,
                                       user: str = None,
                                       passw: str = None,
                                       vendor: str = None,
                                       model: str = None,
                                       # TODO not working
                                       ch: str = None) -> dict[str, object] | str:
        """
        Check the available size of the SD card for a specific camera.

        Parameters
        ----------
        camId : Any, optional
            The ID of the camera.
        host : str, optional
            The host address of the camera.
        port : str, optional
            The port number for the camera connection.
        user : str, optional
            The username for authentication.
        passw : str, optional
            The password for authentication.
        vendor : str, optional
            The vendor of the camera.
        model : str, optional
            The model of the camera.
        ch : str, optional
            The channel identifier. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the available size information, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ArchiveEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key is passw:
                        req_param[str('pass')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def check_licence_quota(self) -> dict[str, object] | str:
        """
        Check the license quota for Surveillance Station cameras.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing license quota information, or a string with error details if the request fails.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckQuota'}

        return self.request_data(api_name, api_path, req_param)

    def format_specific_sd_card(self,
                                camId: Any = None,
                                host: str = None,
                                port: str = None,
                                user: str = None,
                                passw: str = None,
                                vendor: str = None,
                                model: str = None,
                                ch: str = None,
                                # TODO not working
                                timeout: int = None) -> dict[str, object] | str:
        """
        Format the SD card of a specific camera.

        Parameters
        ----------
        camId : Any, optional
            The ID of the camera whose SD card is to be formatted.
        host : str, optional
            The host address of the camera.
        port : str, optional
            The port number for the camera connection.
        user : str, optional
            The username for authentication.
        passw : str, optional
            The password for authentication.
        vendor : str, optional
            The vendor of the camera.
        model : str, optional
            The model of the camera.
        ch : str, optional
            The channel identifier.
        timeout : int, optional
            Timeout value for the formatting operation. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the result of the format operation, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'FormatSDCard'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key is passw:
                        req_param[str('pass')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def quick_create_single_camera(self,
                                   camServerId: Any = None,
                                   actFromHost: bool = None,
                                   camStreamingType: str = None,
                                   camName: str = None,
                                   camIP: str = None,
                                   camPort: str = None,
                                   camVendor: str = None,
                                   camModel: str = None,
                                   camMountType: int = None,
                                   camChannel: str = None,
                                   camVideoType: str = None,
                                   camAudioType: str = None,
                                   camSourcePath: str = None,
                                   camUserName: str = None,
                                   # TODO to check
                                   camPassWord: str = None) -> dict[str, object] | str:
        """
        Quickly create a single camera in Surveillance Station.

        Parameters
        ----------
        camServerId : Any, optional
            The ID of the camera server.
        actFromHost : bool, optional
            Whether the action is performed from the host.
        camStreamingType : str, optional
            The streaming type of the camera.
        camName : str, optional
            The name of the camera.
        camIP : str, optional
            The IP address of the camera.
        camPort : str, optional
            The port number of the camera.
        camVendor : str, optional
            The vendor of the camera.
        camModel : str, optional
            The model of the camera.
        camMountType : int, optional
            The mount type of the camera.
        camChannel : str, optional
            The channel of the camera.
        camVideoType : str, optional
            The video type of the camera.
        camAudioType : str, optional
            The audio type of the camera.
        camSourcePath : str, optional
            The source path for the camera stream.
        camUserName : str, optional
            The username for camera authentication.
        camPassWord : str, optional
            The password for camera authentication. (To be checked).

        Returns
        -------
        dict[str, object] or str
            Result of the quick create operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'QuickCreate'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_camera_lens(self,
                         cameraId: Any = None,
                         direction: str = None,
                         speed: int = None,
                         # TODO not working
                         moveType: str = None) -> dict[str, object] | str:
        """
        Move the camera lens in a specified direction with an optional speed and move type.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control.
        direction : str, optional
            The direction to move the lens (e.g., 'up', 'down', 'left', 'right').
        speed : int, optional
            The speed at which to move the lens.
        moveType : str, optional
            The type of movement (reserved for future use, currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the move operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Move'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def camera_lens_zoom(self,
                         cameraId: Any = None,
                         control: Any = None,
                         # TODO not working
                         moveType: str = None) -> dict[str, object] | str:
        """
        Control the zoom function of a camera lens.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control.
        control : Any, optional
            The zoom control command or value.
        moveType : str, optional
            The type of movement (reserved for future use, currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the zoom operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Zoom'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_preset_ptz_camera(self,
                               cameraId: Any = None,
                               offset: int = None,
                               # TODO not working
                               limit: int = None) -> dict[str, object] | str:
        """
        List preset positions for a PTZ (Pan-Tilt-Zoom) camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the PTZ camera to list presets for.
        offset : int, optional
            The starting index for the preset list.
        limit : int, optional
            The maximum number of presets to return. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Dictionary containing the list of PTZ presets, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_camera_lens_to_preset_position(self,
                                            cameraId: Any = None,
                                            presetId: Any = None,
                                            position: Any = None,
                                            speed: Any = None,
                                            type: Any = None,
                                            # TODO not working
                                            isPatrol: bool = None) -> dict[str, object] | str:
        """
        Move the camera lens to a specified preset position.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control.
        presetId : Any, optional
            The ID of the preset position to move to.
        position : Any, optional
            The position value for the preset.
        speed : Any, optional
            The speed at which to move the lens.
        type : Any, optional
            The type of movement or preset.
        isPatrol : bool, optional
            Whether the movement is part of a patrol operation. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the move operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GoPreset'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_patrol_cameras(self,
                            cameraId: Any = None,
                            offset: int = None,
                            # TODO not working
                            limit: int = None) -> dict[str, object] | str:
        """
        List patrols for a PTZ (Pan-Tilt-Zoom) camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the PTZ camera to list patrols for.
        offset : int, optional
            The starting index for the patrol list.
        limit : int, optional
            The maximum number of patrols to return. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Dictionary containing the list of PTZ patrols, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListPatrol'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def force_cam_to_execute_patrol(self,
                                    cameraId: Any = None,
                                    # TODO not working
                                    patrolId: Any = None) -> dict[str, object] | str:
        """
        Force a camera to execute a specified patrol.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to execute the patrol.
        patrolId : Any, optional
            The ID of the patrol to execute. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the patrol execution as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RunPatrol'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def focus_camera(self,
                     cameraId: Any = None,
                     control: Any = None,
                     # TODO not working
                     moveType: Any = None) -> dict[str, object] | str:
        """
        Control the focus function of a camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control.
        control : Any, optional
            The focus control command or value.
        moveType : Any, optional
            The type of movement (reserved for future use, currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the focus operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Focus'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def control_camera_iris_in_out(self,
                                   cameraId: Any = None,
                                   control: Any = None,
                                   # TODO not working
                                   moveType: Any = None) -> dict[str, object] | str:
        """
        Control the iris (in/out) function of a camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control.
        control : Any, optional
            The iris control command or value.
        moveType : Any, optional
            The type of movement (reserved for future use, currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the iris control operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Iris'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def auto_focus(self, cameraId: Any = None) -> dict[str, object] | str:
        """
        Perform an auto-focus operation on a specified camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to auto-focus.

        Returns
        -------
        dict[str, object] or str
            Result of the auto-focus operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AutoFocus'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_cam_lens_to_absolute_position(self,
                                           posX: int = None,
                                           # TODO not working
                                           posY: int = None) -> dict[str, object] | str:
        """
         Move the camera lens to an absolute position.

         Parameters
         ----------
         posX : int, optional
             The X coordinate for the absolute position.
         posY : int, optional
             The Y coordinate for the absolute position. (Currently not working).

         Returns
         -------
         dict[str, object] or str
             Result of the move operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AbsPtz'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_cam_to_home_position(self,
                                  # TODO not working
                                  cameraId: Any = None) -> dict[str, object] | str:
        """
        Move the camera to its home position.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to move to the home position. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the move operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Home'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def auto_pan_camera(self,
                        cameraId: Any = None,
                        # TODO not working
                        moveType: str = None) -> dict[str, object] | str:
        """
        Automatically pan the camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to auto-pan.
        moveType : str, optional
            The type of movement (reserved for future use, currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the auto-pan operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AutoPan'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_stop_object_tracking(self,
                                   cameraId: Any = None,
                                   # TODO not working
                                   moveType: str = None) -> dict[str, object] | str:
        """
        Start or stop object tracking for a specified camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control object tracking.
        moveType : str, optional
            The type of movement (reserved for future use, currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the object tracking operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ObjTracking'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_stop_external_recording(self,
                                      cameraId: Any = None,
                                      # TODO not working
                                      action: str = None) -> dict[str, object] | str:
        """
        Start or stop external recording for a specified camera.

        Parameters
        ----------
        cameraId : Any, optional
            The ID of the camera to control external recording.
        action : str, optional
            The action to perform (e.g., 'start' or 'stop'). (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the external recording operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.ExternalRecording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Record'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def query_event_list_by_filter(self,
                                   offset: int = None,
                                   limit: int = None,
                                   cameraIds: str = None,
                                   fromTime: int = None,
                                   toTime: int = None,
                                   dsld: int = None,
                                   mountId: int = None) -> dict[str, object] | str:
        """
        Query the event list by applying various filters.

        Parameters
        ----------
        offset : int, optional
            The starting index for the event list.
        limit : int, optional
            The maximum number of events to return.
        cameraIds : str, optional
            Comma-separated list of camera IDs to filter events.
        fromTime : int, optional
            Start time (timestamp) for filtering events.
        toTime : int, optional
            End time (timestamp) for filtering events.
        dsld : int, optional
            Device slot ID to filter events.
        mountId : int, optional
            Mount ID to filter events.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing the filtered event list, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_recordings(self,
                          idList: int = None,
                          dsld: int = None) -> dict[str, object] | str:
        """
        Delete specific recordings from Surveillance Station.

        Parameters
        ----------
        idList : int, optional
            The ID or comma-separated list of IDs of the recordings to delete.
        dsld : int, optional
            Device slot ID associated with the recordings.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_events_by_filter(self,
                                reason: str = None,
                                cameraIds: str = None,
                                fromTime: Any = None,
                                toTime: Any = None,
                                locked: int = None,
                                evtSrcType: int = None,
                                evtSrcId: int = None,
                                blIncludeSnapshot: bool = None,
                                includeAllCam: bool = None,
                                from_end: int = None,
                                # TODO not working
                                from_start: int = None) -> dict[str, object] | str:
        """
        Delete events from Surveillance Station by applying various filters.

        Parameters
        ----------
        reason : str, optional
            The reason for deleting the events.
        cameraIds : str, optional
            Comma-separated list of camera IDs to filter events.
        fromTime : Any, optional
            Start time (timestamp) for filtering events.
        toTime : Any, optional
            End time (timestamp) for filtering events.
        locked : int, optional
            Whether to include locked events.
        evtSrcType : int, optional
            Event source type.
        evtSrcId : int, optional
            Event source ID.
        blIncludeSnapshot : bool, optional
            Whether to include snapshots in the deletion.
        includeAllCam : bool, optional
            Whether to include all cameras.
        from_end : int, optional
            End index for the filter range.
        from_start : int, optional
            Start index for the filter range. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteFilter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def delete_all_recordings(self) -> dict[str, object] | str:
        """
        Delete all recordings from Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteAll'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def apply_settings_advance_tab(self,
                                   # TODO not working
                                   rotateUnrecogCam: bool = None) -> dict[str, object] | str:
        """
        Apply advanced settings in the Surveillance Station recording tab.

        Parameters
        ----------
        rotateUnrecogCam : bool, optional
            Whether to rotate unrecognized cameras. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the apply operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ApplyAdvanced'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_by_number_of_event(self,
                                 offset: bool = None,
                                 limit: int = None,
                                 reason: str = None,
                                 cameraIds: str = None,
                                 fromTime: int = None,
                                 toTime: int = None,
                                 locked: int = None,
                                 evtSrcType: int = None,
                                 evtSrcId: int = None,
                                 blIncludeSnapshot: bool = None,
                                 # TODO not working
                                 includeAllCam: bool = None) -> dict[str, object] | str:
        """
        Count the number of events by category, with optional filters.

        Parameters
        ----------
        offset : bool, optional
            Whether to offset the results.
        limit : int, optional
            The maximum number of results to return.
        reason : str, optional
            The reason for filtering events.
        cameraIds : str, optional
            Comma-separated list of camera IDs to filter events.
        fromTime : int, optional
            Start time (timestamp) for filtering events.
        toTime : int, optional
            End time (timestamp) for filtering events.
        locked : int, optional
            Whether to include locked events.
        evtSrcType : int, optional
            Event source type.
        evtSrcId : int, optional
            Event source ID.
        blIncludeSnapshot : bool, optional
            Whether to include snapshots in the count.
        includeAllCam : bool, optional
            Whether to include all cameras. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Dictionary containing the event count by category, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def keep_event_play_alive(self) -> dict[str, object] | str:
        """
        Keep the event play session alive.

        Returns
        -------
        dict[str, object] or str
            Result of the keepalive operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Keepalive'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_recording_event(self,
                             # TODO not working
                             idList: Any = None) -> dict[str, object] | str:
        """
        Stop a recording event for the specified event IDs.

        Parameters
        ----------
        idList : Any, optional
            The ID or list of IDs of the events to stop recording. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the stop operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Trunc'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def load_settings_in_advanced_tab(self) -> dict[str, object] | str:
        """
        Load settings from the advanced tab in Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            Dictionary containing the advanced settings, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LoadAdvanced'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_selected_event(self,
                            reason: str = None,
                            cameraIds: str = None,
                            fromTime: int = None,
                            toTime: int = None,
                            locked: int = None,
                            evtSrcType: int = None,
                            evtSrcId: int = None,
                            blIncludeSnapshot: bool = None,
                            includeAllCam: bool = None,
                            from_end: int = None,
                            # TODO not working
                            from_start: int = None) -> dict[str, object] | str:
        """
        Lock selected events by applying various filters.

        Parameters
        ----------
        reason : str, optional
            The reason for locking the events.
        cameraIds : str, optional
            Comma-separated list of camera IDs to filter events.
        fromTime : int, optional
            Start time (timestamp) for filtering events.
        toTime : int, optional
            End time (timestamp) for filtering events.
        locked : int, optional
            Whether to lock the events.
        evtSrcType : int, optional
            Event source type.
        evtSrcId : int, optional
            Event source ID.
        blIncludeSnapshot : bool, optional
            Whether to include snapshots in the lock operation.
        includeAllCam : bool, optional
            Whether to include all cameras.
        from_end : int, optional
            End index for the filter range.
        from_start : int, optional
            Start index for the filter range. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the lock operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LockFilter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_selected_event(self,
                              idList: str = None,
                              # TODO not working
                              dsld: int = None) -> dict[str, object] | str:
        """
        Unlock selected events by their IDs.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of event IDs to unlock.
        dsld : int, optional
            Device slot ID associated with the events. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_selected_filter_event(self,
                                     reason: str = None,
                                     cameraIds: str = None,
                                     fromTime: int = None,
                                     toTime: int = None,
                                     locked: int = None,
                                     evtSrcType: int = None,
                                     # TODO not working
                                     evtSrcId: int = None) -> dict[str, object] | str:
        """
        Unlock events by applying various filters.

        Parameters
        ----------
        reason : str, optional
            The reason for unlocking the events.
        cameraIds : str, optional
            Comma-separated list of camera IDs to filter events.
        fromTime : int, optional
            Start time (timestamp) for filtering events.
        toTime : int, optional
            End time (timestamp) for filtering events.
        locked : int, optional
            Whether to unlock only locked events.
        evtSrcType : int, optional
            Event source type.
        evtSrcId : int, optional
            Event source ID. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'UnlockFilter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_selected_recordings(self,
                                 idList: str = None,
                                 dsld: int = None) -> dict[str, object] | str:
        """
        Lock selected recordings by their IDs.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of recording IDs to lock.
        dsld : int, optional
            Device slot ID associated with the recordings.

        Returns
        -------
        dict[str, object] or str
            Result of the lock operation as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_recordings(self,
                            id: int = None,
                            mountId: int = None,
                            offsetTimeMs: int = None,
                            playTimeMs: int = None) -> dict[str, object] | str:
        """
        Download recordings by specifying recording ID and optional parameters.

        Parameters
        ----------
        id : int, optional
            The ID of the recording to download.
        mountId : int, optional
            The mount ID associated with the recording.
        offsetTimeMs : int, optional
            Offset time in milliseconds for the download.
        playTimeMs : int, optional
            Playback time in milliseconds for the download.

        Returns
        -------
        dict[str, object] or str
            The downloaded recording as a binary response, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Download'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param, response_json=False)

    def check_if_recording_playable(self,
                                    eventId: int = None,
                                    chkDetail: bool = None,
                                    mountId: int = None,
                                    # TODO not working
                                    dsld: int = None) -> dict[str, object] | str:
        """
        Check if a recording is playable by event ID and optional parameters.

        Parameters
        ----------
        eventId : int, optional
            The event ID of the recording to check.
        chkDetail : bool, optional
            Whether to check detailed information.
        mountId : int, optional
            The mount ID associated with the recording.
        dsld : int, optional
            Device slot ID. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the check as a dictionary, or a string with error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CheckEventValid'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def play_specific_recording(self,
                                recordingId: int = None,
                                alertRecording: bool = None,
                                mountId: int = None,
                                dsld: int = None,
                                # TODO not working
                                videoCodec: int = None) -> dict[str, object] | str:
        """
        Stream a specific recording from Surveillance Station.

        Parameters
        ----------
        recordingId : int, optional
            The ID of the recording to play.
        alertRecording : bool, optional
            Whether the recording is an alert recording.
        mountId : int, optional
            The mount ID associated with the recording.
        dsld : int, optional
            Device slot ID.
        videoCodec : int, optional
            Video codec to use for streaming. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Streaming information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Stream'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_merged_recording_files(self,
                                        camId: int = None,
                                        fromTime: int = None,
                                        toTime: int = None,
                                        # TODO not working
                                        fileName: str = None) -> dict[str, object] | str:
        """
        Download merged files of recordings within a UTC time range for a target camera.

        If there are different resolutions or codecs within the time range, recordings will be merged as much as possible,
        and the download file will be a zip file.

        This method starts a task with a keep-alive mechanism.
        Use GetRangeExportProgress to get the latest progress and keep-alive.
        After receiving progress 100, use OnRangeExportDone to download the exported recording within 1 minute.
        To cancel the export task, do not send GetRangeExportProgress or OnRangeExportDone; the system will clean up processed files.

        Parameters
        ----------
        camId : int, optional
            The camera ID to export recordings from.
        fromTime : int, optional
            Start UTC timestamp for the export range.
        toTime : int, optional
            End UTC timestamp for the export range.
        fileName : str, optional
            Name of the output file. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Task information for the export or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RangeExport'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def get_newest_progress_keep_alive(self, dlid: int = None) -> dict[str, object] | str:
        """
        Get the latest progress of a range export task and keep the task alive.

        Parameters
        ----------
        dlid : int, optional
            The download task ID.

        Returns
        -------
        dict[str, object] or str
            Progress information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetRangeExportProgress'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_recording_from_target(self,
                                       dlid: int = None,
                                       # TODO not working
                                       fileName: str = None) -> dict[str, object] | str:
        """
         Download the exported recording file from a completed range export task.

         Parameters
         ----------
         dlid : int, optional
             The download task ID.
         fileName : str, optional
             Name of the file to download. (Currently not working).

         Returns
         -------
         dict[str, object] or str
             Downloaded file data or error details.

         Notes
         -----
         GetRangeExportProgress must be called within 1 minute after the corresponding RangeExport task is completed,
         otherwise the exported recordings will be cleared.

         Response: Returns MP4 or zip file data. The response type can be found in the fileExt field of the GetRangeExportProgress
         response when progress is 100.

         API Error Codes:
         400 : Execution failed.
         401 : Parameter invalid.
         405 : CMS server connection failed.
         414 : Some events do not exist.
         439 : Too many items selected.
        """

        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'OnRangeExportDone'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def handle_load_event_export(self,
                                 start: int = None,
                                 limit: bool = None) -> dict[str, object] | str:
        """
        Load exported event recordings with optional pagination.

        Parameters
        ----------
        start : int, optional
            The starting index for loading events.
        limit : bool, optional
            The maximum number of events to load.

        Returns
        -------
        dict[str, object] or str
            Exported event information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_name_export_event(self,
                                dsId: int = None,
                                name: int = None,
                                share: str = None) -> dict[str, object] | str:
        """
        Check if an export event name is valid or already exists.

        Parameters
        ----------
        dsId : int, optional
            The data source ID.
        name : int, optional
            The name to check for the export event.
        share : str, optional
            The share name associated with the export event.

        Returns
        -------
        dict[str, object] or str
            Result of the name check or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckName'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_information_list(self,
                                    dslld: int = None) -> dict[str, object] | str:
        """
        Retrieve the list of camera information for event export.

        Parameters
        ----------
        dslld : int, optional
            The ID of the data source (recording server) to query cameras from.

        Returns
        -------
        dict[str, object] or str
            Camera information list or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CamEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_destination_folder_availability(self,
                                              freeSize: int = None,
                                              startTime: int = None,
                                              stopTime: int = None,
                                              camIdList: str = None) -> dict[str, object] | str:
        """
        Check if the destination folder has enough available space for export.

        Parameters
        ----------
        freeSize : int, optional
            Required free size in bytes.
        startTime : int, optional
            Start time of the export range (UTC timestamp).
        stopTime : int, optional
            End time of the export range (UTC timestamp).
        camIdList : str, optional
            Comma-separated list of camera IDs to check.

        Returns
        -------
        dict[str, object] or str
            Availability information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CheckAvailableExport'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def handle_save_event_export(self,
                                 name: str = None,
                                 srcDsId: int = None,
                                 dstDsId: int = None,
                                 dstdir: str = None,
                                 freesize: int = None,
                                 start_time: int = None,
                                 stop_time: int = None,
                                 isoverwrite: int = None,
                                 camlistid: str = None) -> dict[str, object] | str:
        """
        Save an event export task with the specified parameters.

        Parameters
        ----------
        name : str, optional
            Name of the export task.
        srcDsId : int, optional
            Source data source ID.
        dstDsId : int, optional
            Destination data source ID.
        dstdir : str, optional
            Destination directory for export.
        freesize : int, optional
            Required free size in bytes.
        start_time : int, optional
            Start time of the export range (UTC timestamp).
        stop_time : int, optional
            End time of the export range (UTC timestamp).
        isoverwrite : int, optional
            Whether to overwrite existing files (1 for true, 0 for false).
        camlistid : str, optional
            Comma-separated list of camera IDs to export.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_event_export_info_from_recording_server(self,
                                                    start_time: int = None,
                                                    stop_time: int = None,
                                                    camlistid: str = None) -> dict[str, object] | str:
        """
        Retrieve event export information from the recording server.

        Parameters
        ----------
        start_time : int, optional
            Start time of the export range (UTC timestamp).
        stop_time : int, optional
            End time of the export range (UTC timestamp).
        camlistid : str, optional
            Comma-separated list of camera IDs.

        Returns
        -------
        dict[str, object] or str
            Export information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetEvtExpInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_event_mount(self) -> dict[str, object] | str:
        """
        Load event mount information for export.

        Returns
        -------
        dict[str, object] or str
            Mount information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Mount'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def redirect_webapi_to_target_ds(self,
                                     dsId: int = None,
                                     # TODO not working
                                     webAPI: Any = None) -> dict[str, object] | str:
        """
        Redirect a WebAPI request to a target DiskStation.

        Parameters
        ----------
        dsId : int, optional
            Target DiskStation ID.
        webAPI : Any, optional
            WebAPI information to redirect (array of webAPI_info).

        Returns
        -------
        dict[str, object] or str
            Result of the redirect operation or error details.

        Examples
        --------
        webAPI={"api": "SYNO.SurveillanceStation.AddOns", "version": 1, "method": "List"}
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Redirect'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def modify_share_privilege(self,
                               privSet: int = None,
                               # TODO not working
                               shareName: str = None) -> dict[str, object] | str:
        """
        Modify the share privilege settings in Surveillance Station CMS.

        Parameters
        ----------
        privSet : int, optional
            Privilege set value.
        shareName : str, optional
            Name of the share to modify.

        Returns
        -------
        dict[str, object] or str
            Result of the privilege modification or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def apply_option_settings(self,
                              central_auto_video_relay: bool = None,
                              central_enable: bool = None,
                              central_mode: str = None,
                              central_rec_mask_mode: bool = None,
                              central_rec_sync_time: bool = None,
                              nvr_enable: bool = None,
                              # TODO not working
                              nvr_lang: str = None) -> dict[str, object] | str:
        """
        Apply option settings for Surveillance Station CMS.

        Parameters
        ----------
        central_auto_video_relay : bool, optional
            Enable or disable central auto video relay.
        central_enable : bool, optional
            Enable or disable central management.
        central_mode : str, optional
            Set the central management mode.
        central_rec_mask_mode : bool, optional
            Enable or disable central recording mask mode.
        central_rec_sync_time : bool, optional
            Enable or disable central recording time synchronization.
        nvr_enable : bool, optional
            Enable or disable NVR.
        nvr_lang : str, optional
            Set the NVR language. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the apply operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ApplyOption'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_cms_info(self,
                     # TODO not working
                     isPolling: bool = None) -> dict[str, object] | str:
        """
        Retrieve CMS (Central Management System) information.

        Parameters
        ----------
        isPolling : bool, optional
            Whether to poll for CMS information. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            CMS information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_log_recording_data_from_target_ds(self,
                                              syncType: int = None,
                                              syncTargetId: int = None,
                                              # TODO not working
                                              limit: int = None) -> dict[str, object] | str:
        """
        Retrieve log recording data from a target DiskStation.

        Parameters
        ----------
        syncType : int, optional
            Type of synchronization.
        syncTargetId : int, optional
            ID of the target DiskStation for synchronization.
        limit : int, optional
            Limit the number of records returned. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Log recording data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DoSyncData'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_samba_service(self) -> dict[str, object] | str:  # TODO not working
        """
        Check if the Samba service is enabled on the CMS.

        Returns
        -------
        dict[str, object] or str
            Samba service status or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CheckSambaEnabled'}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def check_if_samba_on_and_rec_enabled(self) -> dict[str, object] | str:
        """
        Check if Samba is enabled and recording is enabled on the CMS.

        Returns
        -------
        dict[str, object] or str
            Status of Samba and recording or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'BatCheckSambaService'}

        return self.request_data(api_name, api_path, req_param)

    def get_encoded_single_image_of_camera(self,
                                           camId: int = None) -> dict[str, object] | str:
        """
        Retrieve an encoded single image (snapshot) from a specified camera.

        Parameters
        ----------
        camId : int, optional
            ID of the camera to get the snapshot from.

        Returns
        -------
        dict[str, object] or str
            Encoded image data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetMDSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_cms_status(self,
                       # TODO not working
                       camId: int = None) -> dict[str, object] | str:
        """
        Retrieve the status of the CMS.

        Parameters
        ----------
        camId : int, optional
            ID of the camera to check status for. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            CMS status or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCMSStatus'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def enable_smb_service(self) -> dict[str, object] | str:
        """
        Enable the Samba service on the CMS.

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableSamba'}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def notify_slave_ds_to_disconnect(self) -> dict[str, object] | str:
        """
        Notify a slave DiskStation to disconnect from the CMS.

        Returns
        -------
        dict[str, object] or str
            Result of the notification or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'NotifyCMSBreak'}

        return self.request_data(api_name, api_path, req_param)

    def lock_recording_server_prevent_setting_change(self,
                                                     # TODO not working
                                                     locked: bool = None) -> dict[str, object] | str:
        """
        Lock the recording server to prevent setting changes.

        Parameters
        ----------
        locked : bool, optional
            Whether to lock the server. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the lock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LockSelf'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_ds_into_recording_server(self,
                                        adminUsername: str = None,
                                        adminPasswd: str = None,
                                        central_rec_mask_mode: str = None,
                                        central_rec_sync_time: str = None) -> dict[str, object] | str:
        """
        Enable a DiskStation as a recording server in the CMS.

        Parameters
        ----------
        adminUsername : str, optional
            Administrator username.
        adminPasswd : str, optional
            Administrator password.
        central_rec_mask_mode : str, optional
            Central recording mask mode.
        central_rec_sync_time : str, optional
            Central recording synchronization time.

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableCMS'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unpair_recording_servers(self,
                                 adminUsername: str = None,
                                 key: str = None,
                                 mac: str = None,
                                 cmsMode: int = None) -> dict[str, object] | str:
        """
        Unpair recording servers from the CMS.

        Parameters
        ----------
        adminUsername : str, optional
            Administrator username.
        key : str, optional
            Key for unpairing.
        mac : str, optional
            MAC address of the server.
        cmsMode : int, optional
            CMS mode.

        Returns
        -------
        dict[str, object] or str
            Result of the unpair operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'UnPair'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_free_memory_size(self) -> dict[str, object] | str:
        """
        Retrieve the free memory size from the target DiskStation.

        Returns
        -------
        dict[str, object] or str
            Free memory size information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetFreeSpace'}

        return self.request_data(api_name, api_path, req_param)

    def handle_slave_ds(self,
                        lock: bool = None,
                        adminUsername: str = None,
                        key: str = None,
                        mac: str = None,
                        # TODO to check
                        masterAuthKey: str = None) -> dict[str, object] | str:
        """
        Handle slave DiskStation operations such as locking or authentication.

        Parameters
        ----------
        lock : bool, optional
            Whether to lock the slave DiskStation.
        adminUsername : str, optional
            Administrator username.
        key : str, optional
            Authentication key.
        mac : str, optional
            MAC address of the slave DiskStation.
        masterAuthKey : str, optional
            Master authentication key. (To check).

        Returns
        -------
        dict[str, object] or str
            Result of the operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_target_ds_info(self,
                           slaveDslp: str = None) -> dict[str, object] | str:
        """
        Retrieve information about the target slave DiskStation.

        Parameters
        ----------
        slaveDslp : str, optional
            Slave DiskStation IP or identifier.

        Returns
        -------
        dict[str, object] or str
            Target DiskStation information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Test'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def logout_slave_ds(self,
                        adminUsername: str = None,
                        key: str = None,
                        mac: str = None) -> dict[str, object] | str:
        """
        Log out a slave DiskStation from the CMS.

        Parameters
        ----------
        adminUsername : str, optional
            Administrator username.
        key : str, optional
            Authentication key.
        mac : str, optional
            MAC address of the slave DiskStation.

        Returns
        -------
        dict[str, object] or str
            Result of the logout operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Logout'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def pair_slave_ds(self,
                      dsname: str = None,
                      slaveDslp: str = None,
                      port: int = None,
                      masterAuthKey: str = None,
                      model: str = None,
                      mac: str = None,
                      cms_locked: bool = None,
                      cms_masked: bool = None,
                      # TODO not working
                      cms_sync_time: bool = None) -> dict[str, object] | str:
        """
        Pair a slave DiskStation with the CMS.

        Parameters
        ----------
        dsname : str, optional
            Name of the slave DiskStation.
        slaveDslp : str, optional
            Slave DiskStation IP or identifier.
        port : int, optional
            Port number for connection.
        masterAuthKey : str, optional
            Master authentication key.
        model : str, optional
            Model of the slave DiskStation.
        mac : str, optional
            MAC address of the slave DiskStation.
        cms_locked : bool, optional
            Whether the CMS is locked.
        cms_masked : bool, optional
            Whether the CMS is masked.
        cms_sync_time : bool, optional
            Synchronize time with CMS. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the pairing operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Pair'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def login_slave_ds(self,
                       adminUsername: str = None,
                       key: str = None,
                       mac: str = None,
                       masterAuthKey: str = None,
                       hostName: str = None,
                       hostPort: int = None,
                       ignoreAuthError: str = None,
                       hostDisconnect: bool = None,
                       blUpdateVolSpace: bool = None,
                       enable_rec: bool = None,
                       cms_locked: bool = None,
                       cms_masked: bool = None,
                       # TODO not working
                       cms_sync_time: bool = None) -> dict[str, object] | str:
        """
        Log in a slave DiskStation to the CMS.

        Parameters
        ----------
        adminUsername : str, optional
            Administrator username.
        key : str, optional
            Authentication key.
        mac : str, optional
            MAC address of the slave DiskStation.
        masterAuthKey : str, optional
            Master authentication key.
        hostName : str, optional
            Hostname of the slave DiskStation.
        hostPort : int, optional
            Port number for connection.
        ignoreAuthError : str, optional
            Ignore authentication errors.
        hostDisconnect : bool, optional
            Whether to disconnect the host.
        blUpdateVolSpace : bool, optional
            Update volume space information.
        enable_rec : bool, optional
            Enable recording.
        cms_locked : bool, optional
            Whether the CMS is locked.
        cms_masked : bool, optional
            Whether the CMS is masked.
        cms_sync_time : bool, optional
            Synchronize time with CMS. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the login operation or error details.

        Notes
        -----
        2.3.15.9 API Error Code
            Code Description
            400 Execution failed.
            401 Invalid parameter.
            415 message connect failed.
        """

        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Login'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_slave_ds(self,
                      slavedsName: str = None,
                      slavedsModel: str = None,
                      slavedsPort: int = None,
                      slavedsVersion: str = None,
                      slavedsMaxCamNum: int = None,
                      slavedsId: str = None,
                      slavedsIP: str = None,
                      slavedsEnable: int = None,
                      slavedsCamCnt: bool = None,
                      adminUsername: str = None,
                      adminPasswd: str = None,
                      cms_locked: bool = None,
                      cms_masked: bool = None,
                      # TODO not working
                      cms_sync_time: bool = None) -> dict[str, object] | str:
        """
        Save or update a slave DiskStation's configuration in the CMS.

        Parameters
        ----------
        slavedsName : str, optional
            Name of the slave DiskStation.
        slavedsModel : str, optional
            Model of the slave DiskStation.
        slavedsPort : int, optional
            Port number used by the slave DiskStation.
        slavedsVersion : str, optional
            Version of the slave DiskStation.
        slavedsMaxCamNum : int, optional
            Maximum number of cameras supported by the slave DiskStation.
        slavedsId : str, optional
            Identifier for the slave DiskStation.
        slavedsIP : str, optional
            IP address of the slave DiskStation.
        slavedsEnable : int, optional
            Enable status of the slave DiskStation.
        slavedsCamCnt : bool, optional
            Number of cameras currently connected to the slave DiskStation.
        adminUsername : str, optional
            Administrator username for authentication.
        adminPasswd : str, optional
            Administrator password for authentication.
        cms_locked : bool, optional
            Whether the CMS is locked.
        cms_masked : bool, optional
            Whether the CMS is masked.
        cms_sync_time : bool, optional
            Synchronize time with CMS. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_slave_ds_list(self,
                           blNeedStatus: bool = None,
                           blGetSortInfo: bool = None,
                           blRuntimeInfo: bool = None,
                           dslds: str = None,
                           sortInfo: int = None) -> dict[str, object] | str:
        """
        Load the list of slave DiskStations from the CMS.

        Parameters
        ----------
        blNeedStatus : bool, optional
            Whether to include status information.
        blGetSortInfo : bool, optional
            Whether to include sorting information.
        blRuntimeInfo : bool, optional
            Whether to include runtime information.
        dslds : str, optional
            Comma-separated list of DiskStation IDs to load.
        sortInfo : int, optional
            Sorting information.

        Returns
        -------
        dict[str, object] or str
            List of slave DiskStations or error details.
        """
        api_name = 'SYNO.SurveillanceStation.CMS.SlavedsList'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_number_of_logs(self,
                             slavedsName: str = None,
                             start: int = None,
                             limit: int = None,
                             level: str = None,
                             filterCamera: str = None,
                             cameraIds: str = None,
                             dsfrom: int = None,
                             to: int = None,
                             keyword: str = None,
                             keywordDsId: str = None,
                             time2String: str = None,
                             dsId: str = None,
                             srcType: int = None,
                             timezoneOffset: int = None) -> dict[str, object] | str:
        """
        Count the number of logs in Surveillance Station based on various filters.

        Parameters
        ----------
        slavedsName : str, optional
            Name of the slave DiskStation.
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of logs to count.
        level : str, optional
            Log level filter.
        filterCamera : str, optional
            Filter by camera.
        cameraIds : str, optional
            Comma-separated list of camera IDs.
        dsfrom : int, optional
            Start time (timestamp).
        to : int, optional
            End time (timestamp).
        keyword : str, optional
            Keyword to search in logs.
        keywordDsId : str, optional
            DiskStation ID for keyword search.
        time2String : str, optional
            Time string for filtering.
        dsId : str, optional
            DiskStation ID.
        srcType : int, optional
            Source type filter.
        timezoneOffset : int, optional
            Timezone offset.

        Returns
        -------
        dict[str, object] or str
            Count of logs or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_selected_logs(self,
                            blClearAll: bool = None,
                            level: int = None,
                            dsId: int = None,
                            filterCamera: str = None,
                            cameraIds: str = None,
                            dsfrom: int = None,
                            to: int = None,
                            keyword: str = None,
                            keywordDsId: str = None,
                            srcType: int = None,
                            timezoneOffset: int = None) -> dict[str, object] | str:
        """
        Clear selected logs from Surveillance Station based on various filters.

        Parameters
        ----------
        blClearAll : bool, optional
            Whether to clear all logs.
        level : int, optional
            Log level filter.
        dsId : int, optional
            DiskStation ID.
        filterCamera : str, optional
            Filter by camera.
        cameraIds : str, optional
            Comma-separated list of camera IDs.
        dsfrom : int, optional
            Start time (timestamp).
        to : int, optional
            End time (timestamp).
        keyword : str, optional
            Keyword to search in logs.
        keywordDsId : str, optional
            DiskStation ID for keyword search.
        srcType : int, optional
            Source type filter.
        timezoneOffset : int, optional
            Timezone offset.

        Returns
        -------
        dict[str, object] or str
            Result of the clear operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Clear'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_information_log(self,
                            start: int = None,
                            limit: int = None,
                            level: str = None,
                            filterCamera: str = None,
                            cameraIds: str = None,
                            dsfrom: int = None,
                            to: int = None,
                            keyword: str = None,
                            keywordDsId: str = None,
                            time2String: str = None,
                            dsId: int = None,
                            srcType: int = None,
                            all: bool = None,
                            blIncludeRecCnt: str = None,
                            blIncludeAuInfo: str = None) -> dict[str, object] | str:
        """
        Retrieve information logs from Surveillance Station based on various filters.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of logs to retrieve.
        level : str, optional
            Log level filter.
        filterCamera : str, optional
            Filter by camera.
        cameraIds : str, optional
            Comma-separated list of camera IDs.
        dsfrom : int, optional
            Start time (timestamp).
        to : int, optional
            End time (timestamp).
        keyword : str, optional
            Keyword to search in logs.
        keywordDsId : str, optional
            DiskStation ID for keyword search.
        time2String : str, optional
            Time string for filtering.
        dsId : int, optional
            DiskStation ID.
        srcType : int, optional
            Source type filter.
        all : bool, optional
            Whether to retrieve all logs.
        blIncludeRecCnt : str, optional
            Include recording count information.
        blIncludeAuInfo : str, optional
            Include additional information.

        Returns
        -------
        dict[str, object] or str
            List of information logs or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_advanced_settings_logs(self) -> dict[str, object] | str:
        """
        Retrieve advanced log settings from Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            Advanced log settings or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def set_advanced_setting_logs(self,
                                  data: Any = None) -> dict[str, object] | str:
        """
        Set advanced log settings in Surveillance Station.

        Parameters
        ----------
        data : Any, optional
            List of log type settings to apply.
            Example:
                data=\\[\\{"SSLogType":321912835,"enable":1\\},\\{"SSLogType":321912836,"enable":0\\}\\]

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetSetting', 'data': data}

        """data example:

           data=[{"SSLogType":321912835,"enable":1},{"SSLogType":321912836,"enable":0}]"""

        return self.request_data(api_name, api_path, req_param)

    def load_license_data(self,
                          # TODO not working
                          num_only: int = None) -> dict[str, object] | str:
        """
        Load license data from Surveillance Station.

        Parameters
        ----------
        num_only : int, optional
            If set, only the number of licenses will be returned.

        Returns
        -------
        dict[str, object] or str
            License data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.License'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Load', 'num_only': num_only}

        return self.request_data(api_name, api_path, req_param)

    def check_license_quota(self,
                            camList: Any = None,
                            # TODO not working
                            camServerId: int = None) -> dict[str, object] | str:
        """
        Check the license quota for cameras in Surveillance Station.

        Parameters
        ----------
        camList : Any, optional
            List of camera information dictionaries.
            Example:
                camList = \\[\\{"ip": "10.13.22.141", "model": "DCS-3110", "vendor": "DLink", "port": 80\\}\\]
        camServerId : int, optional
            Camera server ID.

        Returns
        -------
        dict[str, object] or str
            License quota information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.License'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckQuota'}

        """camList example:

            camList = [{"ip": "10.13.22.141", "model": "DCS-3110", "vendor": "DLink", "port": 80}]"""

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_http_video_stream(self,
                              writeHeader: bool = None,
                              analyevent: bool = None,
                              mountId: int = None) -> dict[str, object] | str:
        """
        Retrieve an HTTP video event stream from Surveillance Station.

        Parameters
        ----------
        writeHeader : bool, optional
            Whether to include headers in the stream.
        analyevent : bool, optional
            Whether to analyze events in the stream.
        mountId : int, optional
            Mount ID for the stream.

        Returns
        -------
        dict[str, object] or str
            Video stream data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Stream'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventStream'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_action_rule(self,
                         id: int = None,
                         name: str = None,
                         ruleType: int = None,
                         actType: int = None,
                         evtSrc: int = None,
                         evtDsId: int = None,
                         evtDevId: int = None,
                         evtId: int = None,
                         evtItem: int = None,
                         evtMinIntvl: int = None,
                         Actions: Any = None,
                         actSchedule: str = None,
                         Id: int = None,
                         actSrc: int = None,
                         actDsId: int = None,
                         actDevId: int = None,
                         actId: int = None,
                         actTimes: int = None,
                         actTimeUnit: int = None,
                         actTimeDur: int = None,
                         actItemId: int = None,
                         actRetPos: int = None,
                         extUrl: str = None,
                         userName: str = None,
                         # TODO not working
                         password: str = None) -> dict[str, object] | str:
        """
        Save or update an action rule in Surveillance Station.

        Parameters
        ----------
        id : int, optional
            Action rule ID.
        name : str, optional
            Name of the action rule.
        ruleType : int, optional
            Type of the rule.
        actType : int, optional
            Action type.
        evtSrc : int, optional
            Event source.
        evtDsId : int, optional
            Event DiskStation ID.
        evtDevId : int, optional
            Event device ID.
        evtId : int, optional
            Event ID.
        evtItem : int, optional
            Event item.
        evtMinIntvl : int, optional
            Minimum interval between events.
        Actions : Any, optional
            List of actions to perform.
        actSchedule : str, optional
            Action schedule.
        Id : int, optional
            Alternative action rule ID.
        actSrc : int, optional
            Action source.
        actDsId : int, optional
            Action DiskStation ID.
        actDevId : int, optional
            Action device ID.
        actId : int, optional
            Action ID.
        actTimes : int, optional
            Number of times to perform the action.
        actTimeUnit : int, optional
            Time unit for the action.
        actTimeDur : int, optional
            Duration for the action.
        actItemId : int, optional
            Action item ID.
        actRetPos : int, optional
            Action return position.
        extUrl : str, optional
            External URL for the action.
        userName : str, optional
            Username for authentication.
        password : str, optional
            Password for authentication. (Currently not working).

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def download_action_rule(self) -> dict[str, object] | str:
        """
        Download the history of action rules from Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            Downloaded action rule history or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'DownloadHistory'}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def send_data_2_player(self) -> dict[str, object] | str:
        """
        Send data to the Surveillance Station player.

        Returns
        -------
        dict[str, object] or str
            Result of the send operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SendData2Player'}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def delete_all_histories_of_action_rule(self, idList: str = None) -> dict[str, object] | str:
        """
        Delete all histories of specified action rules.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of action rule IDs to delete histories for.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'DeleteHistory', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def list_action_rules(self, start: str = None, limit: int = None) -> dict[str, object] | str:
        """
        List action rules in Surveillance Station.

        Parameters
        ----------
        start : str, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of action rules to return.

        Returns
        -------
        dict[str, object] or str
            List of action rules or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'List', 'Start': start, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def disable_action_rules(self, idList: str = None) -> dict[str, object] | str:
        """
        Disable specified action rules in Surveillance Station.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of action rule IDs to disable.

        Returns
        -------
        dict[str, object] or str
            Result of the disable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Disable', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def enable_action_rules(self, idList: str = None) -> dict[str, object] | str:
        """
        Enable specified action rules in Surveillance Station.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of action rule IDs to enable.

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Enable', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def list_history_action_rules(self, start: int = None, limit: int = None) -> dict[str, object] | str:
        """
        List the history of action rules in Surveillance Station.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of history records to return.

        Returns
        -------
        dict[str, object] or str
            List of action rule histories or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ListHistory', 'start': start, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def delete_action_rule(self, idList: str = None) -> dict[str, object] | str:
        """
        Delete specified action rules from Surveillance Station.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of action rule IDs to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'Delete', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def get_list_of_emaps(self,
                          start: int = None,
                          limit: str = None,
                          emapIds: int = None,
                          includeItems: int = None) -> dict[str, object] | str:
        """
        Retrieve a list of eMaps from Surveillance Station.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : str, optional
            Maximum number of eMaps to return.
        emapIds : int, optional
            Specific eMap IDs to retrieve.
        includeItems : int, optional
            Whether to include items in the eMap.

        Returns
        -------
        dict[str, object] or str
            List of eMaps or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Emap'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_specific_emaps_setting(self,
                                   emapIds: int = None,
                                   # TODO to check
                                   includeImage: int = None) -> dict[str, object] | str:
        """
        Retrieve specific eMap settings from Surveillance Station.

        Parameters
        ----------
        emapIds : int, optional
            The ID(s) of the eMap(s) to retrieve settings for.
        includeImage : int, optional
            Whether to include the eMap image in the response.

        Returns
        -------
        dict[str, object] or str
            The eMap settings or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Emap'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_emap_image(self,
                       # TODO to check
                       filename: str = None) -> dict[str, object] | str:
        """
        Retrieve an eMap image from Surveillance Station.

        Parameters
        ----------
        filename : str, optional
            The filename of the eMap image to retrieve.

        Returns
        -------
        dict[str, object] or str
            The eMap image data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Emap.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def get_autorized_ds_token(self) -> dict[str, object] | str:
        """
        Retrieve an authorized DiskStation token for notifications.

        Returns
        -------
        dict[str, object] or str
            The authorized token or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetRegisterToken'}

        return self.request_data(api_name, api_path, req_param)

    def set_message_event(self,
                          eventTypes: str = None,
                          subject: str = None,
                          # TODO not working
                          content: str = None) -> dict[str, object] | str:
        """
        Set a customized message event in Surveillance Station.

        Parameters
        ----------
        eventTypes : str, optional
            The type(s) of event(s) to set the message for.
        subject : str, optional
            The subject of the message.
        content : str, optional
            The content of the message.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetCustomizedMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_message_event(self,
                          # TODO not working
                          eventTypes: int = None) -> dict[str, object] | str:
        """
        Retrieve a customized message event from Surveillance Station.

        Parameters
        ----------
        eventTypes : int, optional
            The type(s) of event(s) to retrieve the message for.

        Returns
        -------
        dict[str, object] or str
            The message event data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetCustomizedMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_notification_sender_name(self,
                                     # TODO not working
                                     ss_pkg_name: str = None) -> dict[str, object] | str:
        """
        Set the sender name for Surveillance Station notifications.

        Parameters
        ----------
        ss_pkg_name : str, optional
            The sender name to set.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetVariables'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def get_notification_sender_name(self) -> dict[str, object] | str:
        """
        Retrieve the sender name for Surveillance Station notifications.

        Returns
        -------
        dict[str, object] or str
            The sender name or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetVariables'}

        return self.request_data(api_name, api_path, req_param)

    def set_advanced_notification_setting(self,
                                          blSyncDSMNotify: bool = None,
                                          # TODO to check
                                          blCompactMsg: bool = None) -> dict[str, object] | str:
        """
        Set advanced notification settings in Surveillance Station.

        Parameters
        ----------
        blSyncDSMNotify : bool, optional
            Whether to synchronize DSM notifications.
        blCompactMsg : bool, optional
            Whether to enable compact message format.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetAdvSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def get_advanced_notification_setting(self) -> dict[str, object] | str:
        """
        Retrieve advanced notification settings from Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            The advanced notification settings or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetAdvSetting'}

        return self.request_data(api_name, api_path, req_param)

    def send_test_mesg_to_primary_secondary_phone(self,
                                                  smsEnable: bool = None,
                                                  smsMethod: int = None,
                                                  smsProvider: str = None,
                                                  userName: str = None,
                                                  password: str = None,
                                                  confirmPassword: str = None,
                                                  primaryPhoneCode: str = None,
                                                  primaryPhonePrefix: str = None,
                                                  secondaryPhoneCode: str = None,
                                                  secondaryPhonePrefix: str = None,
                                                  secondaryPhoneNumber: str = None,
                                                  setMinMessageInterval: bool = None,
                                                  minMessageInterval: int = None,
                                                  hasSysSms: bool = None,
                                                  # TODO to check
                                                  apiId: str = None) -> dict[str, object] | str:
        """
        Send a test message to the primary and secondary phone numbers via SMS.

        Parameters
        ----------
        smsEnable : bool, optional
            Whether SMS notifications are enabled.
        smsMethod : int, optional
            The SMS sending method.
        smsProvider : str, optional
            The SMS provider name.
        userName : str, optional
            Username for SMS provider authentication.
        password : str, optional
            Password for SMS provider authentication.
        confirmPassword : str, optional
            Confirmation of the password.
        primaryPhoneCode : str, optional
            Country code for the primary phone.
        primaryPhonePrefix : str, optional
            Prefix for the primary phone.
        secondaryPhoneCode : str, optional
            Country code for the secondary phone.
        secondaryPhonePrefix : str, optional
            Prefix for the secondary phone.
        secondaryPhoneNumber : str, optional
            The secondary phone number.
        setMinMessageInterval : bool, optional
            Whether to set a minimum message interval.
        minMessageInterval : int, optional
            The minimum interval between messages.
        hasSysSms : bool, optional
            Whether system SMS is enabled.
        apiId : str, optional
            The API ID for the SMS provider.

        Returns
        -------
        dict[str, object] or str
            Result of the test message operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SendTestMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_setting_notification_sms(self) -> dict[str, object] | str:
        """
        Retrieve the SMS notification settings from Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            The SMS notification settings or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def set_sms_service_setting(self,
                                smsEnable: bool = None,
                                smsMethod: int = None,
                                smsProvider: str = None,
                                userName: str = None,
                                password: str = None,
                                confirmPassword: str = None,
                                primaryPhoneCode: str = None,
                                primaryPhonePrefix: str = None,
                                secondaryPhoneCode: str = None,
                                secondaryPhonePrefix: str = None,
                                secondaryPhoneNumber: str = None,
                                setMinMessageInterval: bool = None,
                                minMessageInterval: int = None,
                                hasSysSms: bool = None,
                                apiId: str = None) -> dict[str, object] | str:
        """
        Set the SMS service settings for Surveillance Station notifications.

        Parameters
        ----------
        smsEnable : bool, optional
            Whether SMS notifications are enabled.
        smsMethod : int, optional
            The SMS sending method.
        smsProvider : str, optional
            The SMS provider name.
        userName : str, optional
            Username for SMS provider authentication.
        password : str, optional
            Password for SMS provider authentication.
        confirmPassword : str, optional
            Confirmation of the password.
        primaryPhoneCode : str, optional
            Country code for the primary phone.
        primaryPhonePrefix : str, optional
            Prefix for the primary phone.
        secondaryPhoneCode : str, optional
            Country code for the secondary phone.
        secondaryPhonePrefix : str, optional
            Prefix for the secondary phone.
        secondaryPhoneNumber : str, optional
            The secondary phone number.
        setMinMessageInterval : bool, optional
            Whether to set a minimum message interval.
        minMessageInterval : int, optional
            The minimum interval between messages.
        hasSysSms : bool, optional
            Whether system SMS is enabled.
        apiId : str, optional
            The API ID for the SMS provider.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def send_test_sms(self,
                      attachSnapshot: bool = None,
                      enableInterval: bool = None,
                      mobileEnable: bool = None,
                      msgInterval: str = None,
                      primaryEmail: str = None,
                      secondaryEmail: str = None,
                      synoMailEnable: bool = None,
                      # TODO to check
                      mail_recipient: str = None) -> dict[str, object] | str:
        """
        Send a test SMS notification from Surveillance Station.

        Parameters
        ----------
        attachSnapshot : bool, optional
            Whether to attach a snapshot to the SMS.
        enableInterval : bool, optional
            Whether to enable message interval.
        mobileEnable : bool, optional
            Whether to enable mobile notifications.
        msgInterval : str, optional
            The interval between messages.
        primaryEmail : str, optional
            The primary email address for notifications.
        secondaryEmail : str, optional
            The secondary email address for notifications.
        synoMailEnable : bool, optional
            Whether to enable Synology Mail notifications.
        mail_recipient : str, optional
            The recipient of the test mail.

        Returns
        -------
        dict[str, object] or str
            Result of the test SMS operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SendTestMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def send_test_mail(self,
                       attachSnapshot: bool = None,
                       enableInterval: bool = None,
                       mobileEnable: bool = None,
                       msgInterval: str = None,
                       primaryEmail: str = None,
                       secondaryEmail: str = None,
                       synoMailEnable: bool = None,
                       # TODO to check
                       mail_recipient: str = None) -> dict[str, object] | str:
        """
        Send a test verification mail for Surveillance Station notifications.

        Parameters
        ----------
        attachSnapshot : bool, optional
            Whether to attach a snapshot to the email.
        enableInterval : bool, optional
            Whether to enable message interval.
        mobileEnable : bool, optional
            Whether to enable mobile notifications.
        msgInterval : str, optional
            The interval between messages.
        primaryEmail : str, optional
            The primary email address for notifications.
        secondaryEmail : str, optional
            The secondary email address for notifications.
        synoMailEnable : bool, optional
            Whether to enable Synology Mail notifications.
        mail_recipient : str, optional
            The recipient of the test mail.

        Returns
        -------
        dict[str, object] or str
            Result of the test mail operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.PushService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SendVerificationMail'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_mobile_paired_devices(self,
                                   attachSnapshot: bool = None,
                                   enableInterval: bool = None,
                                   mobileEnable: bool = None,
                                   msgInterval: str = None,
                                   primaryEmail: str = None,
                                   secondaryEmail: str = None,
                                   synoMailEnable: bool = None,
                                   mail_recipient: str = None) -> dict[str, object] | str:
        """
        List mobile devices paired with Surveillance Station for push notifications.

        Parameters
        ----------
        attachSnapshot : bool, optional
            Whether to attach a snapshot to the notification.
        enableInterval : bool, optional
            Whether to enable message interval.
        mobileEnable : bool, optional
            Whether to enable mobile notifications.
        msgInterval : str, optional
            The interval between messages.
        primaryEmail : str, optional
            The primary email address for notifications.
        secondaryEmail : str, optional
            The secondary email address for notifications.
        synoMailEnable : bool, optional
            Whether to enable Synology Mail notifications.
        mail_recipient : str, optional
            The recipient of the notification.

        Returns
        -------
        dict[str, object] or str
            List of paired mobile devices or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.PushService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ListMobileDevice'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unpair_device(self,
                      targetIds: str = None) -> dict[str, object] | str:
        """
        Unpair a mobile device from Surveillance Station notifications.

        Parameters
        ----------
        targetIds : str, optional
            The ID(s) of the device(s) to unpair.

        Returns
        -------
        dict[str, object] or str
            Result of the unpair operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.PushService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_controller_access_schedule(self,
                                       # TODO to check
                                       targetIds: str = None) -> dict[str, object] | str:
        """
        Retrieve the access control controller schedule from Surveillance Station.

        Parameters
        ----------
        targetIds : str, optional
            The ID(s) of the controllers to retrieve the schedule for.

        Returns
        -------
        dict[str, object] or str
            The controller access schedule or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetAccessControlControllerSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_alarm_schedule(self,
                                  cameraId: int = None,
                                  # TODO to check
                                  alarmdx: int = None) -> dict[str, object] | str:
        """
        Retrieve the alarm schedule for a specific camera.

        Parameters
        ----------
        cameraId : int, optional
            The ID of the camera.
        alarmdx : int, optional
            Additional alarm parameter (to check).

        Returns
        -------
        dict[str, object] or str
            The camera alarm schedule or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetCameraAlarmSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_sys_dependent_schedule(self,
                                   # TODO to check
                                   eventGroupTypes: int = None) -> dict[str, object] | str:
        """
        Retrieve the system dependent schedule for Surveillance Station events.

        Parameters
        ----------
        eventGroupTypes : int, optional
            The type(s) of event groups to retrieve the schedule for.

        Returns
        -------
        dict[str, object] or str
            The system dependent schedule or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetSystemDependentSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_batch_schedule(self,
                           eventTypes: str = None,
                           schedule: Any = None,
                           cameraIds: str = None,
                           cameraGroupIds: str = None,
                           # TODO to check
                           filter: int = None) -> dict[str, object] | str:
        """
        Set batch schedules for events, cameras, or camera groups.

        Parameters
        ----------
        eventTypes : str, optional
            The type(s) of events to schedule.
        schedule : Any, optional
            The schedule data to apply.
        cameraIds : str, optional
            The IDs of cameras to apply the schedule to.
        cameraGroupIds : str, optional
            The IDs of camera groups to apply the schedule to.
        filter : int, optional
            Additional filter parameter (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the batch schedule operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetBatchSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_access_ctrl_door_schedule(self,
                                      # TODO to check
                                      doorId: str = None) -> dict[str, object] | str:
        """
        Retrieve the access control door schedule from Surveillance Station.

        Parameters
        ----------
        doorId : str, optional
            The ID of the door to retrieve the schedule for.

        Returns
        -------
        dict[str, object] or str
            The door schedule or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetAccessControlDoorSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_schedule(self,
                            # TODO to check
                            cameraId: str = None) -> dict[str, object] | str:
        """
        Retrieve the schedule for a specific camera.

        Parameters
        ----------
        cameraId : str, optional
            The ID of the camera to retrieve the schedule for.

        Returns
        -------
        dict[str, object] or str
            The camera schedule or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetCameraSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_sys_dependent_schedule(self,
                                   eventType: int = None,
                                   # TODO to check
                                   schedule: Any = None) -> dict[str, object] | str:
        """
        Set the system dependent schedule for Surveillance Station events.

        Parameters
        ----------
        eventType : int, optional
            The type of event to set the schedule for.
        schedule : Any, optional
            The schedule data to apply.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetSystemDependentSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_controller_access_schedule(self,
                                       eventType: int = None,
                                       schedule: Any = None,
                                       # TODO to check
                                       doorId: int = None) -> dict[str, object] | str:
        """
        Set the access control schedule for a controller or door.

        Parameters
        ----------
        eventType : int, optional
            The type of event to set the schedule for.
        schedule : Any, optional
            The schedule data to apply.
        doorId : int, optional
            The ID of the door to set the schedule for.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetAccessControlSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_camera_schedule(self,
                            eventType: int = None,
                            schedule: Any = None,
                            # TODO to check
                            cameraId: Any = None) -> dict[str, object] | str:
        """
        Set the schedule for a specific camera in Surveillance Station.

        Parameters
        ----------
        eventType : int, optional
            The type of event to set the schedule for.
        schedule : Any, optional
            The schedule data to apply.
        cameraId : Any, optional
            The ID of the camera to set the schedule for.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SetCameraSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_notification_email_string(self) -> dict[str, object] | str:
        """
        Retrieve the notification email settings string from Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            The notification email settings or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Email'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def set_adv_tab_info_filter(self,
                                # TODO to check
                                X: int = None) -> dict[str, object] | str:
        """
        Set the advanced tab information filter for notification emails.

        Parameters
        ----------
        X : int, optional
            The filter value to set (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.Email'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Set'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_sms_service_provider(self,
                                    providerName: str = None,
                                    providerPort: int = None,
                                    providerUrl: str = None,
                                    providerTemplate: str = None,
                                    providerSepChar: str = None,
                                    providerNeedSSL: bool = None) -> dict[str, object] | str:
        """
        Create a new SMS service provider for Surveillance Station notifications.

        Parameters
        ----------
        providerName : str, optional
            The name of the SMS provider.
        providerPort : int, optional
            The port used by the provider.
        providerUrl : str, optional
            The URL of the provider.
        providerTemplate : str, optional
            The message template for the provider.
        providerSepChar : str, optional
            The separator character used by the provider.
        providerNeedSSL : bool, optional
            Whether SSL is required for the provider.

        Returns
        -------
        dict[str, object] or str
            Result of the create operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS.ServiceProvider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_sms_provider(self) -> dict[str, object] | str:
        """
        List all SMS service providers configured in Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            List of SMS providers or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS.ServiceProvider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        return self.request_data(api_name, api_path, req_param)

    def delete_sms_service_provider(self,
                                    # TODO to check
                                    providerName: str = None) -> dict[str, object] | str:
        """
        Delete an SMS service provider from Surveillance Station.

        Parameters
        ----------
        providerName : str, optional
            The name of the SMS provider to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Notification.SMS.ServiceProvider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_addson_to_update(self) -> dict[str, object] | str:
        """
        Retrieve information about add-ons that require updates in Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            Add-on update information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetUpdateInfo'}

        return self.request_data(api_name, api_path, req_param)

    def enable_specific_addon(self,
                              service: int = None,
                              # TODO to check
                              servicename: str = None) -> dict[str, object] | str:
        """
        Enable a specific add-on in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to enable.
        servicename : str, optional
            The name of the add-on service to enable.

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_specific_addon_update_info(self,
                                       # TODO to check
                                       service: int = None) -> dict[str, object] | str:
        """
        Retrieve update information for a specific add-on in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to check for updates.

        Returns
        -------
        dict[str, object] or str
            Update information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CheckUpdateInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_specific_addon_info(self,
                                # TODO to check
                                service: int = None) -> dict[str, object] | str:
        """
        Retrieve information for a specific add-on in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to retrieve information for.

        Returns
        -------
        dict[str, object] or str
            Add-on information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_total_addon_info(self) -> dict[str, object] | str:  # TODO to check
        """
        Retrieve information about all add-ons in Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            List of all add-ons or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        return self.request_data(api_name, api_path, req_param)

    def update_addon_package(self,
                             service: int = None,
                             # TODO to check
                             filePath: str = None) -> dict[str, object] | str:
        """
        Update an add-on package in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to update.
        filePath : str, optional
            The file path to the add-on package (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the update operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Update'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_addon_status(self,
                           # TODO to check
                           service: int = None) -> dict[str, object] | str:
        """
        Check the enable status of a specific add-on in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to check (to check).

        Returns
        -------
        dict[str, object] or str
            Status information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CheckEnableDone'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_addon(self,
                      service: int = None,
                      # TODO to check
                      serviceName: str = None) -> dict[str, object] | str:
        """
        Disable a specific add-on in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to disable.
        serviceName : str, optional
            The name of the add-on service to disable (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the disable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_addon_autoupdate(self,
                             service: int = None,
                             # TODO to check
                             BlEnabled: Any = None) -> dict[str, object] | str:
        """
        Set the auto-update setting for a specific add-on in Surveillance Station.

        Parameters
        ----------
        service : int, optional
            The ID of the add-on service to configure.
        BlEnabled : Any, optional
            Whether auto-update is enabled (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetAutoUpdate'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_camera_recording_server(self,
                                                # TODO to check
                                                camIdList: str = None) -> dict[str, object] | str:
        """
        Delete a specific camera recording server in Surveillance Station.

        Parameters
        ----------
        camIdList : str, optional
            List of camera IDs to delete from the recording server (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RecServClear'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_event_analytic(self,
                                  # TODO to check
                                  camIdList: str = None) -> dict[str, object] | str:
        """
        Retrieve camera event analytics from Surveillance Station.

        Parameters
        ----------
        camIdList : str, optional
            List of camera IDs to retrieve analytics for (to check).

        Returns
        -------
        dict[str, object] or str
            Analytics data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_selected_events(self,
                               dsIdList: str = None,
                               # TODO to check
                               idList: str = None) -> dict[str, object] | str:
        """
        Delete selected events from Surveillance Station.

        Parameters
        ----------
        dsIdList : str, optional
            List of DS IDs for which to delete events.
        idList : str, optional
            List of event IDs to delete (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ClearSelected'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_camera_events(self,
                                      # TODO to check
                                      camIdList: str = None) -> dict[str, object] | str:
        """
        Delete events for specific cameras in Surveillance Station.

        Parameters
        ----------
        camIdList : str, optional
            List of camera IDs for which to delete events (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_analytic_history(self,
                             camIdList: str = None,
                             # TODO to check
                             typeListstring: str = None) -> dict[str, object] | str:
        """
        Retrieve analytic history for cameras in Surveillance Station.

        Parameters
        ----------
        camIdList : str, optional
            List of camera IDs to retrieve history for.
        typeListstring : str, optional
            List of analytic types as a string (to check).

        Returns
        -------
        dict[str, object] or str
            Analytic history data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_analytic_history_by_filter(self,
                                       camIdList: str = None,
                                       dsId: int = None,
                                       lock: int = None,
                                       # TODO to check
                                       typeList: str = None) -> dict[str, object] | str:
        """
        Retrieve analytic history for cameras by filter in Surveillance Station.

        Parameters
        ----------
        camIdList : str, optional
            List of camera IDs to filter.
        dsId : int, optional
            The DS ID to filter.
        lock : int, optional
            Lock status to filter.
        typeList : str, optional
            List of analytic types as a string (to check).

        Returns
        -------
        dict[str, object] or str
            Filtered analytic history data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RecServerEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unklock_selected_events(self,
                                dsId: int = None,
                                # TODO to check
                                idList: str = None) -> dict[str, object] | str:
        """
        Unlock selected events in Surveillance Station.

        Parameters
        ----------
        dsId : int, optional
            The DS ID for which to unlock events.
        idList : str, optional
            List of event IDs to unlock (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_camera_analytic_trigger(self,
                                    # TODO to check
                                    trigCamIdList: str = None) -> dict[str, object] | str:
        """
        Trigger camera analytics for specified cameras in Surveillance Station.

        Parameters
        ----------
        trigCamIdList : str, optional
            List of camera IDs to trigger analytics for (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the trigger operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Trigger'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def flush_event_header(self,
                           # TODO to check
                           eventId: str = None) -> dict[str, object] | str:
        """
        Flush the header of a specific event in Surveillance Station.

        Parameters
        ----------
        eventId : str, optional
            The ID of the event to flush the header for (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the flush operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'EventFlushHeader'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_selected_events(self,
                             dsId: int = None,
                             # TODO to check
                             idList: str = None) -> dict[str, object] | str:
        """
        Lock selected events in Surveillance Station.

        Parameters
        ----------
        dsId : int, optional
            The DS ID for which to lock events.
        idList : str, optional
            List of event IDs to lock (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the lock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_analytic_event_from_rec_server(self,
                                           camIdList: str = None,
                                           # TODO to check
                                           idList: int = None) -> dict[str, object] | str:
        """
        Retrieve analytic event counts from the recording server for specified cameras.

        Parameters
        ----------
        camIdList : str, optional
            Comma-separated list of camera IDs to query.
        idList : int, optional
            Additional ID list parameter (to check).

        Returns
        -------
        dict[str, object] or str
            Analytic event count data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'RecServerEventCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_analytic_settings(self,
                               camId: int = None,
                               type: int = None,
                               showFrame: bool = None,
                               showLine: bool = None,
                               showVirtualFence: bool = None,
                               beep: bool = None,
                               sens: int = None,
                               dwellTime: int = None,
                               direction: int = None,
                               objSize: int = None,
                               # TODO to check
                               region: str = None) -> dict[str, object] | str:
        """
         Save analytic settings for a specific camera.

         Parameters
         ----------
         camId : int, optional
             Camera ID to apply settings to.
         type : int, optional
             Type of analytic.
         showFrame : bool, optional
             Whether to display the frame.
         showLine : bool, optional
             Whether to display lines.
         showVirtualFence : bool, optional
             Whether to display virtual fences.
         beep : bool, optional
             Whether to enable beep on event.
         sens : int, optional
             Sensitivity setting.
         dwellTime : int, optional
             Dwell time setting.
         direction : int, optional
             Direction setting.
         objSize : int, optional
             Object size setting.
         region : str, optional
             Region definition (to check).

         Returns
         -------
         dict[str, object] or str
             Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Alert.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_if_snapshot_exist(self,
                                # TODO to check
                                id: int = None) -> dict[str, object] | str:
        """
        Check if a snapshot exists for a given ID.

        Parameters
        ----------
        id : int, optional
            Snapshot ID to check (to check).

        Returns
        -------
        dict[str, object] or str
            Existence status or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ChkFileExist'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_snapshot_modification(self,
                                   id: int = None,
                                   createCopy: bool = None,
                                   width: int = None,
                                   height: int = None,
                                   byteSize: int = None,
                                   # TODO to check
                                   imageData: str = None) -> dict[str, object] | str:
        """
        Save modifications to a snapshot.

        Parameters
        ----------
        id : int, optional
            Snapshot ID to modify.
        createCopy : bool, optional
            Whether to create a copy of the snapshot.
        width : int, optional
            Width of the snapshot.
        height : int, optional
            Height of the snapshot.
        byteSize : int, optional
            Size of the snapshot in bytes.
        imageData : str, optional
            Image data (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the modification or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Edit'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_snapshot_by_category(self,
                                   keyword: str = None,
                                   dsfrom: int = None,
                                   to: int = None,
                                   timezoneOffset: int = None,
                                   byteSize: int = None,
                                   # TODO to check
                                   imageData: str = None) -> dict[str, object] | str:
        """
        Count snapshots by category within a specified range.

        Parameters
        ----------
        keyword : str, optional
            Keyword to filter snapshots.
        dsfrom : int, optional
            Start timestamp.
        to : int, optional
            End timestamp.
        timezoneOffset : int, optional
            Timezone offset.
        byteSize : int, optional
            Size of the snapshot in bytes.
        imageData : str, optional
            Image data (to check).

        Returns
        -------
        dict[str, object] or str
            Count data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_any_locked_snapshot(self,
                                  id: str = None,
                                  dsfrom: int = None,
                                  to: int = None,
                                  # TODO to check
                                  keyword: str = None) -> dict[str, object] | str:
        """
        Check if any locked snapshots exist within a specified range.

        Parameters
        ----------
        id : str, optional
            Snapshot ID(s) to check.
        dsfrom : int, optional
            Start timestamp.
        to : int, optional
            End timestamp.
        keyword : str, optional
            Keyword to filter snapshots (to check).

        Returns
        -------
        dict[str, object] or str
            Lock status or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ChkContainLocked'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_snapshot_by_filter(self,
                                  dsfrom: int = None,
                                  to: int = None,
                                  # TODO to check
                                  keyword: str = None) -> dict[str, object] | str:
        """
        Unlock snapshots by filter within a specified range.

        Parameters
        ----------
        dsfrom : int, optional
            Start timestamp.
        to : int, optional
            End timestamp.
        keyword : str, optional
            Keyword to filter snapshots (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'UnlockFiltered'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_snapshot_information(self,
                                  idList: str = None,
                                  start: int = None,
                                  limit: int = None,
                                  dsfrom: int = None,
                                  to: int = None,
                                  keyword: str = None,
                                  imgSize: int = None,
                                  blIncludeAuInfo: bool = None,
                                  blIncludeRecCnt: bool = None,
                                  # TODO to check
                                  camId: int = None) -> dict[str, object] | str:
        """
        List snapshot information with optional filters.

        Parameters
        ----------
        idList : str, optional
            Comma-separated list of snapshot IDs.
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        dsfrom : int, optional
            Start timestamp.
        to : int, optional
            End timestamp.
        keyword : str, optional
            Keyword to filter snapshots.
        imgSize : int, optional
            Image size filter.
        blIncludeAuInfo : bool, optional
            Whether to include additional info.
        blIncludeRecCnt : bool, optional
            Whether to include recording count.
        camId : int, optional
            Camera ID filter (to check).

        Returns
        -------
        dict[str, object] or str
            List of snapshot information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_snapshot(self,
                        # TODO to check
                        objList: Any = None) -> dict[str, object] | str:
        """
        Unlock specific snapshots.

        Parameters
        ----------
        objList : Any, optional
            List of snapshot objects to unlock (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def take_snapshot(self,
                      dsId: int = None,
                      camId: int = None,
                      # TODO to check
                      blSave: bool = None) -> dict[str, object] | str:
        """
        Take a snapshot for a specific camera and DS.

        Parameters
        ----------
        dsId : int, optional
            DS ID for the snapshot.
        camId : int, optional
            Camera ID for the snapshot.
        blSave : bool, optional
            Whether to save the snapshot (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the snapshot operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TakeSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def get_snapshot_setting_function(self) -> dict[str, object] | str:
        """
        Retrieve the snapshot setting function.

        Returns
        -------
        dict[str, object] or str
            Snapshot setting information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def delete_snapshot_by_filter(self,
                                  deleteAllCommand: bool = None,
                                  dsfrom: int = None,
                                  to: int = None,
                                  # TODO to check
                                  keyword: str = None) -> dict[str, object] | str:
        """
        Delete snapshots by filter within a specified range.

        Parameters
        ----------
        deleteAllCommand : bool, optional
            Whether to delete all snapshots.
        dsfrom : int, optional
            Start timestamp.
        to : int, optional
            End timestamp.
        keyword : str, optional
            Keyword to filter snapshots (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteFiltered'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_snapshot_image(self,
                           id: int = None,
                           # TODO to modify for download?
                           imgSize: int = None) -> dict[str, object] | str:
        """
        Retrieve a snapshot image by ID.

        Parameters
        ----------
        id : int, optional
            Snapshot ID to retrieve.
        imgSize : int, optional
            Image size (to modify for download?).

        Returns
        -------
        dict[str, object] or str
            Snapshot image data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LoadSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_snapshot_image(self,
                            objList: Any = None) -> dict[str, object] | str:
        """
        Lock specific snapshot images.

        Parameters
        ----------
        objList : Any, optional
            List of snapshot objects to lock.

        Returns
        -------
        dict[str, object] or str
            Result of the lock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO: fix typo
    def downld_single_snapshot(self,
                               # TODO not working
                               id: int = None) -> dict[str, object] | str:
        """
        Download a single snapshot by ID.

        Parameters
        ----------
        id : int, optional
            Snapshot ID to download (not working).

        Returns
        -------
        dict[str, object] or str
            Download result or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Download'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_new_snapshot_setting(self,
                                  dispSnapshot: bool = None,
                                  dispDuration: int = None,
                                  limitTotalSize: bool = None,
                                  limitSizeInGb: int = None,
                                  addTimestamp: bool = None,
                                  timestampPosition: int = None) -> dict[str, object] | str:
        """
        Save new snapshot settings.

        Parameters
        ----------
        dispSnapshot : bool, optional
            Whether to display snapshots.
        dispDuration : int, optional
            Display duration for snapshots.
        limitTotalSize : bool, optional
            Whether to limit total snapshot size.
        limitSizeInGb : int, optional
            Limit size in GB.
        addTimestamp : bool, optional
            Whether to add a timestamp to snapshots.
        timestampPosition : int, optional
            Position of the timestamp.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_snapshot(self,
                      camName: str = None,
                      createdTm: int = None,
                      width: int = None,
                      height: int = None,
                      byteSize: int = None,
                      # TODO to check
                      imageData: str = None) -> dict[str, object] | str:
        """
        Save a new snapshot.

        Parameters
        ----------
        camName : str, optional
            Name of the camera.
        createdTm : int, optional
            Creation timestamp.
        width : int, optional
            Width of the snapshot.
        height : int, optional
            Height of the snapshot.
        byteSize : int, optional
            Size of the snapshot in bytes.
        imageData : str, optional
            Image data (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_snapshot_status(self,
                              dispSnapshot: bool = None) -> dict[str, object] | str:
        """
        Check the status of snapshot display.

        Parameters
        ----------
        dispSnapshot : bool, optional
            Whether to display snapshots.

        Returns
        -------
        dict[str, object] or str
            Status information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ChkSnapshotValid'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_visualstation(self,
                             # TODO to check
                             vslist: str = None) -> dict[str, object] | str:
        """
        Enable VisualStation devices.

        Parameters
        ----------
        vslist : str, optional
            Comma-separated list of VisualStation IDs to enable (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def update_vs_network_config(self,
                                 vsMAc: str = None,
                                 ip: str = None,
                                 mask: str = None,
                                 gateway: str = None,
                                 blDhcp: bool = None,
                                 # TODO to check
                                 name: str = None) -> dict[str, object] | str:
        """
        Update the network configuration for a VisualStation device.

        Parameters
        ----------
        vsMAc : str, optional
            MAC address of the VisualStation.
        ip : str, optional
            IP address to assign.
        mask : str, optional
            Subnet mask.
        gateway : str, optional
            Gateway address.
        blDhcp : bool, optional
            Whether to use DHCP.
        name : str, optional
            Name of the VisualStation (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the update operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ReqNetConfig'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_visualstation_by_id(self,
                                 # TODO to check
                                 vslist: str = None) -> dict[str, object] | str:
        """
        Lock VisualStation devices by ID.

        Parameters
        ----------
        vslist : str, optional
            Comma-separated list of VisualStation IDs to lock (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the lock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def enumerate_vs_owner_info(self) -> dict[str, object] | str:
        """
        Enumerate VisualStation owner information.

        Returns
        -------
        dict[str, object] or str
            Owner information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        return self.request_data(api_name, api_path, req_param)

    def unlock_visualstation_by_id(self,
                                   # TODO to check
                                   vslist: str = None) -> dict[str, object] | str:
        """
        Unlock VisualStation devices by ID.

        Parameters
        ----------
        vslist : str, optional
            Comma-separated list of VisualStation IDs to unlock (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_visualstation_by_id(self,
                                    # TODO to check
                                    vslist: str = None) -> dict[str, object] | str:
        """
        Disable VisualStation devices by ID.

        Parameters
        ----------
        vslist : str, optional
            Comma-separated list of VisualStation IDs to disable (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the disable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_visualstation(self,
                                      # TODO to check
                                      vslist: str = None) -> dict[str, object] | str:
        """
        Delete specific VisualStation devices by ID.

        Parameters
        ----------
        vslist : str, optional
            Comma-separated list of VisualStation IDs to delete (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_layout_visualstation(self,
                                       # TODO to check
                                       vsId: int = None) -> dict[str, object] | str:
        """
        Enumerate VisualStation layouts.

        Parameters
        ----------
        vsId : int, optional
            VisualStation ID to filter layouts (to check).

        Returns
        -------
        dict[str, object] or str
            Layout information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_layout_information(self,
                                id: int = None,
                                vsId: int = None,
                                name: str = None,
                                canGrpId: int = None,
                                isDefault: int = None,
                                isFixAspectRatio: int = None,
                                layoutType: int = None,
                                channelList: Any = None,
                                # TODO to check
                                customPosList: str = None) -> dict[str, object] | str:
        """
        Save layout information for a VisualStation.

        Parameters
        ----------
        id : int, optional
            Layout ID.
        vsId : int, optional
            VisualStation ID.
        name : str, optional
            Name of the layout.
        canGrpId : int, optional
            Camera group ID.
        isDefault : int, optional
            Whether this is the default layout.
        isFixAspectRatio : int, optional
            Whether to fix the aspect ratio.
        layoutType : int, optional
            Type of the layout.
        channelList : Any, optional
            List of channels in the layout.
        customPosList : str, optional
            Custom position list (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_layout_visualstation(self,
                                    id: int = None,
                                    # TODO to check
                                    vsId: int = None) -> dict[str, object] | str:
        """
        Delete a VisualStation layout.

        Parameters
        ----------
        id : int, optional
            Layout ID to delete.
        vsId : int, optional
            VisualStation ID (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def clear_visualstation_search_result(self) -> dict[str, object] | str:
        """
        Clear VisualStation search results.

        Returns
        -------
        dict[str, object] or str
            Result of the clear operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        return self.request_data(api_name, api_path, req_param)

    def get_visualstation_ip_info(self,
                                  # TODO to check
                                  ip: int = None) -> dict[str, object] | str:
        """
        Retrieve VisualStation IP information.

        Parameters
        ----------
        ip : int, optional
            IP address to search for (to check).

        Returns
        -------
        dict[str, object] or str
            IP information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SearchIP'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def stop_previous_visualstation_search(self) -> dict[str, object] | str:
        """
        Stop the previous VisualStation search operation.

        Returns
        -------
        dict[str, object] or str
            Result of the stop operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Stop'}

        return self.request_data(api_name, api_path, req_param)

    def get_visualstation_list(self,
                               # TODO to check
                               offset: int = None) -> dict[str, object] | str:
        """
        Retrieve the list of VisualStation devices.

        Parameters
        ----------
        offset : int, optional
            Offset for pagination (to check).

        Returns
        -------
        dict[str, object] or str
            List of VisualStation devices or error details.
        """
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'InfoGet'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_number_of_controller(self) -> dict[str, object] | str:
        """
        Get the number of controllers in the system.

        Returns
        -------
        dict[str, object] or str
            Number of controllers or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetUpdateInfo'}

        return self.request_data(api_name, api_path, req_param)

    def get_cardholder_count(self, filterKeyword: str = None) -> dict[str, object] | str:
        """
        Get the count of cardholders, optionally filtered by keyword.

        Parameters
        ----------
        filterKeyword : str, optional
            Keyword to filter cardholders.

        Returns
        -------
        dict[str, object] or str
            Cardholder count or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategoryCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_all_controllers_logger(self) -> dict[str, object] | str:
        """
        Enumerate all controller logger configurations.

        Returns
        -------
        dict[str, object] or str
            Logger configuration information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumLogConfig'}

        return self.request_data(api_name, api_path, req_param)

    def get_cardholder_photo(self,
                             photo_name: str = None,
                             # TODO to check
                             isRedirectCgi: bool = None) -> dict[str, object] | str:
        """
        Retrieve a cardholder's photo.

        Parameters
        ----------
        photo_name : str, optional
            Name of the photo file.
        isRedirectCgi : bool, optional
            Whether to redirect to CGI for the photo (to check).

        Returns
        -------
        dict[str, object] or str
            Photo data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetCardholderPhoto'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_log_count(self,
                      start: int = None,
                      limit: int = None,
                      filterType: int = None,
                      filterEventSource: Any = None,
                      filterSource: int = None,
                      filterEventSourceItem: int = None,
                      filterTimeFrom: int = None,
                      filterTimeTo: int = None,
                      filterKeyword: str = None,
                      timezoneOffset: int = None,
                      doorIds: str = None,
                      eventTypes: str = None,
                      update: int = None) -> dict[str, object] | str:
        """
        Get the count of logs with optional filters.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        filterType : int, optional
            Type of filter to apply.
        filterEventSource : Any, optional
            Event source filter.
        filterSource : int, optional
            Source filter.
        filterEventSourceItem : int, optional
            Event source item filter.
        filterTimeFrom : int, optional
            Start time for filtering.
        filterTimeTo : int, optional
            End time for filtering.
        filterKeyword : str, optional
            Keyword to filter logs.
        timezoneOffset : int, optional
            Timezone offset.
        doorIds : str, optional
            Door IDs filter.
        eventTypes : str, optional
            Event types filter.
        update : int, optional
            Update flag.

        Returns
        -------
        dict[str, object] or str
            Log count or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategoryLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_cardholder_info(self,
                            start: int = None,
                            limit: int = None,
                            filterKeyword: str = None,
                            filterStatus: int = None,
                            filterCtrlerId: int = None) -> dict[str, object] | str:
        """
        Retrieve cardholder information with optional filters.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        filterKeyword : str, optional
            Keyword to filter cardholders.
        filterStatus : int, optional
            Status filter.
        filterCtrlerId : int, optional
            Controller ID filter.

        Returns
        -------
        dict[str, object] or str
            Cardholder information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def retrieve_last_access_credential(self,
                                        ctrlerId: int = None,
                                        # TODO to check
                                        idPtId: int = None) -> dict[str, object] | str:
        """
        Retrieve the last access credential for a controller.

        Parameters
        ----------
        ctrlerId : int, optional
            Controller ID.
        idPtId : int, optional
            ID/point ID (to check).

        Returns
        -------
        dict[str, object] or str
            Last access credential information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'RetrieveLastCard'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_disable_controller(self,
                                  blEnable: bool = None,
                                  arrayJson: str = None) -> dict[str, object] | str:
        """
        Enable or disable controllers.

        Parameters
        ----------
        blEnable : bool, optional
            Whether to enable (True) or disable (False) controllers.
        arrayJson : str, optional
            JSON array of controller IDs.

        Returns
        -------
        dict[str, object] or str
            Result of the operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableCtrler'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def acknowledge_all_alarm_level_log(self,
                                        start: int = None,
                                        limit: int = None,
                                        filterEventSource: Any = None,
                                        filterSource: int = None,
                                        filterEventSourceItem: str = None,
                                        filterTimeFrom: int = None,
                                        filterKeyword: str = None,
                                        doorIds: str = None,
                                        eventTypes: str = None,
                                        update: int = None) -> dict[str, object] | str:
        """
        Acknowledge all alarm level logs with optional filters.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        filterEventSource : Any, optional
            Event source filter.
        filterSource : int, optional
            Source filter.
        filterEventSourceItem : str, optional
            Event source item filter.
        filterTimeFrom : int, optional
            Start time for filtering.
        filterKeyword : str, optional
            Keyword to filter logs.
        doorIds : str, optional
            Door IDs filter.
        eventTypes : str, optional
            Event types filter.
        update : int, optional
            Update flag.

        Returns
        -------
        dict[str, object] or str
            Result of the acknowledge operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AckAlarm'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def modify_controller_logger_config(self,
                                        # TODO to check
                                        data: Any = None) -> dict[str, object] | str:
        """
        Modify the logger configuration for a controller.

        Parameters
        ----------
        data : Any, optional
            Logger configuration data (see example in docstring).

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.

        Notes
        -----
        Example data:
            data = {
                "log_evt": "11111111111111111111111111111111111111",
                "id": 97,
                "log_alarm": "00111111111111111111111111111111111111"
            }
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveLogConfig'}

        """data example:

        data={"log_evt":"11111111111111111111111111111111111111",
              "id": 97, "log_alarm":"00111111111111111111111111111111111111"}"""

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_controller_settings(self,
                                 arrayJson: str = None) -> dict[str, object] | str:
        """
        Save controller settings for Surveillance Station.

        Parameters
        ----------
        arrayJson : str, optional
            JSON string representing controller settings. Example:
            \\[\\{"enable": true, "id": 97, "name": "ctrler1", "host": "10.13.12.173", "port": 80,
              "model": "A1001", "username": "root", "password": "Q__Q-__-", "time_server":
              "SurveillanceStation", "time_zone": "Fiji", "door": \\[\\{"id": 231, "name": "FrontDoor",
              "enable_cam": true, "cam_ds_id": 0, "cam_id": 13\\}\\]\\}\\]

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        """arrayJson example:

           arrayJson="\\[\\{\"enable\":true,\"id\":97,\"name\":\"ctrler1\",\"host\":\"10.13.12.173\",\"port\":80,
                        \"model\":\"A1001\",\"username\":\"root\",\"password\":\"Q__Q-__-\",\"time_server\":
                        \"SurveillanceStation\",\"time_zone\":\"Fiji\",\"door\":\\[\\{\"id\":231,\"name\":\"FrontDoor\",
                        \"enable_cam\":true,\"cam_ds_id\":0,\"cam_id\":13\\}\\]\\}\\]\" """

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_filtered_logs(self,
                               start: int = None,
                               limit: int = None,
                               filterType: int = None,
                               filterEventSource: int = None,
                               filterSource: int = None,
                               filterEventSourceItem: str = None,
                               filterTimeFrom: int = None,
                               filterTimeTo: int = None,
                               filterKeyword: str = None,
                               doorIds: str = None,
                               eventTypes: str = None,
                               # TODO to modify for download?
                               update: int = None) -> dict[str, object] | str:
        """
        Download filtered logs from Surveillance Station.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        filterType : int, optional
            Type of filter to apply.
        filterEventSource : int, optional
            Event source filter.
        filterSource : int, optional
            Source filter.
        filterEventSourceItem : str, optional
            Event source item filter.
        filterTimeFrom : int, optional
            Start time for filtering.
        filterTimeTo : int, optional
            End time for filtering.
        filterKeyword : str, optional
            Keyword to filter logs.
        doorIds : str, optional
            Door IDs filter.
        eventTypes : str, optional
            Event types filter.
        update : int, optional
            Update flag.

        Returns
        -------
        dict[str, object] or str
            Downloaded log data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DownloadLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_door_name_from_controller(self,
                                      ctrlerId: int = None,
                                      ip: str = None,
                                      port: int = None,
                                      userName: str = None,
                                      # TODO to check
                                      password: int = None) -> dict[str, object] | str:
        """
        Retrieve door names from a specific controller.

        Parameters
        ----------
        ctrlerId : int, optional
            Controller ID.
        ip : str, optional
            Controller IP address.
        port : int, optional
            Controller port.
        userName : str, optional
            Username for authentication.
        password : int, optional
            Password for authentication (to check).

        Returns
        -------
        dict[str, object] or str
            Door names or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetDoorNames'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def test_connection_and_authentication(self,
                                           ctrlerId: int = None,
                                           ip: str = None,
                                           port: int = None,
                                           userName: str = None,
                                           # TODO to check
                                           password: int = None) -> dict[str, object] | str:
        """
        Test connection and authentication to a controller.

        Parameters
        ----------
        ctrlerId : int, optional
            Controller ID.
        ip : str, optional
            Controller IP address.
        port : int, optional
            Controller port.
        userName : str, optional
            Username for authentication.
        password : int, optional
            Password for authentication (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the test or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TestConnect'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_controller_list_info(self,
                                       start: int = None,
                                       limit: int = None,
                                       update: int = None,
                                       blIncludeRecCnt: bool = None,
                                       # TODO to check
                                       blIncludeAuInfo: bool = None) -> dict[str, object] | str:
        """
        Enumerate controller list information.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        update : int, optional
            Update flag.
        blIncludeRecCnt : bool, optional
            Whether to include record count.
        blIncludeAuInfo : bool, optional
            Whether to include additional info (to check).

        Returns
        -------
        dict[str, object] or str
            Controller list information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_cardholder_setting(self,
                                arrayJson: str = None) -> dict[str, object] | str:
        """
        Save cardholder settings.

        Parameters
        ----------
        arrayJson : str, optional
            JSON string representing cardholder settings.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_door_info(self,
                            DoorIds: str = None) -> dict[str, object] | str:
        """
        Enumerate door information.

        Parameters
        ----------
        DoorIds : str, optional
            Comma-separated list of door IDs.

        Returns
        -------
        dict[str, object] or str
            Door information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListDoor'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_logs_surveillance_station(self,
                                        filterType: int = None,
                                        filterEventSource: Any = None,
                                        filterSource: int = None,
                                        filterEventSourceItem: str = None,
                                        filterTimeFrom: int = None,
                                        filterTimeTo: int = None,
                                        filterKeyword: str = None,
                                        doorIds: str = None,
                                        eventTypes: str = None,
                                        update: int = None) -> dict[str, object] | str:
        """
        Clear logs in Surveillance Station with optional filters.

        Parameters
        ----------
        filterType : int, optional
            Type of filter to apply.
        filterEventSource : Any, optional
            Event source filter.
        filterSource : int, optional
            Source filter.
        filterEventSourceItem : str, optional
            Event source item filter.
        filterTimeFrom : int, optional
            Start time for filtering.
        filterTimeTo : int, optional
            End time for filtering.
        filterKeyword : str, optional
            Keyword to filter logs.
        doorIds : str, optional
            Door IDs filter.
        eventTypes : str, optional
            Event types filter.
        update : int, optional
            Update flag.

        Returns
        -------
        dict[str, object] or str
            Result of the clear operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ClearLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_all_user_privilege(self) -> dict[str, object] | str:
        """
        List all user privileges in Surveillance Station.

        Returns
        -------
        dict[str, object] or str
            List of user privileges or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListPrivilege'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def manual_lock_operation(self,
                              doorId: int = None,
                              # TODO to check
                              operation: int = None) -> dict[str, object] | str:
        """
        Perform a manual lock or unlock operation on a door.

        Parameters
        ----------
        doorId : int, optional
            Door ID to operate on.
        operation : int, optional
            Operation code (to check).

        Returns
        -------
        dict[str, object] or str
            Result of the operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DoorControl'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_user_door_priv_setting(self,
                                    arrayJson: str = None) -> dict[str, object] | str:
        """
        Save user door privilege settings.

        Parameters
        ----------
        arrayJson : str, optional
            JSON string representing user door privilege settings.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SavePrivilege'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_all_logs(self,
                      start: int = None,
                      limit: int = None,
                      filterType: int = None,
                      filterEventSource: Any = None,
                      filterSource: int = None,
                      filterEventSourceItem: str = None,
                      filterTimeFrom: int = None,
                      filterTimeTo: int = None,
                      filterKeyword: str = None,
                      timezoneOffset: int = None,
                      doorIds: str = None,
                      eventTypes: str = None,
                      update: int = None,
                      blIncludeRecCnt: bool = None,
                      blIncludeAuInfo: bool = None) -> dict[str, object] | str:
        """
        List all logs in Surveillance Station with optional filters.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        filterType : int, optional
            Type of filter to apply.
        filterEventSource : Any, optional
            Event source filter.
        filterSource : int, optional
            Source filter.
        filterEventSourceItem : str, optional
            Event source item filter.
        filterTimeFrom : int, optional
            Start time for filtering.
        filterTimeTo : int, optional
            End time for filtering.
        filterKeyword : str, optional
            Keyword to filter logs.
        timezoneOffset : int, optional
            Timezone offset.
        doorIds : str, optional
            Door IDs filter.
        eventTypes : str, optional
            Event types filter.
        update : int, optional
            Update flag.
        blIncludeRecCnt : bool, optional
            Whether to include record count.
        blIncludeAuInfo : bool, optional
            Whether to include additional info.

        Returns
        -------
        dict[str, object] or str
            List of logs or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_selected_controller(self, ids: str = None) -> dict[str, object] | str:
        """
        Delete selected controllers from Surveillance Station.

        Parameters
        ----------
        ids : str, optional
            Comma-separated string of controller IDs to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def retrieve_data_from_controller(self, ctrlerId: str = None) -> dict[str, object] | str:
        """
        Retrieve data from a specific controller.

        Parameters
        ----------
        ctrlerId : str, optional
            ID of the controller to retrieve data from.

        Returns
        -------
        dict[str, object] or str
            Retrieved data or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Retrieve'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def block_cardholder(self, arrayJson: str = None) -> dict[str, object] | str:
        """
        Block cardholders in Surveillance Station.

        Parameters
        ----------
        arrayJson : str, optional
            JSON string representing cardholder(s) to block.

        Returns
        -------
        dict[str, object] or str
            Result of the block operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'BlockCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_controller_count(self) -> dict[str, object] | str:
        """
        Get the count of controllers by category.

        Returns
        -------
        dict[str, object] or str
            Controller count or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategory'}

        return self.request_data(api_name, api_path, req_param)

    def start_controller_search(self) -> dict[str, object] | str:
        """
        Start searching for controllers.

        Returns
        -------
        dict[str, object] or str
            Result of the search operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        return self.request_data(api_name, api_path, req_param)

    def get_controller_search_info(self,
                                   pid: int = None,
                                   offset: int = None) -> dict[str, object] | str:
        """
        Get information about the current controller search.

        Parameters
        ----------
        pid : int, optional
            Process ID of the search.
        offset : int, optional
            Offset for paginated results.

        Returns
        -------
        dict[str, object] or str
            Search information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_digital_output(self,
                                 # TODO to check
                                 camId: int = None) -> dict[str, object] | str:
        """
        Enumerate digital output devices.

        Parameters
        ----------
        camId : int, optional
            Camera ID to filter digital outputs.

        Returns
        -------
        dict[str, object] or str
            List of digital outputs or error details.
        """
        api_name = 'SYNO.SurveillanceStation.DigitalOutput'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_digital_output_parameters(self,
                                       camId: int = None,
                                       idx: int = None,
                                       keep_setting: bool = None,
                                       normal_state: int = None,
                                       # TODO to check
                                       trigger_state: bool = None) -> dict[str, object] | str:
        """
        Save parameters for a digital output device.

        Parameters
        ----------
        camId : int, optional
            Camera ID.
        idx : int, optional
            Index of the digital output.
        keep_setting : bool, optional
            Whether to keep the current setting.
        normal_state : int, optional
            Normal state value.
        trigger_state : bool, optional
            Trigger state value.

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.DigitalOutput'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def long_polling_digital_output_status(self,
                                           camId: int = None,
                                           idx: int = None,
                                           keep: bool = None,
                                           setNormalCap: bool = None,
                                           normal: int = None,
                                           trigger: bool = None,
                                           # TODO to check
                                           timeOut: int = None) -> dict[str, object] | str:
        """
        Perform long polling to get the status of a digital output.

        Parameters
        ----------
        camId : int, optional
            Camera ID.
        idx : int, optional
            Index of the digital output.
        keep : bool, optional
            Whether to keep polling.
        setNormalCap : bool, optional
            Set normal capability.
        normal : int, optional
            Normal state value.
        trigger : bool, optional
            Trigger state value.
        timeOut : int, optional
            Timeout for polling.

        Returns
        -------
        dict[str, object] or str
            Status information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.DigitalOutput'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PollState'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def trigger_external_event(self,
                               eventId: int = None,
                               # TODO to check
                               eventName: str = None) -> dict[str, object] | str:
        """
        Trigger an external event in Surveillance Station.

        Parameters
        ----------
        eventId : int, optional
            ID of the event to trigger.
        eventName : str, optional
            Name of the event to trigger.

        Returns
        -------
        dict[str, object] or str
            Result of the trigger operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.ExternalEvent'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Trigger'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_list_io_modules(self,
                            start: int = None,
                            limit: int = None,
                            blFromList: bool = None,
                            # TODO to check
                            ownerDsId: int = None) -> dict[str, object] | str:
        """
        Get a list of I/O modules.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        blFromList : bool, optional
            Whether to get from list.
        ownerDsId : int, optional
            Owner device station ID.

        Returns
        -------
        dict[str, object] or str
            List of I/O modules or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_io_port_list(self,
                         Id: int = None,
                         Port: int = None,
                         IP: str = None,
                         User: str = None,
                         Pass: str = None,
                         Vendor: str = None,
                         # TODO to check
                         Model: str = None) -> dict[str, object] | str:
        """
        Get a list of I/O ports for a module.

        Parameters
        ----------
        Id : int, optional
            Module ID.
        Port : int, optional
            Port number.
        IP : str, optional
            IP address.
        User : str, optional
            Username.
        Pass : str, optional
            Password.
        Vendor : str, optional
            Vendor name.
        Model : str, optional
            Model name.

        Returns
        -------
        dict[str, object] or str
            List of I/O ports or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumPort'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def get_supported_list_io_modules(self) -> dict[str, object] | str:
        """
        Get a list of supported I/O module vendor models.

        Returns
        -------
        dict[str, object] or str
            List of supported vendor models or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'EnumVendorModel'}

        return self.request_data(api_name, api_path, req_param)

    def save_setting_io_module(self,
                               name: str = None,
                               id: int = None,
                               ownerDsId: int = None,
                               vendor: str = None,
                               model: str = None,
                               ip: str = None,
                               port: int = None,
                               userName: str = None,
                               enabled: bool = None,
                               status: int = None,
                               timeServer: str = None,
                               passWord: str = None,
                               ntpEnable: bool = None,
                               # TODO to check
                               DIOdata: Any = None) -> dict[str, object] | str:
        """
        Save or update the settings for an I/O module in Surveillance Station.

        Parameters
        ----------
        name : str, optional
            Name of the I/O module.
        id : int, optional
            ID of the I/O module.
        ownerDsId : int, optional
            Owner device station ID.
        vendor : str, optional
            Vendor name of the I/O module.
        model : str, optional
            Model name of the I/O module.
        ip : str, optional
            IP address of the I/O module.
        port : int, optional
            Port number for the I/O module.
        userName : str, optional
            Username for authentication.
        enabled : bool, optional
            Whether the I/O module is enabled.
        status : int, optional
            Status code of the I/O module.
        timeServer : str, optional
            Time server address.
        passWord : str, optional
            Password for authentication.
        ntpEnable : bool, optional
            Whether NTP is enabled.
        DIOdata : Any, optional
            Digital I/O data (structure to be checked).

        Returns
        -------
        dict[str, object] or str
            Result of the save operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_io_modules(self,
                          # TODO to check
                          iomlist: str = None) -> dict[str, object] | str:
        """
        Enable specified I/O modules.

        Parameters
        ----------
        iomlist : str, optional
            Comma-separated list of I/O module IDs to enable.

        Returns
        -------
        dict[str, object] or str
            Result of the enable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_io_modules(self,
                           # TODO to check
                           iomlist: str = None) -> dict[str, object] | str:
        """
        Disable specified I/O modules.

        Parameters
        ----------
        iomlist : str, optional
            Comma-separated list of I/O module IDs to disable.

        Returns
        -------
        dict[str, object] or str
            Result of the disable operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_io_modules(self,
                          # TODO to check
                          iomlist: str = None) -> dict[str, object] | str:
        """
        Delete specified I/O modules.

        Parameters
        ----------
        iomlist : str, optional
            Comma-separated list of I/O module IDs to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def test_connection_to_io_module(self,
                                     id: int = None,
                                     port: str = None,
                                     ip: str = None,
                                     userName: str = None,
                                     passWord: str = None,
                                     # TODO to check
                                     model: str = None) -> dict[str, object] | str:
        """
        Test the connection to a specified I/O module.

        Parameters
        ----------
        id : int, optional
            ID of the I/O module.
        port : str, optional
            Port number for the I/O module.
        ip : str, optional
            IP address of the I/O module.
        userName : str, optional
            Username for authentication.
        passWord : str, optional
            Password for authentication.
        model : str, optional
            Model name of the I/O module.

        Returns
        -------
        dict[str, object] or str
            Result of the connection test or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TestConn'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_capability_io_module(self,
                                 vendor: str = None,
                                 # TODO to check
                                 model: str = None) -> dict[str, object] | str:
        """
        Get the capability information for a specified I/O module.

        Parameters
        ----------
        vendor : str, optional
            Vendor name of the I/O module.
        model : str, optional
            Model name of the I/O module.

        Returns
        -------
        dict[str, object] or str
            Capability information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCap'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def configure_io_port_setting(self,
                                  id: int = None,
                                  # TODO to check
                                  DIOdata: Any = None) -> dict[str, object] | str:
        """
        Configure the port settings for a specified I/O module.

        Parameters
        ----------
        id : int, optional
            ID of the I/O module.
        DIOdata : Any, optional
            Digital I/O data for port configuration (structure to be checked).

        Returns
        -------
        dict[str, object] or str
            Result of the configuration or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PortSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def poll_trigger_state_io_module(self,
                                     Id: int = None,
                                     list: Any = None,
                                     # TODO to check
                                     timeOut: int = None) -> dict[str, object] | str:
        """
        Poll the trigger state of digital input (DI) ports for a specified I/O module.

        Parameters
        ----------
        Id : int, optional
            ID of the I/O module.
        list : Any, optional
            List of DI ports to poll (structure to be checked).
        timeOut : int, optional
            Timeout for polling operation.

        Returns
        -------
        dict[str, object] or str
            Polling result or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PollingDI'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def poll_do_trigger_module(self,
                               id: int = None,
                               idx: int = None,
                               normal: int = None,
                               trigger: bool = None,
                               # TODO to check
                               timeOut: int = None) -> dict[str, object] | str:
        """
        Poll the trigger state of digital output (DO) ports for a specified I/O module.

        Parameters
        ----------
        id : int, optional
            ID of the I/O module.
        idx : int, optional
            Index of the DO port.
        normal : int, optional
            Normal state value.
        trigger : bool, optional
            Trigger state.
        timeOut : int, optional
            Timeout for polling operation.

        Returns
        -------
        dict[str, object] or str
            Polling result or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PollingDO'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO to check
    def get_number_of_devices(self) -> dict[str, object] | str:
        """
        Get the number of I/O devices for each device station.

        Returns
        -------
        dict[str, object] or str
            Number of devices or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetDevNumOfDs'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_category_count_io_module(self,
                                     start: int = None,
                                     limit: int = None,
                                     ownerDsId: int = None,
                                     # TODO to check
                                     blFromList: bool = None) -> dict[str, object] | str:
        """
        Get the count of I/O modules by category.

        Parameters
        ----------
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.
        ownerDsId : int, optional
            Owner device station ID.
        blFromList : bool, optional
            Whether to get count from a list (to be checked).

        Returns
        -------
        dict[str, object] or str
            Count by category or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_search_io_module(self) -> dict[str, object] | str:
        """
        Start searching for I/O modules.

        Returns
        -------
        dict[str, object] or str
            Result of the search operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        return self.request_data(api_name, api_path, req_param)

    def get_search_io_module_info(self,
                                  pid: int = None) -> dict[str, object] | str:
        """
        Get information about the current I/O module search.

        Parameters
        ----------
        pid : int, optional
            Process ID of the search.

        Returns
        -------
        dict[str, object] or str
            Search information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.IOModule.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'InfoGet'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_current_camera_status(self,
                                  # TODO not working
                                  id_list: str = None) -> dict[str, object] | str:
        """
        Get the current status of specified cameras.

        Parameters
        ----------
        id_list : str, optional
            Comma-separated list of camera IDs.

        Returns
        -------
        dict[str, object] or str
            Camera status information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'OneTime'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_preset_camera_list(self,
                                # TODO not working
                                cameraId: Any = None) -> dict[str, object] | str:
        """
        Enumerate the list of presets for a specified camera.

        Parameters
        ----------
        cameraId : Any, optional
            ID of the camera.

        Returns
        -------
        dict[str, object] or str
            List of camera presets or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_preset_camera_capability(self,
                                     # TODO not working
                                     cameraId: int = None) -> dict[str, object] | str:
        """
        Get the capability information for camera presets.

        Parameters
        ----------
        cameraId : int, optional
            ID of the camera.

        Returns
        -------
        dict[str, object] or str
            Preset capability information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def record_current_camera_position(self,
                                       cameraId: int = None,
                                       position: int = None,
                                       speed: int = None,
                                       # TODO not working
                                       name: str = None) -> dict[str, object] | str:
        """
        Record the current position of a camera as a preset.

        Parameters
        ----------
        cameraId : int, optional
            ID of the camera.
        position : int, optional
            Preset position index.
        speed : int, optional
            Speed for moving to the preset.
        name : str, optional
            Name for the preset.

        Returns
        -------
        dict[str, object] or str
            Result of the record operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetPreset'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_list_preset_camera(self,
                                  cameraId: Any = None,
                                  # TODO not working
                                  position: str = None) -> dict[str, object] | str:
        """
        Delete specified presets from a camera.

        Parameters
        ----------
        cameraId : Any, optional
            ID of the camera.
        position : str, optional
            Preset position(s) to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DelPreset'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def go_specific_preset_by_given_speed(self,
                                          cameraId: Any = None,
                                          position: int = None,
                                          speed: int = None,
                                          # TODO not working
                                          type: int = None) -> dict[str, object] | str:
        """
        Move a camera to a specific preset position at a given speed.

        Parameters
        ----------
        cameraId : Any, optional
            ID of the camera.
        position : int, optional
            Preset position index.
        speed : int, optional
            Speed for moving to the preset.
        type : int, optional
            Type of preset move (to be checked).

        Returns
        -------
        dict[str, object] or str
            Result of the move operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Execute'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_current_camera_position(self,
                                    cameraId: Any = None,
                                    # TODO not working
                                    bindPosition: int = None) -> dict[str, object] | str:
        """
        Set the current position of a camera as the home position.

        Parameters
        ----------
        cameraId : Any, optional
            ID of the camera.
        bindPosition : int, optional
            Position to bind as home.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetHome'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_patrol_list(self,
                         cam: Any = None) -> dict[str, object] | str:
        """
        Enumerate the list of patrols for a specified camera.

        Parameters
        ----------
        cam : Any, optional
            Camera identifier.

        Returns
        -------
        dict[str, object] or str
            List of patrols or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_patrol_name_list(self,
                              camId: Any = None) -> dict[str, object] | str:
        """
        Enumerate the list of patrol names for a specified camera.

        Parameters
        ----------
        camId : Any, optional
            Camera identifier.

        Returns
        -------
        dict[str, object] or str
            List of patrol names or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumPartial'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_patrol_detail(self,
                           # TODO not working
                           id: int = None) -> dict[str, object] | str:
        """
        Load the details of a specific patrol.

        Parameters
        ----------
        id : int, optional
            Patrol ID.

        Returns
        -------
        dict[str, object] or str
            Patrol details or error information.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def add_or_modify_patrol(self,
                             camId: Any = None,
                             id: int = None,
                             stayTime: int = None,
                             speed: int = None,
                             name: str = None,
                             # TODO not working
                             presetList: Any = None) -> dict[str, object] | str:
        """
        Add or modify a patrol for a camera.

        Parameters
        ----------
        camId : Any, optional
            Camera identifier.
        id : int, optional
            Patrol ID.
        stayTime : int, optional
            Stay time at each preset.
        speed : int, optional
            Patrol speed.
        name : str, optional
            Name of the patrol.
        presetList : Any, optional
            List of presets for the patrol (structure to be checked).

        Returns
        -------
        dict[str, object] or str
            Result of the add/modify operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_patrol(self,
                               camId: Any = None,
                               # TODO not working
                               patrolId: str = None) -> dict[str, object] | str:
        """
        Delete a specific patrol from a camera.

        Parameters
        ----------
        camId : Any, optional
            Camera identifier.
        patrolId : str, optional
            Patrol ID to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def run_patrol(self,
                   camId: Any = None,
                   id: int = None) -> dict[str, object] | str:  # TODO not working
        """
        Run a specified patrol on a camera.

        Parameters
        ----------
        camId : Any, optional
            Camera identifier.
        id : int, optional
            Patrol ID.

        Returns
        -------
        dict[str, object] or str
            Result of the run operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Execute'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_patrol(self,
                    camId: Any = None) -> dict[str, object] | str:  # TODO not working
        """
        Stop the currently running patrol on a camera.

        Parameters
        ----------
        camId : Any, optional
            Camera identifier.

        Returns
        -------
        dict[str, object] or str
            Result of the stop operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Stop'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_camera_search_process(self) -> dict[str, object] | str:
        """
        Start searching for cameras.

        Returns
        -------
        dict[str, object] or str
            Result of the search operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        return self.request_data(api_name, api_path, req_param)

    def get_camera_search_info(self,
                               pid: int = None,
                               offset: int = None) -> dict[str, object] | str:
        """
        Get information about the current camera search.

        Parameters
        ----------
        pid : int, optional
            Process ID of the search.
        offset : int, optional
            Offset for pagination.

        Returns
        -------
        dict[str, object] or str
            Search information or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def toggle_home_mode(self,
                         on: bool = None) -> dict[str, object] | str:
        """
        Toggle the Home Mode in Surveillance Station.

        Parameters
        ----------
        on : bool, optional
            Whether to enable (True) or disable (False) Home Mode.

        Returns
        -------
        dict[str, object] or str
            Result of the toggle operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.HomeMode'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Switch'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_home_mode_settings(self,
                               need_mobiles: bool = None) -> dict[str, object] | str:
        """
        Get the current Home Mode settings.

        Parameters
        ----------
        need_mobiles : bool, optional
            Whether to include mobile device information.

        Returns
        -------
        dict[str, object] or str
            Home Mode settings or error details.
        """
        api_name = 'SYNO.SurveillanceStation.HomeMode'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_transaction_list(self,
                             filterIds: str = None,
                             filterDsIds: str = None,
                             filterEnable: bool = None,
                             filterStatus: int = None,
                             start: int = None,
                             # TODO not working
                             limit: int = None) -> dict[str, object] | str:
        """
        Get a list of device transactions with optional filters.

        Parameters
        ----------
        filterIds : str, optional
            Comma-separated list of transaction IDs to filter.
        filterDsIds : str, optional
            Comma-separated list of device station IDs to filter.
        filterEnable : bool, optional
            Filter by enabled status.
        filterStatus : int, optional
            Filter by status code.
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.

        Returns
        -------
        dict[str, object] or str
            List of transactions or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Device'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_all_transaction_list(self,
                                 filterIds: str = None,
                                 dsId: int = None,
                                 filterTimeFrom: Any = None,
                                 filterStatus: int = None,
                                 filterLock: bool = None,
                                 filterTimeTo: Any = None,
                                 filterTimeRangeIntersect: bool = None,
                                 filterKeyword: str = None,
                                 start: int = None,
                                 # TODO not working
                                 limit: int = None) -> dict[str, object] | str:
        """
        Get a list of all transactions with optional filters.

        Parameters
        ----------
        filterIds : str, optional
            Comma-separated list of transaction IDs to filter.
        dsId : int, optional
            Device station ID.
        filterTimeFrom : Any, optional
            Start time for filtering.
        filterStatus : int, optional
            Filter by status code.
        filterLock : bool, optional
            Filter by lock status.
        filterTimeTo : Any, optional
            End time for filtering.
        filterTimeRangeIntersect : bool, optional
            Whether to intersect time ranges.
        filterKeyword : str, optional
            Keyword for filtering.
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.

        Returns
        -------
        dict[str, object] or str
            List of transactions or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_history_records(self,
                             filterIds: str = None,
                             dsId: int = None,
                             filterStatus: int = None,
                             filterLock: bool = None,
                             filterTimeFrom: Any = None,
                             filterTimeTo: Any = None,
                             filterTimeRangeIntersect: bool = None,
                             filterKeyword: str = None,
                             start: int = None,
                             limit: int = None) -> dict[str, object] | str:
        """
         Lock specified history records.

         Parameters
         ----------
         filterIds : str, optional
             Comma-separated list of record IDs to lock.
         dsId : int, optional
             Device station ID.
         filterStatus : int, optional
             Filter by status code.
         filterLock : bool, optional
             Filter by lock status.
         filterTimeFrom : Any, optional
             Start time for filtering.
         filterTimeTo : Any, optional
             End time for filtering.
         filterTimeRangeIntersect : bool, optional
             Whether to intersect time ranges.
         filterKeyword : str, optional
             Keyword for filtering.
         start : int, optional
             Start index for pagination.
         limit : int, optional
             Maximum number of results to return.

         Returns
         -------
         dict[str, object] or str
             Result of the lock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_history_records(self,
                               filterIds: str = None,
                               dsId: int = None,
                               filterStatus: int = None,
                               filterLock: bool = None,
                               filterTimeFrom: Any = None,
                               filterTimeTo: Any = None,
                               filterTimeRangeIntersect: bool = None,
                               filterKeyword: str = None,
                               start: int = None,
                               limit: int = None) -> dict[str, object] | str:
        """
        Unlock specified history records.

        Parameters
        ----------
        filterIds : str, optional
            Comma-separated list of record IDs to unlock.
        dsId : int, optional
            Device station ID.
        filterStatus : int, optional
            Filter by status code.
        filterLock : bool, optional
            Filter by lock status.
        filterTimeFrom : Any, optional
            Start time for filtering.
        filterTimeTo : Any, optional
            End time for filtering.
        filterTimeRangeIntersect : bool, optional
            Whether to intersect time ranges.
        filterKeyword : str, optional
            Keyword for filtering.
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.

        Returns
        -------
        dict[str, object] or str
            Result of the unlock operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_history_records(self,
                               filterIds: str = None,
                               dsId: int = None,
                               filterStatus: int = None,
                               filterLock: bool = None,
                               filterTimeFrom: Any = None,
                               filterTimeTo: Any = None,
                               filterTimeRangeIntersect: bool = None,
                               filterKeyword: str = None,
                               start: int = None,
                               limit: int = None) -> dict[str, object] | str:
        """
        Delete specified history records.

        Parameters
        ----------
        filterIds : str, optional
            Comma-separated list of record IDs to delete.
        dsId : int, optional
            Device station ID.
        filterStatus : int, optional
            Filter by status code.
        filterLock : bool, optional
            Filter by lock status.
        filterTimeFrom : Any, optional
            Start time for filtering.
        filterTimeTo : Any, optional
            End time for filtering.
        filterTimeRangeIntersect : bool, optional
            Whether to intersect time ranges.
        filterKeyword : str, optional
            Keyword for filtering.
        start : int, optional
            Start index for pagination.
        limit : int, optional
            Maximum number of results to return.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_session_with_specified_session_id(self,
                                                device_name: str = None,
                                                session_id: str = None,
                                                # TODO not working
                                                timeout: int = None) -> dict[str, object] | str:
        """
        Start a session with a specified session ID.

        Parameters
        ----------
        device_name : str, optional
            Name of the device.
        session_id : str, optional
            Session ID to start.
        timeout : int, optional
            Timeout for the session.

        Returns
        -------
        dict[str, object] or str
            Result of the start operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Begin'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def complete_session_with_specified_id(self,
                                           device_name: str = None,
                                           # TODO not working
                                           session_id: str = None) -> dict[str, object] | str:
        """
        Complete a session with a specified session ID.

        Parameters
        ----------
        device_name : str, optional
            Name of the device.
        session_id : str, optional
            Session ID to complete.

        Returns
        -------
        dict[str, object] or str
            Result of the complete operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Complete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def cancel_session_with_specified_session_id(self,
                                                 device_name: str = None,
                                                 # TODO not working
                                                 session_id: str = None) -> dict[str, object] | str:
        """
        Cancel a session with a specified session ID.

        Parameters
        ----------
        device_name : str, optional
            Name of the device.
        session_id : str, optional
            Session ID to cancel.

        Returns
        -------
        dict[str, object] or str
            Result of the cancel operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Cancel'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def carry_data_into_session_id(self,
                                   device_name: str = None,
                                   session_id: str = None,
                                   # TODO not working
                                   content: str = None) -> dict[str, object] | str:
        """
        Append data to a session with a specified session ID.

        Parameters
        ----------
        device_name : str, optional
            Name of the device.
        session_id : str, optional
            Session ID to append data to.
        content : str, optional
            Data content to append.

        Returns
        -------
        dict[str, object] or str
            Result of the append operation or error details.
        """
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AppendData'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def add_edit_active_vault_task(self,
                                   blCustomFolder: bool = None,
                                   blLimitBySize: bool = None,
                                   blRotateFile: bool = None,
                                   blSrcRecNoOverlap: bool = None,
                                   blUseRecDet: bool = None,
                                   camId: Any = None,
                                   camInfo: Any = None,
                                   dayLimit: int = None,
                                   didCode: str = None,
                                   dsSerial: str = None,
                                   execTime: Any = None,
                                   hostname: str = None,
                                   id: int = None,
                                   name: str = None,
                                   passwd: str = None,
                                   port: str = None,
                                   recEndTm: Any = None,
                                   recMode: str = None,
                                   recSchedule: str = None,
                                   recStartTm: Any = None,
                                   schedule: str = None,
                                   storagePath: str = None,
                                   # TODO to check
                                   type: int = None) -> dict[str, object] | str:
        """
        Add or edit an active vault task for archiving.

        Parameters
        ----------
        blCustomFolder : bool, optional
            Whether to use a custom folder for storage.
        blLimitBySize : bool, optional
            Whether to limit the archive by size.
        blRotateFile : bool, optional
            Whether to enable file rotation.
        blSrcRecNoOverlap : bool, optional
            Whether to avoid overlapping source recordings.
        blUseRecDet : bool, optional
            Whether to use recording detection.
        camId : Any, optional
            Camera ID.
        camInfo : Any, optional
            Camera information.
        dayLimit : int, optional
            Day limit for the archive.
        didCode : str, optional
            Device code.
        dsSerial : str, optional
            Device serial number.
        execTime : Any, optional
            Execution time.
        hostname : str, optional
            Hostname of the source server.
        id : int, optional
            Task ID (for editing).
        name : str, optional
            Name of the task.
        passwd : str, optional
            Password for authentication.
        port : str, optional
            Port number.
        recEndTm : Any, optional
            Recording end time.
        recMode : str, optional
            Recording mode.
        recSchedule : str, optional
            Recording schedule.
        recStartTm : Any, optional
            Recording start time.
        schedule : str, optional
            Task schedule.
        storagePath : str, optional
            Path for storage.
        type : int, optional
            Type of the task.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def login_source_server_get_info(self,
                                     port: str = None,
                                     hostname: str = None,
                                     protocol: bool = None,
                                     username: str = None,
                                     passwd: str = None,
                                     archId: int = None,
                                     didCode: str = None,
                                     # TODO not working
                                     srcDsId: int = None) -> dict[str, object] | str:
        """
        Log in to the source server and retrieve information.

        Parameters
        ----------
        port : str, optional
            Port number of the source server.
        hostname : str, optional
            Hostname of the source server.
        protocol : bool, optional
            Protocol to use (e.g., HTTPS).
        username : str, optional
            Username for authentication.
        passwd : str, optional
            Password for authentication.
        archId : int, optional
            Archive ID.
        didCode : str, optional
            Device code.
        srcDsId : int, optional
            Source device ID (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LoginSourceDS'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_archive_vault_task(self,
                                  id: int = None,
                                  keepRec: bool = None) -> dict[str, object] | str:
        """
        Delete an archive vault task.

        Parameters
        ----------
        id : int, optional
            Task ID to delete.
        keepRec : bool, optional
            Whether to keep the recordings.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_exist_archive_vault(self) -> dict[str, object] | str:
        """
        List all existing archive vault tasks.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_archive_vault_task(self,
                                  # TODO not working
                                  id: int = None) -> dict[str, object] | str:
        """
        Enable an archive vault task.

        Parameters
        ----------
        id : int, optional
            Task ID to enable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_archive_vault_task(self,
                                   id: int = None) -> dict[str, object] | str:
        """
        Disable an archive vault task.

        Parameters
        ----------
        id : int, optional
            Task ID to disable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DisableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_archive_vault_batchedit_task(self,
                                             taskIds: str = None,
                                             # TODO not working
                                             attrs: Any = None) -> dict[str, object] | str:
        """
        Batch edit (disable) archive vault tasks.

        Parameters
        ----------
        taskIds : str, optional
            Comma-separated list of task IDs.
        attrs : Any, optional
            Additional attributes for batch edit (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'BatchEditTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_batch_edit_progress(self,
                                # TODO not working
                                pid: int = None) -> dict[str, object] | str:
        """
        Get the progress of a batch edit operation.

        Parameters
        ----------
        pid : int, optional
            Process ID of the batch edit operation (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'BatchEditProgress'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_batchedit_proress_info(self,
                                   # TODO not working
                                   pid: int = None) -> dict[str, object] | str:
        """
        Get detailed information about batch edit progress.

        Parameters
        ----------
        pid : int, optional
            Process ID of the batch edit operation (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetBatchEditProgress'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clean_batchedit_progress_data(self,
                                      pid: int = None) -> dict[str, object] | str:
        """
        Clean up batch edit progress data.

        Parameters
        ----------
        pid : int, optional
            Process ID of the batch edit operation.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'BatchEditProgressDone'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_youtube_live_broadcast_setting(self) -> dict[str, object] | str:
        """
        Get the current YouTube Live broadcast settings.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.YoutubeLive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        return self.request_data(api_name, api_path, req_param)

    def set_youtube_live_broadcast_info(self,
                                        rtmp_path: str = None,
                                        key: str = None,
                                        cam_id: int = None,
                                        stream_profile: int = None,
                                        live_on: bool = None) -> dict[str, object] | str:
        """
        Set YouTube Live broadcast information.

        Parameters
        ----------
        rtmp_path : str, optional
            RTMP path for the broadcast.
        key : str, optional
            Stream key.
        cam_id : int, optional
            Camera ID.
        stream_profile : int, optional
            Stream profile.
        live_on : bool, optional
            Whether to enable live broadcast.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.YoutubeLive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def close_youtube_live_broadcast(self) -> dict[str, object] | str:
        """
        Close the current YouTube Live broadcast.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.YoutubeLive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CloseLive'}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def get_deep_video_analytic(self) -> dict[str, object] | str:
        """
        Get the list of deep video analytic tasks.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        return self.request_data(api_name, api_path, req_param)

    def create_edit_DVA_task(self,
                             analyze_type: int = None,
                             actFromHost: bool = None,
                             name: str = None,
                             camera_id: int = None,
                             enable: bool = None,
                             enable_recording: bool = None,
                             pre_rec_time: int = None,
                             post_rec_time: int = None,
                             event_integration: int = None,
                             region_type: int = None,
                             det_region_cnt: int = None,
                             det_region: int = None,
                             people_mode: int = None,
                             reset_cnt_frequency: int = None,
                             reset_weekday: int = None,
                             reset_date: int = None,
                             reset_time_minute: int = None,
                             reset_time_hour: int = None,
                             fence_dir_flag: int = None,
                             people_display_pos: int = None,
                             stream_profile: int = None,
                             people_enable_stay_max: bool = None,
                             intrusion_detect_target: int = None,
                             min_obj_size: Any = None,
                             min_obj_size_option: int = None,
                             enable_min_duration: int = None,
                             people_display_info: int = None,
                             people_enter: int = None,
                             people_stay_max: int = None,
                             people_region: str = None,
                             people_hint_pos: str = None,
                             # TODO not working
                             blEditMode: bool = None) -> dict[str, object] | str:
        """
        Create or edit a Deep Video Analytics (DVA) task.

        Parameters
        ----------
        analyze_type : int, optional
            Type of analysis to perform.
        actFromHost : bool, optional
            Whether the action is triggered from the host.
        name : str, optional
            Name of the DVA task.
        camera_id : int, optional
            ID of the camera associated with the task.
        enable : bool, optional
            Whether to enable the task.
        enable_recording : bool, optional
            Whether to enable recording for the task.
        pre_rec_time : int, optional
            Pre-recording time in seconds.
        post_rec_time : int, optional
            Post-recording time in seconds.
        event_integration : int, optional
            Event integration setting.
        region_type : int, optional
            Type of detection region.
        det_region_cnt : int, optional
            Number of detection regions.
        det_region : int, optional
            Detection region configuration.
        people_mode : int, optional
            People counting mode.
        reset_cnt_frequency : int, optional
            Frequency for resetting the counter.
        reset_weekday : int, optional
            Weekday for counter reset.
        reset_date : int, optional
            Date for counter reset.
        reset_time_minute : int, optional
            Minute for counter reset.
        reset_time_hour : int, optional
            Hour for counter reset.
        fence_dir_flag : int, optional
            Fence direction flag.
        people_display_pos : int, optional
            Display position for people counting.
        stream_profile : int, optional
            Stream profile to use.
        people_enable_stay_max : bool, optional
            Whether to enable maximum stay for people.
        intrusion_detect_target : int, optional
            Target for intrusion detection.
        min_obj_size : Any, optional
            Minimum object size for detection.
        min_obj_size_option : int, optional
            Option for minimum object size.
        enable_min_duration : int, optional
            Enable minimum duration for detection.
        people_display_info : int, optional
            Display information for people counting.
        people_enter : int, optional
            Number of people entering.
        people_stay_max : int, optional
            Maximum number of people staying.
        people_region : str, optional
            Region for people counting.
        people_hint_pos : str, optional
            Hint position for people counting.
        blEditMode : bool, optional
            Edit mode flag (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_dva_task(self,
                        ids: str = None) -> dict[str, object] | str:  # TODO not working
        """
        Delete a Deep Video Analytics (DVA) task.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of DVA task IDs to delete.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_dva_task(self,
                        ids: str = None) -> dict[str, object] | str:  # TODO not working
        """
        Enable one or more Deep Video Analytics (DVA) tasks.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of DVA task IDs to enable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_dva_task(self,
                         # TODO not working
                         ids: str = None) -> dict[str, object] | str:
        """
        Disable one or more Deep Video Analytics (DVA) tasks.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of DVA task IDs to disable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DisableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def reset_counter_people_counting_task(self,
                                           # TODO not working
                                           taskId: str = None) -> dict[str, object] | str:
        """
        Reset the people counting counter for a specific DVA task.

        Parameters
        ----------
        taskId : str, optional
            ID of the people counting task to reset.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ResetPplCntCounter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_people_enter_leave_count(self,
                                     ids: str = None,
                                     timeStart: str = None,
                                     timeEnd: str = None,
                                     timezone: int = None,
                                     ) -> dict[str, object] | str:  # TODO not working
        """
        Get the count of people entering and leaving for specified DVA tasks.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of DVA task IDs.
        timeStart : str, optional
            Start time for the count (ISO format or timestamp).
        timeEnd : str, optional
            End time for the count (ISO format or timestamp).
        timezone : int, optional
            Timezone offset.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Report'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_people_count_of_day(self,
                                ids: str = None,
                                interval: int = None,
                                intervalUnit: int = None,
                                timezone: int = None,
                                timestamp: int = None,
                                # TODO not working
                                blOccupancy: int = None) -> dict[str, object] | str:
        """
        Get the people count report for a specific day.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of DVA task IDs.
        interval : int, optional
            Interval for the report.
        intervalUnit : int, optional
            Unit for the interval.
        timezone : int, optional
            Timezone offset.
        timestamp : int, optional
            Timestamp for the report.
        blOccupancy : int, optional
            Occupancy flag (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Report'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetReport'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_people_counting_task(self,
                                  taskList: str = None,
                                  # TODO not working
                                  limit: int = None) -> dict[str, object] | str:
        """
        List people counting tasks.

        Parameters
        ----------
        taskList : str, optional
            Comma-separated list of task IDs to list.
        limit : int, optional
            Limit the number of tasks returned (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_recording_file_of_detection(self,
                                           slaveDsParam: str = None,
                                           # TODO not working
                                           deleteMethod: int = None) -> dict[str, object] | str:
        """
        Delete recording files associated with detection events.

        Parameters
        ----------
        slaveDsParam : str, optional
            Parameters for the slave device.
        deleteMethod : int, optional
            Method for deletion (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_info_of_task_and_frame(self,
                                   eventId: int = None,
                                   taskId: int = None,
                                   # TODO not working
                                   blAlertEvt: bool = None) -> dict[str, object] | str:
        """
        Get analytic result information for a specific task and frame.

        Parameters
        ----------
        eventId : int, optional
            Event ID to query.
        taskId : int, optional
            Task ID to query.
        blAlertEvt : bool, optional
            Alert event flag (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetAnalyticResult'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_recording_file_of_detection(self,
                                         dsId: int = None,
                                         # TODO not working
                                         idList: int = None) -> dict[str, object] | str:
        """
        Lock recording files associated with detection events.

        Parameters
        ----------
        dsId : int, optional
            Device server ID.
        idList : int, optional
            List of recording file IDs to lock (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_recording_file_of_detection(self,
                                           dsId: int = None,
                                           # TODO not working
                                           idList: str = None) -> dict[str, object] | str:
        """
        Unlock recording files associated with detection events.

        Parameters
        ----------
        dsId : int, optional
            Device server ID.
        idList : str, optional
            List of recording file IDs to unlock (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    # TODO not working
    def get_info_people_counting_task(self) -> dict[str, object] | str:
        """
        Get information about people counting tasks.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_people_counting_task(self,
                                    enable: bool = None,
                                    task_ids: str = None,
                                    owner_ds_id: int = None,
                                    name: str = None,
                                    people_display_info: str = None,
                                    people_enable_stay_max: int = None,
                                    reset_cnt_frequency: int = None,
                                    resert_date: int = None,
                                    resert_weekday: int = None,
                                    resert_tome_hour: int = None,
                                    # TODO not working
                                    resert_tome_minute: int = None) -> dict[str, object] | str:
        """
        Create a new people counting task.

        Parameters
        ----------
        enable : bool, optional
            Whether to enable the task.
        task_ids : str, optional
            Comma-separated list of task IDs.
        owner_ds_id : int, optional
            Owner device server ID.
        name : str, optional
            Name of the task.
        people_display_info : str, optional
            Display information for people counting.
        people_enable_stay_max : int, optional
            Enable maximum stay for people.
        reset_cnt_frequency : int, optional
            Frequency for resetting the counter.
        resert_date : int, optional
            Date for counter reset.
        resert_weekday : int, optional
            Weekday for counter reset.
        resert_tome_hour : int, optional
            Hour for counter reset.
        resert_tome_minute : int, optional
            Minute for counter reset (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def modify_setting_of_people_counting_task(self,
                                               enable: bool = None,
                                               id: int = None,
                                               task_ids: str = None,
                                               name: str = None,
                                               people_display_info: int = None,
                                               people_enable_max: int = None,
                                               reset_cnt_frequency: int = None,
                                               resert_date: int = None,
                                               resert_weekday: int = None,
                                               resert_tome_hour: int = None,
                                               # TODO not working
                                               resert_tome_minute: int = None) -> dict[str, object] | str:
        """
        Modify the settings of an existing people counting task.

        Parameters
        ----------
        enable : bool, optional
            Whether to enable the task.
        id : int, optional
            ID of the task to modify.
        task_ids : str, optional
            Comma-separated list of task IDs.
        name : str, optional
            Name of the task.
        people_display_info : int, optional
            Display information for people counting.
        people_enable_max : int, optional
            Enable maximum stay for people.
        reset_cnt_frequency : int, optional
            Frequency for resetting the counter.
        resert_date : int, optional
            Date for counter reset.
        resert_weekday : int, optional
            Weekday for counter reset.
        resert_tome_hour : int, optional
            Hour for counter reset.
        resert_tome_minute : int, optional
            Minute for counter reset (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Edit'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_task_group(self,
                          # TODO not working
                          ids: str = None) -> dict[str, object] | str:
        """
        Delete a people counting task group.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task group IDs to delete.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_count_people_task_in_groups(self,
                                          # TODO not working
                                          ids: str = None) -> dict[str, object] | str:
        """
        Enable people counting tasks in specified groups.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task group IDs to enable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_count_people_task_in_groups(self,
                                         # TODO not working
                                         ids: str = None) -> dict[str, object] | str:
        """
        Disable people counting tasks in specified groups.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task group IDs to disable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_number_counting_task_group(self,
                                       # TODO not working
                                       id: int = None) -> dict[str, object] | str:
        """
        Get the people count for a specific task group.

        Parameters
        ----------
        id : int, optional
            ID of the task group.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetPeopleCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_recording_file_result(self,
                                   # TODO not working
                                   id: int = None) -> dict[str, object] | str:
        """
        Reset the people count for a specific IVA task group.

        Parameters
        ----------
        id : int, optional
            ID of the IVA task group.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ResetPeopleCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_face_list_task(self,
                           ids: str = None,
                           ownerDsId: int = None,
                           blOnlyEnableDs: bool = None,
                           ) -> dict[str, object] | str:  # TODO not working
        """
        Retrieve the list of face detection tasks.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task IDs to filter.
        ownerDsId : int, optional
            ID of the owner DiskStation.
        blOnlyEnableDs : bool, optional
            Whether to include only enabled DiskStations.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_or_edit_task(self,
                            id: int = None,
                            id_on_rec_server: int = None,
                            camera_id: int = None,
                            camera_id_on_rec: int = None,
                            owner_ds_id: int = None,
                            enable: bool = None,
                            blEditMode: bool = None,
                            stream_profile: int = None,
                            name: str = None,
                            similarity: float = None,
                            allowed_color: int = None,
                            allowed_list: Any = None,
                            blocked_color: int = None,
                            blocked_list: Any = None,
                            vip_color: int = None,
                            vip_list: Any = None,
                            recognized_color: int = None,
                            unrecognized_color: int = None,
                            deleted: bool = None,
                            det_region: str = None,
                            det_region_cnt: int = None,
                            region_type: int = None,
                            display_info: int = None,
                            display_type: int = None,
                            frame_display_info: int = None,
                            enable_min_ogj_size: bool = None,
                            min_ogj_size: float = None,
                            post_rec_time: int = None,
                            pre_rec_time: int = None,
                            schedule: str = None,
                            scheduleOn: bool = None,
                            # TODO not working
                            ignore_bad_quality: bool = None) -> dict[str, object] | str:
        """
        Create or edit a face detection task.

        Parameters
        ----------
        id : int, optional
            Task ID.
        id_on_rec_server : int, optional
            Task ID on the recording server.
        camera_id : int, optional
            Camera ID.
        camera_id_on_rec : int, optional
            Camera ID on the recording server.
        owner_ds_id : int, optional
            Owner DiskStation ID.
        enable : bool, optional
            Whether to enable the task.
        blEditMode : bool, optional
            Edit mode flag.
        stream_profile : int, optional
            Stream profile index.
        name : str, optional
            Name of the task.
        similarity : float, optional
            Similarity threshold for face recognition.
        allowed_color : int, optional
            Color code for allowed faces.
        allowed_list : Any, optional
            List of allowed faces.
        blocked_color : int, optional
            Color code for blocked faces.
        blocked_list : Any, optional
            List of blocked faces.
        vip_color : int, optional
            Color code for VIP faces.
        vip_list : Any, optional
            List of VIP faces.
        recognized_color : int, optional
            Color code for recognized faces.
        unrecognized_color : int, optional
            Color code for unrecognized faces.
        deleted : bool, optional
            Whether the task is deleted.
        det_region : str, optional
            Detection region.
        det_region_cnt : int, optional
            Number of detection regions.
        region_type : int, optional
            Type of region.
        display_info : int, optional
            Display information.
        display_type : int, optional
            Display type.
        frame_display_info : int, optional
            Frame display information.
        enable_min_ogj_size : bool, optional
            Enable minimum object size.
        min_ogj_size : float, optional
            Minimum object size.
        post_rec_time : int, optional
            Post-recording time in seconds.
        pre_rec_time : int, optional
            Pre-recording time in seconds.
        schedule : str, optional
            Task schedule.
        scheduleOn : bool, optional
            Whether the schedule is enabled.
        ignore_bad_quality : bool, optional
            Ignore bad quality flag (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_face_task(self,
                         ids: str = None,
                         # TODO not working
                         keepRecording: bool = None) -> dict[str, object] | str:
        """
        Delete one or more face detection tasks.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task IDs to delete.
        keepRecording : bool, optional
            Whether to keep the associated recordings (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_task_to_start_detection_recording(self,
                                                 # TODO not working
                                                 ids: str = None) -> dict[str, object] | str:
        """
        Enable face detection tasks to start detection and recording.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task IDs to enable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_task_to_stop_detection_recording(self,
                                                 # TODO not working
                                                 ids: str = None) -> dict[str, object] | str:
        """
        Disable face detection tasks to stop detection and recording.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of task IDs to disable.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DisableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_task_with_privilege_to_watch(self,
                                          # TODO not working
                                          ids: int = None) -> dict[str, object] | str:
        """
        List face detection tasks with privilege to watch.

        Parameters
        ----------
        ids : int, optional
            Task group ID to filter.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ListPlayableTsk'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_face_group(self,
                          name: str = None,
                          description: str = None,
                          # TODO not working
                          update_registered_face: Any = None) -> dict[str, object] | str:
        """
        Create a new face group.

        Parameters
        ----------
        name : str, optional
            Name of the face group.
        description : str, optional
            Description of the face group.
        update_registered_face : Any, optional
            Registered face update information (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CreateFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_face_grooup(self,
                            # TODO not working
                            ids: Any = None) -> dict[str, object] | str:
        """
        Delete (disable) one or more face groups.

        Parameters
        ----------
        ids : Any, optional
            IDs of the face groups to delete (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'DeleteFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def edit_face_group(self,
                        name: str = None,
                        description: str = None,
                        update_registered_face: Any = None,
                        id: int = None) -> dict[str, object] | str:  # TODO not working
        """
        Edit an existing face group.

        Parameters
        ----------
        name : str, optional
            Name of the face group.
        description : str, optional
            Description of the face group.
        update_registered_face : Any, optional
            Registered face update information.
        id : int, optional
            ID of the face group to edit.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EditFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_face_group_list(self,
                            id_only: bool = None,
                            # TODO not working
                            filter: Any = None) -> dict[str, object] | str:
        """
        Retrieve the list of face groups.

        Parameters
        ----------
        id_only : bool, optional
            Whether to return only IDs.
        filter : Any, optional
            Filter criteria (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_face_groups(self,
                          # TODO not working
                          filter: Any = None) -> dict[str, object] | str:
        """
        Count the number of face groups.

        Parameters
        ----------
        filter : Any, optional
            Filter criteria (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def detect_faces_image(self,
                           image_data: str = None,
                           # TODO not working
                           image_size: int = None) -> dict[str, object] | str:
        """
        Detect faces in an image.

        Parameters
        ----------
        image_data : str, optional
            Base64-encoded image data.
        image_size : int, optional
            Size of the image (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'DetectImageFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_registered_face(self,
                               account: str = None,
                               name: str = None,
                               description: str = None,
                               image_data: str = None,
                               image_size: int = None,
                               face: Any = None,
                               update_face_group: Any = None,
                               captured_face_id: int = None,
                               update_unrecognized_captured_face: bool = None,
                               # TODO not working
                               append_image_data: bool = None) -> dict[str, object] | str:
        """
        Create a new registered face.

        Parameters
        ----------
        account : str, optional
            Account associated with the face.
        name : str, optional
            Name of the person.
        description : str, optional
            Description of the face.
        image_data : str, optional
            Base64-encoded image data.
        image_size : int, optional
            Size of the image.
        face : Any, optional
            Face data.
        update_face_group : Any, optional
            Face group update information.
        captured_face_id : int, optional
            ID of the captured face.
        update_unrecognized_captured_face : bool, optional
            Whether to update unrecognized captured face.
        append_image_data : bool, optional
            Append image data flag (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CreateRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_registered_face(self,
                               # TODO not working
                               ids: Any = None) -> dict[str, object] | str:
        """
        Delete one or more registered faces.

        Parameters
        ----------
        ids : Any, optional
            IDs of the registered faces to delete (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'DeleteRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def edit_registered_face(self,
                             id: int = None,
                             account: str = None,
                             name: str = None,
                             description: str = None,
                             image_data: str = None,
                             image_size: int = None,
                             face: Any = None,
                             update_face_group: Any = None,
                             captured_face_id: int = None,
                             update_unrecognized_captured_face: bool = None,
                             append_image_data: bool = None,
                             ) -> dict[str, object] | str:  # TODO not working
        """
        Edit an existing registered face.

        Parameters
        ----------
        id : int, optional
            ID of the registered face.
        account : str, optional
            Account associated with the face.
        name : str, optional
            Name of the person.
        description : str, optional
            Description of the face.
        image_data : str, optional
            Base64-encoded image data.
        image_size : int, optional
            Size of the image.
        face : Any, optional
            Face data.
        update_face_group : Any, optional
            Face group update information.
        captured_face_id : int, optional
            ID of the captured face.
        update_unrecognized_captured_face : bool, optional
            Whether to update unrecognized captured face.
        append_image_data : bool, optional
            Append image data flag.

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'EditRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_registered_face(self,
                             id_only: bool = None,
                             filter: Any = None,
                             append_image_data: bool = None,
                             ) -> dict[str, object] | str:  # TODO not working
        """
        List registered faces.

        Parameters
        ----------
        id_only : bool, optional
            Whether to return only IDs.
        filter : Any, optional
            Filter criteria.
        append_image_data : bool, optional
            Whether to append image data (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'ListRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_registered_face(self,
                              # TODO not working
                              filter: Any = None) -> dict[str, object] | str:
        """
        Count the number of registered faces.

        Parameters
        ----------
        filter : Any, optional
            Filter criteria (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'CountRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def search_registered_face(self,
                               keywords: str = None,
                               # TODO not working
                               append_image_data: bool = None) -> dict[str, object] | str:
        """
        Search for registered faces by keywords.

        Parameters
        ----------
        keywords : str, optional
            Search keywords.
        append_image_data : bool, optional
            Whether to append image data (not working).

        Returns
        -------
        dict of str to object or str
            API response from the request.
        """
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'SearchRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_face_result_list(self,
                             filter: Any = None,
                             blIncludeSnapshot: bool = None,
                             blIncludeRegisteredFace: bool = None,
                             limit: int = None,
                             # TODO not working
                             slaveDsParam: int = None) -> dict[str, object] | str:
        """
        Retrieve a list of face recognition results.

        Parameters
        ----------
        filter : Any, optional
            Filter criteria for the face results.
        blIncludeSnapshot : bool, optional
            Whether to include snapshot images in the results.
        blIncludeRegisteredFace : bool, optional
            Whether to include registered face information.
        limit : int, optional
            Maximum number of results to return.
        slaveDsParam : int, optional
            Additional parameter for slave DiskStation (not working).

        Returns
        -------
        dict of str to object or str
            API response containing the list of face recognition results.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_face_result(self,
                           filter: Any = None,
                           # TODO not working
                           slaveDsParam: Any = None) -> dict[str, object] | str:
        """
        Delete face recognition results.

        Parameters
        ----------
        filter : Any, optional
            Filter criteria for selecting face results to delete.
        slaveDsParam : Any, optional
            Additional parameter for slave DiskStation (not working).

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the delete operation.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_face_result(self,
                         filter: Any = None,
                         # TODO not working
                         slaveDsParam: Any = None) -> dict[str, object] | str:
        """
        Lock face recognition results to prevent modification or deletion.

        Parameters
        ----------
        filter : Any, optional
            Filter criteria for selecting face results to lock.
        slaveDsParam : Any, optional
            Additional parameter for slave DiskStation (not working).

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the lock operation.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_face_result(self,
                           filter: Any = None,
                           # TODO not working
                           slaveDsParam: Any = None) -> dict[str, object] | str:
        """
        Unlock face recognition results to allow modification or deletion.

        Parameters
        ----------
        filter : Any, optional
            Filter criteria for selecting face results to unlock.
        slaveDsParam : Any, optional
            Additional parameter for slave DiskStation (not working).

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the unlock operation.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_recording_file_of_face_info(self,
                                        # TODO not working
                                        capturedFaceId: int = None) -> dict[str, object] | str:
        """
        Retrieve the recording file associated with a specific captured face.

        Parameters
        ----------
        capturedFaceId : int, optional
            ID of the captured face (not working).

        Returns
        -------
        dict of str to object or str
            API response containing the recording file information.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetEventInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_recognition_face_information(self,
                                         taskId: int = None,
                                         eventId: int = None,
                                         startTime: int = None,
                                         endTime: int = None,
                                         # TODO not working
                                         blIncludeRegisteredFace: int = None) -> dict[str, object] | str:
        """
        Retrieve analytic results for face recognition events.

        Parameters
        ----------
        taskId : int, optional
            ID of the face recognition task.
        eventId : int, optional
            ID of the event.
        startTime : int, optional
            Start time for the query (timestamp).
        endTime : int, optional
            End time for the query (timestamp).
        blIncludeRegisteredFace : int, optional
            Whether to include registered face information (not working).

        Returns
        -------
        dict of str to object or str
            API response containing analytic results.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'GetAnalyticResult'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def correct_face_result(self,
                            id: int = None,
                            # TODO not working
                            registered_face_id: int = None) -> dict[str, object] | str:
        """
        Correct the result of a face recognition event by associating it with a registered face.

        Parameters
        ----------
        id : int, optional
            ID of the face recognition result to correct.
        registered_face_id : int, optional
            ID of the registered face to associate (not working).

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the correction.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Correct'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def mark_face_result_as_stranger(self,
                                     # TODO not working
                                     ids: str = None) -> dict[str, object] | str:
        """
        Mark one or more face recognition results as strangers.

        Parameters
        ----------
        ids : str, optional
            Comma-separated list of face result IDs to mark as strangers (not working).

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the operation.
        """
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'MarkAsStranger'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def add_new_bookmark(self,
                         id: int = None,
                         eventId: int = None,
                         cameraId: int = None,
                         archId: int = None,
                         name: str = None,
                         timestamp: Any = None,
                         comment: str = None,
                         ) -> dict[str, object] | str:  # TODO not working
        """
        Add a new bookmark to a recording.

        Parameters
        ----------
        id : int, optional
            ID of the bookmark.
        eventId : int, optional
            ID of the associated event.
        cameraId : int, optional
            ID of the camera.
        archId : int, optional
            ID of the archive.
        name : str, optional
            Name of the bookmark.
        timestamp : Any, optional
            Timestamp for the bookmark.
        comment : str, optional
            Comment for the bookmark.

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the add operation.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Bookmark'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveBookmark'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_bookmark(self,
                        # TODO not working
                        bookmarkIds: Any = None) -> dict[str, object] | str:
        """
        Delete one or more bookmarks from recordings.

        Parameters
        ----------
        bookmarkIds : Any, optional
            IDs of the bookmarks to delete (not working).

        Returns
        -------
        dict of str to object or str
            API response indicating the result of the delete operation.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Bookmark'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteBookmark'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_bookmark_detail(self,
                             offset: int = None,
                             limit: int = None,
                             cameraIds: str = None,
                             fromTime: int = None,
                             # TODO not working
                             toTime: int = None) -> dict[str, object] | str:
        """
        List details of bookmarks for recordings.

        Parameters
        ----------
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Maximum number of bookmarks to return.
        cameraIds : str, optional
            Comma-separated list of camera IDs to filter.
        fromTime : int, optional
            Start time for filtering bookmarks (timestamp).
        toTime : int, optional
            End time for filtering bookmarks (not working).

        Returns
        -------
        dict of str to object or str
            API response containing bookmark details.
        """
        api_name = 'SYNO.SurveillanceStation.Recording.Bookmark'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteBookmark'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)
