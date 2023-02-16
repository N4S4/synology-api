
ENTRY_URL = '{url}/webapi/entry.cgi'

# potential additional fields (taken from web session) are:
# "enable_syno_token": "yes"
# "logintype": "local"
# "enable_device_token": "no"
# "rememberme": "0"

LOGIN_PARAMS = {
    'api': 'SYNO.API.Auth',
    'version': 7,
    'method': 'login',
    'account': None, # needs to be filled
    'passwd': None, # needs to be filled
    'otp_code': '', # empty string when not using 2FA
}
