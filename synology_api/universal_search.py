from __future__ import annotations
from typing import Optional, Any
from . import base_api


class UniversalSearch(base_api.BaseApi):
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

        super(UniversalSearch, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                              dsm_version, debug, otp_code)

        self.session.get_api_list('Finder')
        self.request_data: Any = self.session.request_data
        self.finder_list: Any = self.session.app_api_list
        self.base_url: str = self.session.base_url

    def search(self, keyword: str) -> dict[str, object] | str:
        api_name = 'SYNO.Finder.FileIndexing.Search'
        info = self.finder_list[api_name]
        api_path = info['path']

        req_param = {
            "query_serial": 1,
            "indice": '[]',
            "keyword": keyword,
            "orig_keyword": keyword,
            "criteria_list": '[]',
            "from": 0,
            "size": 10,
            "fields": '["SYNOMDAcquisitionMake","SYNOMDAcquisitionModel","SYNOMDAlbum","SYNOMDAperture","SYNOMDAudioBitRate","SYNOMDAudioTrackNumber","SYNOMDAuthors","SYNOMDCodecs","SYNOMDContentCreationDate","SYNOMDContentModificationDate","SYNOMDCreator","SYNOMDDurationSecond","SYNOMDExposureTimeString","SYNOMDExtension","SYNOMDFSCreationDate","SYNOMDFSName","SYNOMDFSSize","SYNOMDISOSpeed","SYNOMDLastUsedDate","SYNOMDMediaTypes","SYNOMDMusicalGenre","SYNOMDOwnerUserID","SYNOMDOwnerUserName","SYNOMDRecordingYear","SYNOMDResolutionHeightDPI","SYNOMDResolutionWidthDPI","SYNOMDTitle","SYNOMDVideoBitRate","SYNOMDIsEncrypted"]',
            "file_type": "",
            "search_weight_list": '[{"field":"SYNOMDWildcard","weight":1},{"field":"SYNOMDTextContent","weight":1},{"field":"SYNOMDSearchFileName","weight":8.5,"trailing_wildcard":"true"}]',
            "sorter_field": "relevance",
            "sorter_direction": "asc",
            "sorter_use_nature_sort": "false",
            "sorter_show_directory_first": "true",
            "api": "SYNO.Finder.FileIndexing.Search",
            "method": "search",
            "version": 1
        }

        return self.request_data(api_name, api_path, req_param)
