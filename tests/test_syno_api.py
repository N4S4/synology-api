import datetime
import json
from unittest import TestCase
import unittest
from synology_api.filestation import FileStation
from synology_api.surveillancestation import SurveillanceStation
import os, pathlib


def parse_config(config_path) -> dict[str, str]:
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data


class TestSynoApi(TestCase):
    config: dict[str, str]

    def setUp(self):
        self.config = parse_config(
            os.path.realpath(
                os.path.join(
                    pathlib.Path(__file__).parent.resolve(),
                    './resources/config-test.json'
                )
            )
        )


    def test_syno_filestation_login(self):
        fs = FileStation(ip_address=self.config["synology_ip"], port=self.config["synology_port"],
                         username=self.config["synology_user"],
                         password=self.config["synology_password"],
                         secure=bool(self.config["synology_secure"]), cert_verify=False,
                         dsm_version=int(self.config["dsm_version"]), debug=True,
                         otp_code=self.config["otp_code"])

        self.assertIsNotNone(fs)
        self.assertIsNotNone(fs.session)
        self.assertIsNotNone(fs.session.sid)
        self.assertIsNot(fs.session.sid, '')
        shares_list = fs.get_list_share()
        self.assertIsNotNone(shares_list)
        self.assertEqual(shares_list.__len__(), 2)

    def test_syno_surveillancestation_login(self):
        ss = SurveillanceStation(ip_address=self.config["synology_ip"], port=self.config["synology_port"],
                                 username=self.config["synology_user"],
                                 password=self.config["synology_password"],
                                 secure=bool(self.config["synology_secure"]), cert_verify=False,
                                 dsm_version=int(self.config["dsm_version"]), debug=True,
                                 otp_code=self.config["otp_code"])

        self.assertIsNotNone(ss)
        self.assertIsNotNone(ss.session)
        self.assertIsNotNone(ss.session.sid)
        self.assertIsNot(ss.session.sid, '')
        ss_info = ss.surveillance_station_info()
        self.assertIsNotNone(ss_info)
        ss_info_data = ss_info['data']
        self.assertIsNotNone(ss_info_data)
        self.assertEqual(ss_info_data['path'], '/webman/3rdparty/SurveillanceStation/')


if __name__ == '__main__':
    unittest.main()
