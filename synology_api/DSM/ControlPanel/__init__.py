"""
ControlPanel submodule for Synology DSM API. Provides access to all DSM Control Panel APIs.
"""

from .ApplicationPrivileges import ApplicationPrivileges
from .DomainLDAP import DomainLDAP
from .ExternalAccess import ExternalAccess
from .ExternalDevices import ExternalDevices
from .FileServices import FileServices
from .HardwarePower import HardwarePower
from .IndexingService import IndexingService
from .InfoCenter import InfoCenter
from .LoginPortal import LoginPortal
from .Network import Network
from .Notifications import Notifications
from .RegionalOptions import RegionalOptions
from .Security import Security
from .SharedFolder import SharedFolder
from .SynologyAccount import SynologyAccount
from .TaskScheduler import TaskScheduler
from .Security import Security
from .TerminalSNMP import TerminalSNMP
from .UpdateRestore import UpdateRestore
from .UserGroup import UserGroup

from synology_api import base_api


class ControlPanel(base_api.BaseApi):
    """
    ControlPanel submodule for Synology DSM API. Provides access to all DSM Control Panel APIs.
    """
    _app_priv = None
    _domain_ldap = None
    _ext_access = None
    _ext_devices = None
    _file_services = None
    _hard_power = None
    _idx_service = None
    _info_center = None
    _log_portal = None
    _network = None
    _notification = None
    _region_opt = None
    _security = None
    _shared_folder = None
    _syno_account = None
    _task_scheduler = None
    _terminal_snmp = None
    _update_restore = None
    _user_group = None

    @property
    def ApplicationPrivileges(self):
        """
        ControlPanel: ApplicationPrivileges.

        Returns
        -------
        ApplicationPrivileges
            Instance of the ApplicationPrivileges API, sharing the same state as DSM.
        """
        if self._app_priv is None:
            # Create ApplicationPrivileges instance without calling __init__
            self._app_priv = ApplicationPrivileges.__new__(
                ApplicationPrivileges)
            # Share the state
            self._app_priv.__dict__ = self.__dict__
        return self._app_priv

    @property
    def DomainLDAP(self):
        """
        ControlPanel: DomainLDAP.

        Returns
        -------
        DomainLDAP
            Instance of the DomainLDAP API, sharing the same state as DSM.
        """
        if self._domain_ldap is None:
            # Create DomainLDAP instance without calling __init__
            self._domain_ldap = DomainLDAP.__new__(DomainLDAP)
            # Share the state
            self._domain_ldap.__dict__ = self.__dict__
        return self._domain_ldap

    @property
    def ExternalAccess(self):
        """
        ControlPanel: ExternalAccess.

        Returns
        -------
        ExternalAccess
            Instance of the ExternalAccess API, sharing the same state as DSM.
        """
        if self._ext_access is None:
            # Create ExternalAccess instance without calling __init__
            self._ext_access = ExternalAccess.__new__(ExternalAccess)
            # Share the state
            self._ext_access.__dict__ = self.__dict__
        return self._ext_access

    @property
    def ExternalDevices(self):
        """
        ControlPanel: ExternalDevices.

        Returns
        -------
        ExternalDevices
            Instance of the ExternalDevices API, sharing the same state as DSM.
        """
        if self._ext_devices is None:
            # Create ExternalDevices instance without calling __init__
            self._ext_devices = ExternalDevices.__new__(ExternalDevices)
            # Share the state
            self._ext_devices.__dict__ = self.__dict__
        return self._ext_devices

    @property
    def FileServices(self):
        """
        ControlPanel: FileServices.

        Returns
        -------
        FileServices
            Instance of the FileServices API, sharing the same state as DSM.
        """
        if self._file_services is None:
            # Create FileServices instance without calling __init__
            self._file_services = FileServices.__new__(FileServices)
            # Share the state
            self._file_services.__dict__ = self.__dict__
        return self._file_services

    @property
    def HardwarePower(self):
        """
        ControlPanel: HardwarePower.

        Returns
        -------
        HardwarePower
            Instance of the HardwarePower API, sharing the same state as DSM.
        """
        if self._hard_power is None:
            # Create HardwarePower instance without calling __init__
            self._hard_power = HardwarePower.__new__(HardwarePower)
            # Share the state
            self._hard_power.__dict__ = self.__dict__
        return self._hard_power

    @property
    def IndexingService(self):
        """
        ControlPanel: IndexingService.

        Returns
        -------
        IndexingService
            Instance of the IndexingService API, sharing the same state as DSM.
        """
        if self._idx_service is None:
            # Create IndexingService instance without calling __init__
            self._idx_service = IndexingService.__new__(IndexingService)
            # Share the state
            self._idx_service.__dict__ = self.__dict__
        return self._idx_service

    @property
    def InfoCenter(self):
        """
        ControlPanel: InfoCenter.

        Returns
        -------
        InfoCenter
            Instance of the InfoCenter API, sharing the same state as DSM.
        """
        if self._info_center is None:
            # Create InfoCenter instance without calling __init__
            self._info_center = InfoCenter.__new__(InfoCenter)
            # Share the state
            self._info_center.__dict__ = self.__dict__
        return self._info_center

    @property
    def LoginPortal(self):
        """
        ControlPanel: LoginPortal.

        Returns
        -------
        LoginPortal
            Instance of the LoginPortal API, sharing the same state as DSM.
        """
        if self._log_portal is None:
            # Create LoginPortal instance without calling __init__
            self._log_portal = LoginPortal.__new__(LoginPortal)
            # Share the state
            self._log_portal.__dict__ = self.__dict__
        return self._log_portal

    @property
    def Network(self):
        """
        ControlPanel: Network.

        Returns
        -------
        Network
            Instance of the Network API, sharing the same state as DSM.
        """
        if self._network is None:
            # Create Network instance without calling __init__
            self._network = Network.__new__(Network)
            # Share the state
            self._network.__dict__ = self.__dict__
        return self._network

    @property
    def Notifications(self):
        """
        ControlPanel: Notifications.

        Returns
        -------
        Notifications
            Instance of the Notifications API, sharing the same state as DSM.
        """
        if self._notification is None:
            # Create Notifications instance without calling __init__
            self._notification = Notifications.__new__(Notifications)
            # Share the state
            self._notification.__dict__ = self.__dict__
        return self._notification

    @property
    def RegionalOptions(self):
        """
        ControlPanel: RegionalOptions.

        Returns
        -------
        RegionalOptions
            Instance of the RegionalOptions API, sharing the same state as DSM.
        """
        if self._region_opt is None:
            # Create RegionalOptions instance without calling __init__
            self._region_opt = RegionalOptions.__new__(RegionalOptions)
            # Share the state
            self._region_opt.__dict__ = self.__dict__
        return self._region_opt

    @property
    def Security(self):
        """
        ControlPanel: Security.

        Returns
        -------
        Security
            Instance of the Security API, sharing the same state as DSM.
        """
        if self._security is None:
            # Create Security instance without calling __init__
            self._security = Security.__new__(Security)
            # Share the state
            self._security.__dict__ = self.__dict__
        return self._security

    @property
    def SharedFolder(self):
        """
        ControlPanel: SharedFolder.

        Returns
        -------
        SharedFolder
            Instance of the SharedFolder API, sharing the same state as DSM.
        """
        if self._shared_folder is None:
            # Create SharedFolder instance without calling __init__
            self._shared_folder = SharedFolder.__new__(SharedFolder)
            # Share the state
            self._shared_folder.__dict__ = self.__dict__
        return self._shared_folder

    @property
    def SynologyAccount(self):
        """
        ControlPanel: SynologyAccount.

        Returns
        -------
        SynologyAccount
            Instance of the SynologyAccount API, sharing the same state as DSM.
        """
        if self._syno_account is None:
            # Create ApplicationPrivileges instance without calling __init__
            self._syno_account = SynologyAccount.__new__(SynologyAccount)
            # Share the state
            self._syno_account.__dict__ = self.__dict__
        return self._syno_account

    @property
    def TaskScheduler(self):
        """
        ControlPanel: TaskScheduler.

        Returns
        -------
        TaskScheduler
            Instance of the TaskScheduler API, sharing the same state as DSM.
        """
        if self._task_scheduler is None:
            # Create TaskScheduler instance without calling __init__
            self._task_scheduler = TaskScheduler.__new__(TaskScheduler)
            # Share the state
            self._task_scheduler.__dict__ = self.__dict__
        return self._task_scheduler

    @property
    def TerminalSNMP(self):
        """
        ControlPanel: TerminalSNMP.

        Returns
        -------
        TerminalSNMP
            Instance of the TerminalSNMP API, sharing the same state as DSM.
        """
        if self._terminal_snmp is None:
            # Create TerminalSNMP instance without calling __init__
            self._terminal_snmp = TerminalSNMP.__new__(TerminalSNMP)
            # Share the state
            self._terminal_snmp.__dict__ = self.__dict__
        return self._terminal_snmp

    @property
    def UpdateRestore(self):
        """
        ControlPanel: UpdateRestore.

        Returns
        -------
        UpdateRestore
            Instance of the UpdateRestore API, sharing the same state as DSM.
        """
        if self._update_restore is None:
            # Create UpdateRestore instance without calling __init__
            self._update_restore = UpdateRestore.__new__(UpdateRestore)
            # Share the state
            self._update_restore.__dict__ = self.__dict__
        return self._update_restore

    @property
    def UserGroup(self):
        """
        ControlPanel: UserGroup.

        Returns
        -------
        UserGroup
            Instance of the UserGroup API, sharing the same state as DSM.
        """
        if self._user_group is None:
            # Create UserGroup instance without calling __init__
            self._user_group = UserGroup.__new__(UserGroup)
            # Share the state
            self._user_group.__dict__ = self.__dict__
        return self._user_group
