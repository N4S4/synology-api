from . import base_api_core


class VPN(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7,
                 debug=True, otp_code=None):
        super(VPN, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def settings_list(self):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status_load'}

        return self.request_data(api_name, api_path, req_param)

    def active_connections_list(self, sort='login_time', dir='DESC', start=0, limit=100):
        api_name = 'SYNO.VPNServer.Management.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'enum', 'sort': sort, 'dir': dir, 'start': start,
                     'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def log_list(self, start=0, limit=50, prtltype=0):
        api_name = 'SYNO.VPNServer.Management.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'start': start, 'limit': limit,
                     'prtltype': prtltype}

        return self.request_data(api_name, api_path, req_param)

    def network_interface_setting(self):
        api_name = 'SYNO.VPNServer.Management.Interface'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def security_autoblock_setting(self):
        api_name = 'SYNO.Core.Security.AutoBlock'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def permission_setting(self, start=0, limit=100):
        api_name = 'SYNO.VPNServer.Management.Account'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'action': 'enum', 'start': str(start),
                     'limit': str(limit)}

        return self.request_data(api_name, api_path, req_param)

    def pptp_settings_info(self):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'serv_type': 'pptp'}

        return self.request_data(api_name, api_path, req_param)

    def openvpn_settings_info(self):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'serv_type': 'openvpn'}

        return self.request_data(api_name, api_path, req_param)

    def l2tp_settings_info(self):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'serv_type': 'l2tp'}

        return self.request_data(api_name, api_path, req_param)

    # TODO not working {'error': {'code': 600}, 'success': False} response
    '''def pptp_settings_setup(self, serv_type='pptp', serv_enable=True, serv_ip='10.0.0.0', serv_range=5, auth_type=2,
                            auth_conn=3, mppe_type=1, mtu=1400, dns_check=False, dns='192.168.1.1'):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']

        if serv_enable:
            serv_enable = 'true'
        elif not serv_enable:
            serv_enable = 'false'
        else:
            return 'serv_enable must be True or False'

        if dns_check:
            dns_check = 'true'
        elif not dns_check:
            dns_check = 'false'
        else:
            return 'dns_check must be True or False'

        req_param = {'version': info['maxVersion'], 'method': 'apply', 'serv_type': serv_type,
                     'serv_enable': serv_enable, 'serv_ip': serv_ip, 'serv_range': serv_range,
                     'auth_type': auth_type, 'auth_conn': auth_conn, 'mppe_type': mppe_type, 'mtu': mtu,
                     'dns_check': dns_check, 'dns': dns}

        return self.request_data(api_name, api_path, req_param)'''

    # TODO not working {'error': {'code': 600}, 'success': False} response
    '''def openvpn_settings_setup(self, serv_type='openvpn', serv_enable=True, serv_ip='10.8.0.0', serv_range=5,
                               comp_enable=True, push_route_enable=False, tls_auth_key=False, verify_server_cn=False,
                               auth_conn=3, port=1194, protocol='udp', encryption='AES-256-CBC', authentication= 'SHA512',
                               enable_ipv6_server=False, ipv6_prefix='', mssfix_value=1450):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']

        if serv_enable:
            serv_enable = 'true'
        elif not serv_enable:
            serv_enable = 'false'
        else:
            return 'serv_enable must be True or False'

        if comp_enable:
            comp_enable = 'true'
        elif not comp_enable:
            comp_enable = 'false'
        else:
            return 'comp_enable must be True or False'

        if push_route_enable:
            push_route_enable = 'true'
        elif not push_route_enable:
            push_route_enable = 'false'
        else:
            return 'push_route_enable must be True or False'

        if tls_auth_key:
            tls_auth_key = 'true'
        elif not tls_auth_key:
            tls_auth_key = 'false'
        else:
            return 'tls_auth_key must be True or False'

        if verify_server_cn:
            verify_server_cn = 'true'
        elif not verify_server_cn:
            verify_server_cn = 'false'
        else:
            return 'verify_server_cn must be True or False'

        if enable_ipv6_server:
            enable_ipv6_server = 'true'
        elif not enable_ipv6_server:
            enable_ipv6_server = 'false'
        else:
            return 'enable_ipv6_server must be True or False'

        req_param = {'version': info['maxVersion'], 'method': 'apply', 'serv_type': serv_type,
                     'serv_enable': serv_enable, 'serv_ip': serv_ip, 'serv_range': serv_range,
                     'comp_enable': comp_enable, 'push_route_enable': push_route_enable, 'tls_auth_key': tls_auth_key,
                     'verify_server_cn': verify_server_cn, 'auth_conn': auth_conn, 'port': port, 'protocol': protocol,
                     'encryption': encryption, 'authentication': authentication,
                     'enable_ipv6_server': enable_ipv6_server, 'ipv6_prefix': ipv6_prefix, 'mssfix_value': mssfix_value}

        return self.request_data(api_name, api_path, req_param)'''

    # TODO not working {'error': {'code': 600}, 'success': False} response
    '''def l2tp_settings_setup(self, serv_type='l2tp', serv_enable=True, serv_ip='10.2.0.0', serv_range=5,
                               auth_type=2, auth_conn=3, mtu=1400, dns_check=False, dns='192.168.1.1', preshared_key='',
                               preshared_key_confirm='', sha2_truncbug=True, kernel_mode=True):
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']

        if serv_enable:
            serv_enable = 'true'
        elif not serv_enable:
            serv_enable = 'false'
        else:
            return 'serv_enable must be True or False'

        if dns_check:
            dns_check = 'true'
        elif not dns_check:
            dns_check = 'false'
        else:
            return 'dns_check must be True or False'

        if sha2_truncbug:
            sha2_truncbug = 'true'
        elif not sha2_truncbug:
            sha2_truncbug = 'false'
        else:
            return 'sha2_truncbug must be True or False'

        if kernel_mode:
            kernel_mode = 'true'
        elif not kernel_mode:
            kernel_mode = 'false'
        else:
            return 'kernel_mode must be True or False'

        req_param = {'version': info['maxVersion'], 'method': 'apply', 'serv_type': serv_type,
                     'serv_enable': serv_enable, 'serv_ip': serv_ip, 'serv_range': serv_range,
                     'auth_type': auth_type, 'auth_conn': auth_conn, 'mtu': mtu, 'dns_check': dns_check, 'dns': dns,
                     'preshared_key': preshared_key, 'preshared_key_confirm': preshared_key_confirm,
                     'sha2_truncbug': sha2_truncbug, 'kernel_mode': kernel_mode}

        return self.request_data(api_name, api_path, req_param)'''

