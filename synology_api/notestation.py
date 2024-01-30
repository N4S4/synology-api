from __future__ import annotations
from typing import Optional
from . import base_api


class NoteStation(base_api.BaseApi):

    def settings_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO success response but need more info about it
    '''def notestation_settings_init(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'init'}

        return self.request_data(api_name, api_path, req_param)'''

    def info(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notebooks_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Notebook'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def tags_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Tag'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def shortcuts(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Shortcut'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def todo(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Todo'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def smart(self) -> dict[str, object] | str:  # TODO need to investigate for additional params
        api_name = 'SYNO.NoteStation.Smart'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def note_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def specific_note_id(self, note_id) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']

        if note_id is None:
            return 'note_id must be specify, run note_list() and copy object_id that you need'

        req_param = {'version': info['maxVersion'], 'method': 'get', 'object_id': note_id}

        return self.request_data(api_name, api_path, req_param)

    # TODO success response but need additional data
    '''def note_idle(self) -> dict[str, object] | str:
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'idle'}

        return self.request_data(api_name, api_path, req_param)'''
