"""
Main entry point for Synology DSM API access.
"""

from .ControlPanel import ControlPanel
from .Package.FileStation import FileStation
from .Package.PackageCenter import PackageCenter
from synology_api import base_api


class DSM(base_api.BaseApi):
    """
    Main entry point for Synology DSM API access. Provides access to ControlPanel, FileStation, and PackageCenter APIs.

    Parameters
        ----------
        *args : tuple
            Positional arguments passed to BaseApi.
        **kwargs : dict
            Keyword arguments passed to BaseApi.
    """
    _ctrl_panel = None
    _file_station = None
    _package_center = None

    def __init__(self, *args, **kwargs):
        """
        Initialize DSM API wrapper.

        Parameters
        ----------
        *args : tuple
            Positional arguments passed to BaseApi.
        **kwargs : dict
            Keyword arguments passed to BaseApi.
        """
        super().__init__(*args, **kwargs)

    @property
    def ControlPanel(self):
        """
        ControlPanel: ControlPanel.

        Returns
        -------
        ControlPanel
            Instance of the ControlPanel API, sharing the same state as DSM.
        """
        if self._ctrl_panel is None:
            # Create ControlPanel instance without calling __init__
            self._ctrl_panel = ControlPanel.__new__(ControlPanel)
            # Share the state
            self._ctrl_panel.__dict__ = self.__dict__
        return self._ctrl_panel

    @property
    def FileStation(self):
        """
        FileStation: FileStation.

        Returns
        -------
        FileStation
            Instance of the FileStation API, sharing the same state as DSM.
        """
        if self._file_station is None:
            # Create FileStation instance without calling __init__
            self._file_station = FileStation.__new__(FileStation)
            # Share the state
            self._file_station.__dict__ = self.__dict__
        return self._file_station

    @property
    def PackageCenter(self):
        """
        PackageCenter: PackageCenter.

        Returns
        -------
        PackageCenter
            Instance of the PackageCenter API, sharing the same state as DSM.
        """
        if self._package_center is None:
            # Create PackageCenter instance without calling __init__
            self._package_center = PackageCenter.__new__(PackageCenter)
            # Share the state
            self._package_center.__dict__ = self.__dict__
        return self._package_center
