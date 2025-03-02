from .ControlPanel import ControlPanel
from .Package.FileStation import FileStation
from .Package.PackageCenter import PackageCenter

from synology_api import base_api

class DSM(base_api.BaseApi):
    _ctrl_panel = None
    _file_station = None
    _package_center = None
    
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
    
    @property
    def PackageCenter(self):
        if self._package_center is None:
            # Create PackageCenter instance without calling __init__
            self._package_center = PackageCenter.__new__(PackageCenter)
            # Share the state
            self._package_center.__dict__ = self.__dict__
        return self._package_center