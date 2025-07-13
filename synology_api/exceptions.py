"""
Exception classes for Synology API.

This module defines custom exception classes for handling errors and error codes
returned by various Synology API endpoints.
"""

from .error_codes import error_codes, auth_error_codes, download_station_error_codes, file_station_error_codes, core_error_codes
from .error_codes import virtualization_error_codes


# Base exception:
class SynoBaseException(Exception):
    """
    Base class for an exception.

    Defines error_message.

    Parameters
    ----------
    error_message : str
        The error message describing the exception.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_message: str, *args: object) -> None:
        """
        Initialize SynoBaseException.

        Parameters
        ----------
        error_message : str
            The error message describing the exception.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        super().__init__(*args)
        self.error_message = error_message
        return


# Classes to reraise Exceptions from requests.
class SynoConnectionError(SynoBaseException):
    """
    Exception raised when a connection error occurs.

    Parameters
    ----------
    error_message : str
        The error message describing the connection error.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_message: str, *args: object) -> None:
        """
        Initialize SynoConnectionError.

        Parameters
        ----------
        error_message : str
            The error message describing the connection error.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        super().__init__(error_message=error_message, *args)
        return


class HTTPError(SynoBaseException):
    """
    Exception raised when an HTTP error occurs.

    Parameters
    ----------
    error_message : str
        The error message describing the HTTP error.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_message: str, *args: object) -> None:
        """
        Initialize HTTPError.

        Parameters
        ----------
        error_message : str
            The error message describing the HTTP error.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        super().__init__(error_message, *args)
        return


class JSONDecodeError(SynoBaseException):
    """
    Exception raised when the server fails to send valid JSON.

    Parameters
    ----------
    error_message : str
        The error message describing the JSON decode error.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_message: str, *args: object) -> None:
        """
        Initialize JSONDecodeError.

        Parameters
        ----------
        error_message : str
            The error message describing the JSON decode error.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        super().__init__(error_message, *args)
        return


# Classes for when we receive an error code in the JSON from the server.
class LoginError(SynoBaseException):
    """
    Exception raised for an error during login.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize LoginError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code: int = error_code
        if error_code not in error_codes.keys():
            super().__init__(error_message=auth_error_codes[error_code], *args)
        else:
            super().__init__(error_message=error_codes[error_code], *args)
        return


class LogoutError(SynoBaseException):
    """
    Exception raised for an error during logout.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize LogoutError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code: int = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message=auth_error_codes[error_code], *args)
        return


class DownloadStationError(SynoBaseException):
    """
    Exception raised for an error during a Download Station request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize DownloadStationError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code: int = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        elif error_code in download_station_error_codes.keys():
            super().__init__(
                error_message=download_station_error_codes[error_code], *args)
        else:
            super().__init__(error_message="DownloadStation Error: %i" % error_code, *args)
        return


class FileStationError(SynoBaseException):
    """
    Exception raised for an error during a File Station request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize FileStationError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code: int = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        elif error_code in file_station_error_codes.keys():
            super().__init__(
                error_message=file_station_error_codes[error_code], *args)
        else:
            super().__init__(error_message="FileStation Error: %i" % error_code, *args)
        return


class VirtualizationError(SynoBaseException):
    """
    Exception raised for an error during a virtualization request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize VirtualizationError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        elif error_code in virtualization_error_codes.keys():
            super().__init__(
                error_message=virtualization_error_codes[error_code], *args)
        else:
            super().__init__(error_message="Virtualization Error: %i" % error_code, *args)
        return


class AudioStationError(SynoBaseException):
    """
    Exception raised for an error during an Audio Station request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize AudioStationError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="AudioStation Error: %i" % error_code, *args)
        return


class ActiveBackupError(SynoBaseException):
    """
    Exception raised for an error during an Active Backup request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize ActiveBackupError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message='ActiveBackup Error: %i' % error_code, *args)


class ActiveBackupMicrosoftError(SynoBaseException):
    """
    Exception raised for an error during an Active Backup Microsoft request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize ActiveBackupMicrosoftError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message='ActiveBackupMicrosoft Error: %i' % error_code, *args)


class BackupError(SynoBaseException):
    """
    Exception raised for an error during a backup request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize BackupError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Backup Error: %i" % error_code, *args)
        return


class CertificateError(SynoBaseException):
    """
    Exception raised for an error during a Core.Certificate request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize CertificateError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code])
        else:
            super().__init__(error_message="Certificate Error: %i" % error_code, *args)
        return


