
![synology-api](https://user-images.githubusercontent.com/33936751/100731387-99fffc00-33cb-11eb-833c-b6ab87177651.jpg)
<a href="https://pepy.tech/projects/synology-api" rel="noreferrer" target="_blank"><img alt="Pepy Total Downloads" src="https://img.shields.io/pepy/dt/synology-api?color=blue"></a>
<a href="https://n4s4.github.io/synology-api" rel="noreferrer" target="_blank"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fn4s4.github.io%2Fsynology-api&label=docs&color=green"></a>

<a href="https://github.com/N4S4/synology-api/commits/master/" rel="noreferrer" target="_blank"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/n4s4/synology-api"></a>
<a href="https://github.com/N4S4/synology-api/blob/master/LICENSE.txt" rel="noreferrer" target="_blank"><img alt="GitHub License" src="https://img.shields.io/github/license/n4s4/synology-api"></a>


# Synology Wrapper

If you find yourself here, most probably you are trying to develop something for your NAS, this wrapper might come to your help to build your script.

I would like to specify that I do this for hobby as is my passion and in my little free time.

Said this, there is no warranties chained and this library is provided "As Is", you will find many things can be simplified, and I slowly will but feel free to [Contribute](https://n4s4.github.io/synology-api/docs/contribute).
 
## Premise

I've tried this wrapper only with `python3`.  
I do not know if it actually runs with previous versions 

Before opening an issue make sure you do your own research, if you are not sure, write me.

## Installation

The package is distributed via pip3, but it can also be installed from source.

```bash
pip3 install synology-api
```

or

```bash
pip3 install git+https://github.com/N4S4/synology-api
```


## Basic Usage
Here is a basic example on how to use the package, check [Getting Started - Basic Usage](https://n4s4.github.io/synology-api/docs/getting-started/usage) for more details.

```python
from synology_api.filestation import FileStation
from synology_api.downloadstation import DownloadStation

fs = FileStation(
    'Synology Ip',
    'Synology Port',
    'Username',
    'Password',
    secure=False,
    cert_verify=False,
    dsm_version=7,
    debug=True,
    otp_code=None
)

ds = DownloadStation(
    'Synology Ip',
    'Synology Port',
    'Username',
    'Password',
    secure=False,
    cert_verify=False,
    dsm_version=7,
    debug=True,
    otp_code=None
)

fs_info = fs.get_info()
ds_info = ds.get_info()

```

## Available Functions

At the moment there are around +300 APIs implemented with countless methods for each, the majority is not documented, but some are.  

You can find a exhaustive list here:  
[APIs - Supported APIs](https://n4s4.github.io/synology-api/docs/apis) 

## Feeling kind?
If this code helps and you wish to support me:
- [Paypal](https://paypal.me/ren4s4)
- [GitHub Sponsor](https://github.com/sponsors/N4S4)

## Community
- [Telegram Group](https://t.me/SynologyApi)
- [Github Discussions](https://github.com/N4S4/synology-api/discussions)

## See Related projects

- [Synology API Telegram Bot](https://github.com/N4S4/synology-api-telegram-bot)

If you want to show your project in this section, write me.

## Bugs

Maybe? 

I hate bugs..

Well report them please (if you'll ever use this code)

## Conclusions

There is still a lot to implement.

The code is probably in some parts twisted, I will try to optimize it at best.

## Contributing

Just Don't Be Scared.  
Check [Contribute - Contribution 101](https://n4s4.github.io/synology-api/docs/contribute) for useful information.

## Author

- Renato Visaggio - _Initial_ _Work_ - [N4S4](https://github.com/N4S4)

## Contributors

- List of contributors here: [Contributors](https://github.com/N4S4/synology-api/graphs/contributors)

