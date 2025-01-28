from .error_codes import error_codes, auth_error_codes, download_station_error_codes, file_station_error_codes, core_error_codes
from .error_codes import virtualization_error_codes


# Base exception:
class SynoBaseException(Exception):
    """Base class for an exception. Defines error_message."""

    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(*args)
        self.error_message = error_message
        return


# Classes to reraise Exceptions from requests.
class SynoConnectionError(SynoBaseException):
    """Class to raise when a connection error occurs."""

    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(error_message=error_message, *args)
        return


class HTTPError(SynoBaseException):
    """Class to raise when a http error occurs."""

    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(error_message, *args)
        return


class JSONDecodeError(SynoBaseException):
    """Class to raise when server fails to send JSON."""

    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(error_message, *args)
        return


# Classes for when we receive an error code in the JSON from the server.
class LoginError(SynoBaseException):
    """Class for an error during login."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code: int = error_code
        if error_code not in error_codes.keys():
            super().__init__(error_message=auth_error_codes[error_code], *args)
        else:
            super().__init__(error_message=error_codes[error_code], *args)
        return


class LogoutError(SynoBaseException):
    """Class for an error during logout."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code: int = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message=auth_error_codes[error_code], *args)
        return


class DownloadStationError(SynoBaseException):
    """Class for an error during a download station request."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code: int = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        elif error_code in download_station_error_codes.keys():
            super().__init__(error_message=download_station_error_codes[error_code], *args)
        else:
            super().__init__(error_message="DownloadStation Error: %i" % error_code, *args)
        return


class FileStationError(SynoBaseException):
    """Class for an error during a file station request."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code: int = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        elif error_code in file_station_error_codes.keys():
            super().__init__(error_message=file_station_error_codes[error_code], *args)
        else:
            super().__init__(error_message="FileStation Error: %i" % error_code, *args)
        return


class VirtualizationError(SynoBaseException):
    """Class for an error during a virtualization request."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        elif error_code in virtualization_error_codes.keys():
            super().__init__(error_message=virtualization_error_codes[error_code], *args)
        else:
            super().__init__(error_message="Virtualization Error: %i" % error_code, *args)
        return


class AudioStationError(SynoBaseException):
    """Class for an error during an audio station request. NOTE: I can't find any documentation on the audio station
    webAPI errors numbers and their respective messages."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="AudioStation Error: %i" % error_code, *args)
        return


class ActiveBackupError(SynoBaseException):
    """Class for an error during ActiveBackup request. NOTE: I can't find any documentation on error codes or their
    respective messages."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message='ActiveBackup Error: %i' % error_code, *args)

class ActiveBackupMicrosoftError(SynoBaseException):
    """Class for an error during ActiveBackupMicrosoft request. NOTE: I can't find any documentation on error codes or their
    respective messages."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message='ActiveBackupMicrosoft Error: %i' % error_code, *args)

class BackupError(SynoBaseException):
    """Class for an error during backup request. NOTE: Again I can't find error code documentation."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Backup Error: %i" % error_code, *args)
        return


class CertificateError(SynoBaseException):
    """Class for an error during Core.Certificate request. NOTE: Lacking documentation."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code])
        else:
            super().__init__(error_message="Certificate Error: %i" % error_code, *args)
        return
    
class CloudSyncError(SynoBaseException):
    """Class for an error during SYNO.CloudSync request. NOTE: Lacking documentation."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code])
        else:
            super().__init__(error_message="Cloud Sync Error: %i" % error_code, *args)
        return


class DHCPServerError(SynoBaseException):
    """Class for an error during a DHCPServer request."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DHCPServer Error: %i" % error_code, *args)
        return


class DirectoryServerError(SynoBaseException):
    """Class for an error during a directory server request. NOTE: No docs on errors."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DirectoryServer Error: %i" % error_code, *args)
        return


class DockerError(SynoBaseException):
    """Class for an error during a docker request. NOTE: No docs on errors."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Docker Error: %i" % error_code, *args)
        return


class DriveAdminError(SynoBaseException):
    """Class for an error during a drive admin request. NOTE: No error docs."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DriveAdmin Error: %i" % error_code, *args)
        return


class LogCenterError(SynoBaseException):
    """Class for an error during a LogCenter request. NOTE: No docs on errors.... again."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="LogCenter Error: %i" % error_code, *args)
        return


class NoteStationError(SynoBaseException):
    """Class for an error during a NoteStation request. NOTE: No error docs."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="NoteStation Error: %i" % error_code, *args)
        return


class OAUTHError(SynoBaseException):
    """Class for an error during a OAUTH request. NOTE: No error docs."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="OAUTH Error: %i" % error_code, *args)
        return


class PhotosError(SynoBaseException):
    """Class for an error during a Photos request. NOTE: No error docs."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Photos Error: %i" % error_code, *args)
        return


class SecurityAdvisorError(SynoBaseException):
    """Class for an error during a SecurityAdvisor request. NOTE: What docs?"""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="SecurityAdvisor Error: %i" % error_code, *args)
        return


class TaskSchedulerError(SynoBaseException):
    """Class for an error during TaskScheduler request. NOTE:... no docs on errors...."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="TaskScheduler Error: %i" % error_code, *args)
        return


class EventSchedulerError(SynoBaseException):
    """Class for an error during EventScheduler request. NOTE:... no docs on errors...."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="EventScheduler Error: %i" % error_code, *args)
        return


class UniversalSearchError(SynoBaseException):
    """Class for an error during UniversalSearch request. NOTE:... no docs on errors...."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="UniversalSearch Error: %i" % error_code, *args)
        return


class USBCopyError(SynoBaseException):
    """Class for an error during a USBCopy request. NOTE: No docs on errors."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="USBCopy Error: %i" % error_code, *args)

class VPNError(SynoBaseException):
    """Class for an error during a VPN request. NOTE: No docs on errors."""

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="VPN Error: %i" % error_code, *args)
        return

class CoreError(SynoBaseException):
    """Class for an error during a SYNO.Core.*
    """
    
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in core_error_codes.keys():
            super().__init__(error_message=core_error_codes[error_code], *args)
        else:
            super().__init__(error_message="Core Error: %i" % error_code, *args)
        return

class CoreSysInfoError(SynoBaseException):
    """Class for an error during a 'SYNO.Backup.Service.NetworkBackup', SYNO.Storage.*,
            'SYNO.Finder.FileIndexing.Status', 'SYNO.S2S.Server.Pair', SYNO.ResourceMonitor.*
    """

    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="CoreSysInfo Error: %i" % error_code, *args)
        return


class UndefinedError(SynoBaseException):
    """Class for undefined errors."""

    def __init__(self, error_code: int, api_name: str, *args: object) -> None:
        self.error_code = error_code
        self.api_name = api_name
        super().__init__(error_message="Undefined Error: API: %s, Code: %i" % (api_name, error_code), *args)
        return
