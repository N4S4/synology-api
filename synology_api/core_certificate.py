from . import base_api_core

import os
import requests
import json


class Certificate(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(Certificate, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        self._debug = debug

    def _base_certificate_methods(self, method, cert_id=None, ids=None):
        available_method = ['list', 'set', 'delete']
        if method not in available_method:
            # print error here
            return f"Method {method} no supported."

        api_name = 'SYNO.Core.Certificate.CRT'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': method}

        if 'set' == method and cert_id:
            req_param.update(
                {'as_default': 'true',
                 'desc': '\"\"',
                 'id': f"\"{cert_id}\""
                 })
        elif 'delete' == method and ids:
            ids = json.dumps(ids)
            req_param.update({"ids": ids})

        return self.request_data(api_name, api_path, req_param)

    def list_cert(self):
        return self._base_certificate_methods('list')

    def set_default_cert(self, cert_id):
        return self._base_certificate_methods('set', cert_id)

    def delete_certificate(self, ids):
        if isinstance(ids, str):
            ids = [ids]
        return self._base_certificate_methods('delete', ids=ids)

    def upload_cert(self, serv_key="server.key", ser_cert="server.crt", ca_cert=None, set_as_default=True, cert_id=None, desc=None):
        api_name = 'SYNO.Core.Certificate'
        info = self.session.app_api_list[api_name]
        api_path = info['path']
        serv_key = os.path.abspath(serv_key)
        ser_cert = os.path.abspath(ser_cert)
        # ca_cert is optional argument for upload cert
        ca_cert = os.path.abspath(ca_cert) if ca_cert else None

        session = requests.session()

        url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=import&_sid=%s' % (
                    api_name, info['minVersion'], self._sid)

        if cert_id:
            print("update exist cert: " + cert_id)
        data_payload = {'id': cert_id or '', 'desc': desc or '', 'as_default': 'true' if set_as_default else 'false'}

        with open(serv_key, 'rb') as payload_serv_key, open(ser_cert, 'rb') as payload_ser_cert:
            files = {'key': (serv_key, payload_serv_key, 'application/x-iwork-keynote-sffkey'),
                     'cert': (ser_cert, payload_ser_cert, 'application/pkix-cert')}
            if ca_cert:
                with open(ca_cert, 'rb') as payload_ca_cert:
                    files['inter_cert'] = (ca_cert, payload_ca_cert, 'application/pkix-cert')
                    r = session.post(url, files=files, data=data_payload, verify=self.session.verify_cert_enabled())
            else:
                r = session.post(url, files=files, data=data_payload, verify=self.session.verify_cert_enabled())

        if 200 == r.status_code and r.json()['success']:
            if self._debug is True:
                print('Certificate upload successful.')

        return r.status_code, r.json()
