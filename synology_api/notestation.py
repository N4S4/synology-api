from . import base_api_core


class NoteStation(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7,
                 debug=True, otp_code=None):
        super(NoteStation, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

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

    def smart(self):  # TODO need to investigate for additional params
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

    def specific_note_id(self, note_id):
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']

        if note_id is None:
            return 'note_id must be specify, run note_list() and copy object_id that you need'

        req_param = {'version': info['maxVersion'], 'method': 'get', 'object_id': note_id}

        return self.request_data(api_name, api_path, req_param)

    # TODO success response but need additional data
    '''def note_idle(self):
        api_name = 'SYNO.NoteStation.Note'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'idle'}

        return self.request_data(api_name, api_path, req_param)'''
