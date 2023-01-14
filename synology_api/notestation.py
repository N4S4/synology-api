from typing import Optional
from . import base_api_core


class NoteStation(base_api_core.Core):
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
        super(NoteStation, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        return

    def settings_info(self):
        api_name = 'SYNO.NoteStation.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO success response but need more info about it
    '''def notestation_settings_init(self):
        api_name = 'SYNO.NoteStation.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'init'}

        return self.request_data(api_name, api_path, req_param)'''

    def info(self):
        api_name = 'SYNO.NoteStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notebooks_info(self):
        api_name = 'SYNO.NoteStation.Notebook'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def tags_info(self):
        api_name = 'SYNO.NoteStation.Tag'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def shortcuts(self):
        api_name = 'SYNO.NoteStation.Shortcut'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def todo(self):
        api_name = 'SYNO.NoteStation.Todo'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def smart(self) -> dict[str, object]:  # TODO need to investigate for additional params
        api_name = 'SYNO.NoteStation.Smart'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def note_list(self):
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def specific_note_id(self, note_id:str) -> dict[str, object]:
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']

        if note_id is None:
            return 'note_id must be specify, run note_list() and copy object_id that you need'

        req_param = {'version': info['maxVersion'], 'method': 'get', 'object_id': note_id}

        return self.request_data(api_name, api_path, req_param)

    # TODO success response but need additional data
    '''def note_idle(self) -> dict[str, object]:
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'idle'}

        return self.request_data(api_name, api_path, req_param)'''
