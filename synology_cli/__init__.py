
from json import loads
from pathlib import Path
from typing import Dict

from appdirs import user_config_dir
from dataclasses import dataclass, field
from dataclass_factory import Factory

from .webservice import WebService

@dataclass
class Profile:

    url: str = field( default=None )
    account: str = field( default=None )
    password: str = field( default=None )

@dataclass
class ApplicationConfiguration:

    profile: str = field( default=None )
    profiles: Dict[str, Profile] = field( default_factory=dict )

    def active_profile( self ) -> Profile:
        return self.profiles.get( self.profile )

@dataclass
class ApplicationContext:

    cfg: ApplicationConfiguration = field( default=None )
    service: WebService = field( default=None )

# init

ctx: ApplicationContext = ApplicationContext()

with Path( user_config_dir( 'synocli', roaming=True ), 'config.json' ) as p:
    ctx.cfg = Factory().load( loads( p.read_text( encoding='UTF-8' ) ), ApplicationConfiguration )
