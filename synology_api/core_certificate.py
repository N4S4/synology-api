from __future__ import annotations
from io import BytesIO
from typing import Optional

from . import base_api

import os
import requests
import json


class Certificate(base_api.BaseApi):
    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None
                 ) -> None:
        super(Certificate, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug,
                                          otp_code)
        self._debug: bool = debug

    def _base_certificate_methods(self,
                                  method: str,
                                  cert_id: Optional[str] = None,
                                  ids: Optional[str | list[str]] = None
                                  ) -> str | dict[str, object]:
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

    def list_cert(self) -> dict[str, object]:
        return self._base_certificate_methods('list')

    def set_default_cert(self, cert_id: str) -> dict[str, object]:
        return self._base_certificate_methods('set', cert_id)

    def delete_certificate(self, ids: str | list[str]) -> dict[str, object]:
        if isinstance(ids, str):
            ids = [ids]
        return self._base_certificate_methods('delete', ids=ids)

    def upload_cert(self,
                    serv_key: str = "server.key",
                    ser_cert: str = "server.crt",
                    ca_cert: Optional[str] = None,
                    set_as_default: bool = True,
                    cert_id: Optional[str] = None,
                    desc: Optional[str] = None
                    ) -> tuple[int, dict[str, object]]:
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
        data_payload = {'id': cert_id or '', 'desc': desc or '', 'as_default': 'true' if set_as_default else ''}

        with open(serv_key, 'rb') as payload_serv_key, open(ser_cert, 'rb') as payload_ser_cert:
            files = {'key': (serv_key, payload_serv_key, 'application/x-x509-ca-cert'),
                     'cert': (ser_cert, payload_ser_cert, 'application/x-x509-ca-cert')}
            if ca_cert:
                with open(ca_cert, 'rb') as payload_ca_cert:
                    files['inter_cert'] = (ca_cert, payload_ca_cert, 'application/x-x509-ca-cert')
                    r = session.post(url, files=files, data=data_payload, verify=self.session.verify_cert_enabled(), headers={"X-SYNO-TOKEN":self.session._syno_token})
            else:
                r = session.post(url, files=files, data=data_payload, verify=self.session.verify_cert_enabled(), headers={"X-SYNO-TOKEN":self.session._syno_token})

        if 200 == r.status_code and r.json()['success']:
            if self._debug is True:
                print('Certificate upload successful.')

        return r.status_code, r.json()

    def set_certificate_for_service(self,
                                    cert_id: str,
                                    service_name: str = "DSM Desktop Service",
                                    ) -> tuple[int, dict[str, object]]:
        api_name = 'SYNO.Core.Certificate.Service'
        info = self.session.app_api_list[api_name]
        api_path = info['path']

        # retrieve existing certificates
        certs = self.list_cert()['data']['certificates']
        old_certid = ""
        for cert in certs:
            for service in cert['services']:
                # look for the previous cert
                if service['display_name'] == service_name:
                    old_certid = cert['id']
                    break

        # we need to abort, if the certificate is already set, otherwise DSM6 just removes the whole default service...
        if old_certid == cert_id:
            if self._debug is True:
                print('Certificate already set, aborting')
            return 200, "Certificate already set, aborting"

        servicedatadict = {
            "DSM Desktop Service": {
                "display_name": "DSM Desktop Service",
                "display_name_i18n": "common:web_desktop",
                "isPkg": False,
                "owner": "root",
                "service": "default",
                "subscriber": "system",
            }
        }

        # needed for DSM7
        servicedatadictdsm7 = {
            "DSM Desktop Service": {
                "multiple_cert": True,
                "user_setable": True
            }
        }

        # construct the payload
        payloaddict = {
            "settings": json.dumps([{
                "service": {**servicedatadict[service_name],
                            **(servicedatadictdsm7[service_name] if (self.session._version == 7) else {})},
                "old_id": f"{old_certid}",
                "id": f"{cert_id}"
            }], separators=(',', ':')),
            "api": f"{api_name}",
            "version": f"{info['minVersion']}",
            "method": "set"
        }

        paramdict = {
            "_sid": self._sid,
        }

        session = requests.session()

        url = ('%s%s' % (self.base_url, api_path))

        headers = {
            "X-SYNO-TOKEN": self.session._syno_token,
        }

        r = session.post(url, params=paramdict, data=payloaddict, verify=self.session.verify_cert_enabled(),
                         headers=headers)

        if 200 == r.status_code and r.json()['success']:
            if self._debug is True:
                print('Certificate set successfully.')

        return r.status_code, r.json()


    def export_cert(self, cert_id: str) -> Optional[BytesIO]:
        """Export a certificate from the Synology NAS.

            Parameters
            ----------
            cert_id : str
                The certificate ID to export. This can be found in the list_cert() method.
            
            Returns
            -------
            Optional[BytesIO]
                A BytesIO object containing the certificate archive.
        """

        api_name = "SYNO.Core.Certificate"
        info = self.session.app_api_list[api_name]
        api_path = info['path']

        session = requests.session()

        url = (
            f"{self.base_url}{api_path}?"
            f"api={api_name}&"
            f"version={info['minVersion']}&"
            f"method=export&"
            f"file=\"archive\"&"
            f"_sid={self._sid}&"
            f"id={cert_id}"
        )

        result = session.get(url, verify=self.session.verify_cert_enabled(), headers={"X-SYNO-TOKEN":self.session._syno_token})

        if result.status_code == 200:
            return BytesIO(result.content)

        return
