from . import base_api_core

import os
import requests


class Certificate(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False):
        super(Certificate, self).__init__(ip_address, port, username, password, secure, cert_verify)

    def list_cert(self):
        api_name = 'SYNO.Core.Certificate.CRT'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1', 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def set_default_cert(self, cert_id):
        api_name = 'SYNO.Core.Certificate.CRT'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'set',
                     'as_default': 'true',
                     'desc': cert_id,
                     }

        return self.request_data(api_name, api_path, req_param)

    def upload_cert(self, serv_key="server.key", ser_cert="server.crt", ca_cert="server-ca.crt"):
        api_name = 'SYNO.Core.Certificate'
        info = self.session.app_api_list[api_name]
        api_path = info['path']
        serv_key = os.path.basename(serv_key)
        ser_cert = os.path.basename(ser_cert)
        ca_cert = os.path.basename(ca_cert)

        session = requests.session()

        payload_serv_key = open(serv_key, 'rb')
        payload_ser_cert = open(ser_cert, 'rb')
        payload_ca_cert = open(ca_cert, 'rb')

        url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=import&_sid=%s' % (
                    api_name, info['minVersion'], self._sid)

        files = {'key': (serv_key, payload_serv_key, 'application/x-iwork-keynote-sffkey'),
                 'cert': (ser_cert, payload_ser_cert, 'application/pkix-cert'),
                 'inter_cert': (ca_cert, payload_ca_cert, 'application/pkix-cert')}

        data_payload = {'id': "",
                        'desc': "",
                        'as_default': ""}

        try:
            r = session.post(url, files=files, data=data_payload)
        # close file if reading files rises an exception.
        finally:
            payload_serv_key.close()
            payload_ser_cert.close()
            payload_ca_cert.close()

        if r.status_code is 200 and r.json()['success']:
            return 'Upload Complete'
        else:
            return r.status_code, r.json()

