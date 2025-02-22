from .ControlPanel import ControlPanel
from .FileStation import FileStation

from synology_api import base_api

class DSM(base_api.BaseApi):
    _ctrl_panel = None
    _file_station = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @property
    def ControlPanel(self):
        if self._ctrl_panel is None:
            # Create ControlPanel instance without calling __init__
            self._ctrl_panel = ControlPanel.__new__(ControlPanel)
            # Share the state
            self._ctrl_panel.__dict__ = self.__dict__
        return self._ctrl_panel

    @property
    def FileStation(self):
        if self._file_station is None:
            # Create FileStation instance without calling __init__
            self._file_station = FileStation.__new__(FileStation)
            # Share the state
            self._file_station.__dict__ = self.__dict__
        return self._file_station