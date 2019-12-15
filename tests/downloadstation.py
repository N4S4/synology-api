#!/usr/bin/python

from getpass import getpass
import pprint

from synology_api.downloadstation import DownloadStation

def downloadstation_test():
    pwd = getpass("Password: ")
    dls = DownloadStation('192.168.1.63', '5000', 'andrew', pwd)
    pprint.pprint(dls.session.json())
    pprint.pprint(dls.get_info())
    pprint.pprint(dls.get_config())

    return 0

import sys

if __name__ == "__main__":
    res = downloadstation_test()
    sys.exit(res)
