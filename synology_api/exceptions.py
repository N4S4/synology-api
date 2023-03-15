from .error_codes import error_codes, auth_error_codes, download_station_error_codes, file_station_error_codes
from .error_codes import virtualization_error_codes#, surveillance_station_error_codes

# Base exception:
class BaseException(Exception):
    '''Base class for an exception. Defines error_message.'''
    def __init__(self, error_message:str, *args: object) -> None:
        super().__init__(*args)
        self.error_message = error_message
        return
# Classes to reraise Exceptions from requests.
class ConnectionError(BaseException):
    '''Class to raise when a connection error occurs.'''
    def __init__(self, error_message:str, *args: object) -> None:
        super().__init__(error_message=error_message, *args)
        return

class HTTPError(BaseException):
    '''Class to raise when an http error occurs.'''
    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(error_message, *args)
        return

class JSONDecodeError(BaseException):
    '''Class to raise when server fails to send JSON.'''
    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(error_message, *args)
        return

# Classes for when we receieve an error code in the JSON from the server.
class LoginError(BaseException):
    '''Class for an error during login.'''
    def __init__(self, error_code:int, *args: object) -> None:
        self.error_code : int = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message=auth_error_codes[error_code], *args)
        return

class LogoutError(BaseException):
    '''Class for an error during logout.'''
    def __init__(self, error_code:int, *args: object) -> None:
        self.error_code : int = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message=auth_error_codes[error_code], *args)
        return

class DownloadStationError(BaseException):
    '''Class for an error during a download station request.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code : int = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        elif (error_code in download_station_error_codes.keys()):
            super().__init__(error_message=download_station_error_codes[error_code], *args)
        else:
            super().__init__(error_message="DownloadStation Error: %i" % error_code, *args)
        return

class FileStationError(BaseException):
    '''Class for an error during a file station request.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code : int = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        elif (error_code in file_station_error_codes.keys()):
            super().__init__(error_message=file_station_error_codes[error_code], *args)
        else:
            super().__init__(error_message="FileStation Error: %i" % error_code, *args)
        return

class VirtualizationError(BaseException):
    '''Class for an error during a virtualization request.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        elif (error_code in virtualization_error_codes.keys()):
            super().__init__(error_message=virtualization_error_codes[error_code], *args)
        else:
            super().__init__(error_message="Virtualization Error: %i" % error_code, *args)
        return

class AudioStationError(BaseException):
    '''Class for an error during an audio station request. NOTE: I can't find any documentation on the audio station webAPI errors numbers and their respective messages.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="AudioStation Error: %i" % error_code, *args)
        return

class ActiveBackupError(BaseException):
    '''Class for an error duing ActiveBackup request. NOTE: I can't find any documentaion on error codes or thier respective messages.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message='ActiveBackup Error: %i' % error_code, *args)

class BackupError(BaseException):
    '''Class for an error during backup request. NOTE: Again I can't find error code documentation.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Backup Error: %i" % error_code, *args)
        return

class CertificateError(BaseException):
    '''Class for an error during Core.Certificate request. NOTE: Lacking documentation.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code])
        else:
            super().__init__(error_message="Certificate Error: %i" % error_code, *args)
        return

class DHCPServerError(BaseException):
    '''Class for an error during a DHCPServer request.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DHCPServer Error: %i" % error_code, *args)
        return

class DirectoryServerError(BaseException):
    '''Class for an error during a directory server request. NOTE: No docs on errors.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DirectoryServer Error: %i" % error_code, *args)
        return

class DockerError(BaseException):
    '''Class for an error during a docker request. NOTE: No docs on errors.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Docker Error: %i" % error_code, *args)
        return

class DriveAdminError(BaseException):
    '''Class for an error during a drive admin request. NOTE: No error docs.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DriveAdmin Error: %i" % error_code, *args)
        return

class LogCenterError(BaseException):
    '''Class for an error during a LogCenter request. NOTE: No docs on errors.... again.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="LogCenter Error: %i" % error_code, *args)
        return

class NoteStationError(BaseException):
    '''Class for an error during a NoteStation request. NOTE: No error docs.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="NoteStation Error: %i" % error_code, *args)
        return

class OAUTHError(BaseException):
    '''Class for an error during a OAUTH request. NOTE: No error docs.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="OAUTH Error: %i" % error_code, *args)
        return

class PhotosError(BaseException):
    '''Class for an error during a Photos request. NOTE: No error docs.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Photos Error: %i" % error_code, *args)
        return

class SecurityAdvisorError(BaseException):
    '''Class for an error during a SecurityAdvisor request. NOTE: What docs?'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="SecurityAdvisor Error: %i" % error_code, *args)
        return

class UniversalSearchError(BaseException):
    '''Class for an error during UniversalSearch request. NOTE:... no docs on errors....'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="UniversalSearch Error: %i" % error_code, *args)
        return

class USBCopyError(BaseException):
    '''Class for an error during a USBCopy request. NOTE: No docs on errors.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="USBCopy Error: %i" % error_code, *args)

class VirtualizationError(BaseException):
    '''Class for an error during a Virtualization request. NOTE: No docs on errors.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Virtualization Error: %i" % error_code, *args)
        return

class VPNError(BaseException):
    '''Class for an error during a VPN request. NOTE: No docs on errors.'''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="VPN Error: %i" % error_code, *args)
        return

class CoreSysInfoError(BaseException):
    '''Class for an error during a SYNO.Core.*, 'SYNO.Backup.Service.NetworkBackup', SYNO.Storage.*,
            'SYNO.Finder.FileIndexing.Status', 'SYNO.S2S.Server.Pair', SYNO.ResourceMonitor.*
    '''
    def __init__(self, error_code: int, *args: object) -> None:
        self.error_code = error_code
        if (error_code in error_codes.keys()):
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="CoreSysInfo Error: %i" % error_code, *args)
        return

class UndefinedError(BaseException):
    '''Class for undefined errors.'''
    def __init__(self, error_code: int, api_name: str, *args: object) -> None:
        self.error_code = error_code
        self.api_name = api_name
        super().__init__(error_message="Undefined Error: API: %s, Code: %i" % (api_name, error_code), *args)
        return