class CloudSyncError(SynoBaseException):
    """
    Exception raised for an error during a SYNO.CloudSync request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize CloudSyncError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code])
        else:
            super().__init__(error_message="Cloud Sync Error: %i" % error_code, *args)
        return


class DHCPServerError(SynoBaseException):
    """
    Exception raised for an error during a DHCPServer request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize DHCPServerError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DHCPServer Error: %i" % error_code, *args)
        return


class DirectoryServerError(SynoBaseException):
    """
    Exception raised for an error during a Directory Server request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize DirectoryServerError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DirectoryServer Error: %i" % error_code, *args)
        return


class DockerError(SynoBaseException):
    """
    Exception raised for an error during a Docker request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize DockerError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Docker Error: %i" % error_code, *args)
        return


class DriveAdminError(SynoBaseException):
    """
    Exception raised for an error during a Drive Admin request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize DriveAdminError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="DriveAdmin Error: %i" % error_code, *args)
        return


class LogCenterError(SynoBaseException):
    """
    Exception raised for an error during a LogCenter request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize LogCenterError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="LogCenter Error: %i" % error_code, *args)
        return


class NoteStationError(SynoBaseException):
    """
    Exception raised for an error during a NoteStation request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize NoteStationError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="NoteStation Error: %i" % error_code, *args)
        return


class OAUTHError(SynoBaseException):
    """
    Exception raised for an error during an OAUTH request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize OAUTHError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="OAUTH Error: %i" % error_code, *args)
        return


class PhotosError(SynoBaseException):
    """
    Exception raised for an error during a Photos request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize PhotosError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="Photos Error: %i" % error_code, *args)
        return


class SecurityAdvisorError(SynoBaseException):
    """
    Exception raised for an error during a SecurityAdvisor request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize SecurityAdvisorError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="SecurityAdvisor Error: %i" % error_code, *args)
        return


class TaskSchedulerError(SynoBaseException):
    """
    Exception raised for an error during a TaskScheduler request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize TaskSchedulerError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="TaskScheduler Error: %i" % error_code, *args)
        return


class EventSchedulerError(SynoBaseException):
    """
    Exception raised for an error during an EventScheduler request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize EventSchedulerError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="EventScheduler Error: %i" % error_code, *args)
        return


class UniversalSearchError(SynoBaseException):
    """
    Exception raised for an error during a UniversalSearch request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize UniversalSearchError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="UniversalSearch Error: %i" % error_code, *args)
        return


class USBCopyError(SynoBaseException):
    """
    Exception raised for an error during a USBCopy request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize USBCopyError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="USBCopy Error: %i" % error_code, *args)


class VPNError(SynoBaseException):
    """
    Exception raised for an error during a VPN request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize VPNError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="VPN Error: %i" % error_code, *args)
        return


class CoreError(SynoBaseException):
    """
    Exception raised for an error during a SYNO.Core.* request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize CoreError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in core_error_codes.keys():
            super().__init__(error_message=core_error_codes[error_code], *args)
        else:
            super().__init__(error_message="Core Error: %i" % error_code, *args)
        return


class CoreSysInfoError(SynoBaseException):
    """
    Exception raised for an error during a CoreSysInfoError request.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, *args: object) -> None:
        """
        Initialize CoreSysInfoError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        if error_code in error_codes.keys():
            super().__init__(error_message=error_codes[error_code], *args)
        else:
            super().__init__(error_message="CoreSysInfo Error: %i" % error_code, *args)
        return


class UndefinedError(SynoBaseException):
    """
    Exception raised for undefined errors.

    Parameters
    ----------
    error_code : int
        The error code returned by the API.
    api_name : str
        The name of the API where the error occurred.
    *args : object
        Additional arguments to pass to the base Exception.
    """

    def __init__(self, error_code: int, api_name: str, *args: object) -> None:
        """
        Initialize UndefinedError.

        Parameters
        ----------
        error_code : int
            The error code returned by the API.
        api_name : str
            The name of the API where the error occurred.
        *args : object
            Additional arguments to pass to the base Exception.
        """
        self.error_code = error_code
        self.api_name = api_name
        super().__init__(error_message="Undefined Error: API: %s, Code: %i" %
                         (api_name, error_code), *args)
        return
