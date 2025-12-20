
"""
File services class for interacting with Synology DSM File services settings.
"""

from synology_api import base_api


class FileServices(base_api.BaseApi):
    """
    File services class for interacting with Synology DSM File services settings.

    Provides methods to get and set SMB, AFP, NFS, FTP, SFTP, and other file service settings.
    """

    def get_smb_settings(self):
        """
        Get SMB settings.

        Returns
        -------
        dict
            SMB settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "disable_shadow_copy": false,
                "disable_strict_allocate": false,
                "enable_access_based_share_enum": false,
                "enable_adserver": null,
                "enable_aio_read": false,
                "enable_delete_vetofiles": false,
                "enable_dirsort": false,
                "enable_durable_handles": false,
                "enable_enhance_log": false,
                "enable_fruit_locking": false,
                "enable_local_master_browser": false,
                "enable_mask": false,
                "enable_msdfs": false,
                "enable_multichannel": false,
                "enable_ntlmv1_auth": false,
                "enable_op_lock": true,
                "enable_perf_chart": false,
                "enable_reset_on_zero_vc": false,
                "enable_samba": true,
                "enable_server_signing": 0,
                "enable_smb2_leases": true,
                "enable_smb3_directory_leasing": true,
                "enable_strict_sync": false,
                "enable_symlink": true,
                "enable_syno_catia": true,
                "enable_synotify": true,
                "enable_vetofile": false,
                "enable_widelink": false,
                "offline_files_support": false,
                "smb3_directory_leasing_scope": "home_only",
                "smb_encrypt_transport": 1,
                "smb_max_protocol": 3,
                "smb_min_protocol": 1,
                "syno_wildcard_search": false,
                "vetofile": "",
                "wins": "",
                "workgroup": "WORKGROUP"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.SMB'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_afp_settings(self) -> dict:
        """
        Get AFP settings.

        Returns
        -------
        dict
            AFP settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_afp": false,
                "enable_disconnect_quick": false,
                "enable_umask": false,
                "time_machine": ""
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.AFP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_nfs_settings(self) -> dict:
        """
        Get NFS settings.

        Returns
        -------
        dict
            NFS settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_nfs": false,
                "enable_nfs_v4": false,
                "enabled_minor_ver": 0,
                "nfs_v4_domain": "",
                "read_size": 8192,
                "support_encrypt_share": 1,
                "support_major_ver": 4,
                "support_minor_ver": 1,
                "unix_pri_enable": true,
                "write_size": 8192
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.NFS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_ftp_settings(self) -> dict:
        """
        Get FTP settings.

        Returns
        -------
        dict
            FTP settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "custom_port": "55536:55899",
                "custom_port_range": false,
                "enable_ascii": false,
                "enable_fips": false,
                "enable_flow_ctrl": false,
                "enable_ftp": false,
                "enable_ftps": false,
                "enable_fxp": false,
                "ext_ip": "",
                "max_conn_per_ip": 0,
                "maxdownloadrate": 0,
                "maxuploadrate": 0,
                "modify_time_std": "utc",
                "portnum": 21,
                "timeout": 300,
                "use_ext_ip": false,
                "utf8_mode": 1
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.FTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_sftp_settings(self) -> dict:
        """
        Get SFTP settings.

        Returns
        -------
        dict
            SFTP settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable": false,
                "portnum": 22
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.FTP.SFTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_bandwidth_control_protocol_settings(self, protocol: str, schedule_plan: str) -> dict:
        """
        Get bandwidth control protocol settings.

        Parameters
        ----------
        protocol : str
            Protocol name (e.g. "FTP", "NetworkBackup").
        schedule_plan : str
            Schedule plan, a 128-bit binary string.

        Returns
        -------
        dict
            Bandwidth control protocol settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "policy": "disabled",
                "protocol": "FTP",
                "schedule_plan": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.BandwidthControl.Protocol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get',
            'protocol': protocol
        }
        return self.request_data(api_name, api_path, req_param)

    def get_network_backup_settings(self) -> dict:
        """
        Get network backup settings.

        Returns
        -------
        dict
            Network backup settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable": false,
                "enable_custom_config": false,
                "enable_rsync_account": false,
                "rsync_sshd_port": "22"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Backup.Service.NetworkBackup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_domain_settings(self) -> dict:
        """
        Get domain settings.

        Returns
        -------
        dict
            Domain settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_domain": false
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Directory.Domain'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_service_discovery_settings(self) -> dict:
        """
        Get service discovery settings.

        Returns
        -------
        dict
            Service discovery settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_afp_time_machine": false,
                "enable_smb_time_machine": false,
                "time_machine_disable_shares": [],
                "time_machine_shares": []
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.ServiceDiscovery'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_wstransfer_settings(self) -> dict:
        """
        Get WSTransfer settings.

        Returns
        -------
        dict
            WSTransfer settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_wstransfer": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.ServiceDiscovery.WSTransfer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_reflink_copy_settings(self) -> dict:
        """
        Get reflink copy settings.

        Returns
        -------
        dict
            Reflink copy settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "reflink_copy_enable": false
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.ReflinkCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_tftp_settings(self) -> dict:
        """
        Get TFTP settings.

        Returns
        -------
        dict
            TFTP settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "enable": false,
                "enable_log": false,
                "endip": "255.255.255.255",
                "permission": "r",
                "root_path": "",
                "startip": "0.0.0.0",
                "timeout": 3
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.TFTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def clean_smb_cache(self) -> dict:
        """
        Clean SMB cache.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.SMB'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'clean_cache'
        }
        return self.request_data(api_name, api_path, req_param)

    def set_afp_settings(self, enable: bool, enable_transfer_log: bool, enable_umask: bool, enable_disconnect_quick: bool) -> dict:
        """
        Set AFP settings.

        Parameters
        ----------
        enable : bool
            Enable or disable AFP.
        enable_transfer_log : bool
            Enable or disable transfer log.
        enable_umask : bool
            Enable or disable umask.
        enable_disconnect_quick : bool
            Enable or disable quick disconnect.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.AFP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'enable_transfer_log': enable_transfer_log,
            'enable_umask': enable_umask,
            'enable_disconnect_quick': enable_disconnect_quick
        }
        return self.request_data(api_name, api_path, req_param)

    def set_nfs_settings(self, enable: bool, max_protocol: int, enable_v4: bool, enabled_minor_ver: int) -> dict:
        """
        Set NFS settings.

        Parameters
        ----------
        enable : bool
            Enable or disable NFS.
        max_protocol : int
            Maximum NFS protocol version.
        enable_v4 : bool
            Enable or disable NFSv4.
        enabled_minor_ver : int
            Enabled minor version.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.NFS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'max_protocol': max_protocol,
            'enable_v4': enable_v4,
            'enabled_minor_ver': enabled_minor_ver
        }
        return self.request_data(api_name, api_path, req_param)

    def get_ftp_security_settings(self) -> dict:
        """
        Get FTP security settings.

        Returns
        -------
        dict
            FTP security settings data.

        Examples
        --------
        ```json
        {
            "data": {
                "anonymous": false,
                "anonymous_chroot": false,
                "anonymous_chroot_share": "",
                "enable_umask": false,
                "user_chroot": false
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.FTP.Security'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_ftp_security_share_list(self) -> dict:
        """
        Get FTP security share list.

        Returns
        -------
        dict
            FTP security share list data.

        Examples
        --------
        ```json
        {
            "data":{
                "share": [
                    "docker"
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.FTP.Security.ShareList'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def set_ftp_settings(self, enable_ftp: bool, enable_ftps: bool,
                         timeout: int = 300, portnum: int = 21, custom_port_range: bool = False,
                         use_ext_ip: bool = False, enable_fxp: bool = True, enable_ascii: bool = True,
                         utf8_mode: int = 1, modify_time_std: str = "utc", custom_port: str = "55536:55899",
                         external_ip: str = "default"
                         ) -> dict:
        """
        Set FTP settings.

        Parameters
        ----------
        enable_ftp : bool
            Enable or disable FTP.
        enable_ftps : bool
            Enable or disable FTPS.
        timeout : int, optional
            Timeout in seconds. Default is 300.
        portnum : int, optional
            Port number. Default is 21.
        custom_port_range : bool, optional
            Enable or disable custom port range. Default is False.
        use_ext_ip : bool, optional
            Enable or disable external IP. Default is False.
        enable_fxp : bool, optional
            Enable or disable FXP. Default is True.
        enable_ascii : bool, optional
            Enable or disable ASCII mode. Default is True.
        utf8_mode : int, optional
            UTF-8 mode (0: disable, 1: Auto, 2: Force). Default is 1.
        modify_time_std : str, optional
            Modify time standard ("utc", "local"). Default is "utc".
        custom_port : str, optional
            Custom port range. Default is "55536:55899".
        external_ip : str, optional
            External IP address. Default is "default".

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.FTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable_ftp': enable_ftp,
            'enable_ftps': enable_ftps,
            'timeout': timeout,
            'portnum': portnum,
            'custom_port_range': custom_port_range,
            'use_ext_ip': use_ext_ip,
            'enable_fxp': enable_fxp,
            'enable_ascii': enable_ascii,
            'utf8_mode': utf8_mode,
            'modify_time_std': modify_time_std,
            'custom_port': custom_port,
            'external_ip': external_ip
        }
        return self.request_data(api_name, api_path, req_param)

    def set_sftp_settings(self, enable: bool, portnum: int = 22) -> dict:
        """
        Set SFTP settings.

        Parameters
        ----------
        enable : bool
            Enable or disable SFTP.
        portnum : int, optional
            Port number. Default is 22.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.FTP.SFTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'portnum': portnum,
            'sftp_portnum': portnum
        }
        return self.request_data(api_name, api_path, req_param)

    def set_rsync_settings(self, enable: bool, port: int = 22) -> dict:
        """
        Set rsync settings.

        Parameters
        ----------
        enable : bool
            Enable or disable rsync.
        port : int, optional
            Rsync SSHD port. Default is 22.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Backup.Service.NetworkBackup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'rsync_sshd_port': port
        }
        return self.request_data(api_name, api_path, req_param)

    def set_reflink_copy_settings(self, reflink_copy_enable: bool) -> dict:
        """
        Set reflink copy settings.

        Parameters
        ----------
        reflink_copy_enable : bool
            Enable or disable reflink copy.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.FileServ.ReflinkCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'reflink_copy_enable': reflink_copy_enable
        }
        return self.request_data(api_name, api_path, req_param)

    def set_tftp_settings(self, enable: bool, root_path: str) -> dict:
        """
        Set TFTP settings.

        Parameters
        ----------
        enable : bool
            Enable or disable TFTP.
        root_path : str
            Root path for TFTP. Path must be a valid directory.

        Returns
        -------
        dict
            Result of the operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.TFTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'root_path': root_path
        }
        return self.request_data(api_name, api_path, req_param)

    pass
