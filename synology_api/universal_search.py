from typing import Optional
from synology_api import auth
from urllib import parse


class UniversalSearch:
    def __init__(self,
                    ip_address : str,
                    port : str,
                    username : str,
                    password : str,
                    secure : bool = False,
                    cert_verify : bool = False,
                    dsm_version : int = 7,
                    debug : bool = True,
                    otp_code : Optional[str] = None
                ) -> None:
        self.session : auth.Authentication = auth.Authentication(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        self.session.login('Finder')
        self.session.get_api_list('Finder')
        self.request_data : function = self.session.request_data
        self.finder_list : dict[str, object] = self.session.app_api_list
        self._sid : str = self.session.sid
        self.base_url : str = self.session.base_url

    def search(self, keyword:str) -> dict[str, object]:
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
