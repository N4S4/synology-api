from __future__ import annotations
from typing import Optional, Any
from . import base_api


class UniversalSearch(base_api.BaseApi):

    def search(self, keyword: str) -> dict[str, object] | str:
        api_name = 'SYNO.Finder.FileIndexing.Search'
        info = self.gen_list[api_name]
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
