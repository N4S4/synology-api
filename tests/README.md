
# Testing

In order to be able to run a test against a local Synology device, create a file
_credentials.yaml_ in this folder with the following content:

```json
{
  "device": "<your_device_name>",
  "<your_device_name>": {
    "ip_address": "<your_ip_address>",
    "port": <your_port>,
    "username": "<your_user>",
    "password": "<your_password>",
    "secure": true,
    "cert_verify": false,
    "dsm_version": 7,
    "otp_code": null
  }
}
```

The file is read by _fixtures.py_ and can be fed to the constructor of a Synology
Service. Switch to a different device by setting the name in the _device_ key.
