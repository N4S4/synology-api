
from json import loads, dumps
from pathlib import Path
from sys import exit as sysexit
from typing import Dict, Any

from appdirs import user_config_dir
from dataclasses import dataclass, field
from rich.console import Console

from .ui import dataclass_table
from .webservice import WebService

CONFIG_FILE = 'config.json'
PROFILES_FILE = 'profiles.json'
SESSIONS_FILE = 'sessions.json'

@dataclass
class Profile:

    url: str = field( default=None )
    account: str = field( default=None )
    password: str = field( default=None )

@dataclass
class ApplicationConfiguration:

    profile: Dict = field( default=None ) # active profile
    session: Dict = field( default=None ) # active session

    config: Dict[str, str] = field( default_factory=dict )
    profiles: Dict[str, Dict] = field( default_factory=dict )
    sessions: Dict[str, Dict] = field( default_factory=dict )

    def save_sessions( self ) -> None:
        with Path(ucd, SESSIONS_FILE) as f:
            f.write_text( dumps( self.sessions, indent=2 ), encoding='UTF-8' )

@dataclass
class ApplicationContext:

    cfg: ApplicationConfiguration = field( default=None )
    service: WebService = field( default=None )

    console: Console = field( default=Console() )

    def print( self, obj: Any ) -> None:
        if isinstance( obj, list ):
            self.console.print( dataclass_table( obj ) )
        else:
            self.console.print( obj )

# init

ctx: ApplicationContext = ApplicationContext()

with Path( user_config_dir( 'synocli', roaming=True ) ) as ucd:
    ctx.cfg = ApplicationConfiguration()

    try:
        with Path( ucd, CONFIG_FILE ) as f:
            ctx.cfg.config = loads( f.read_text( encoding='UTF-8' ) )
    except FileNotFoundError:
        print( f'Error reading configuration file {f}, exiting ...' )
        sysexit( -1 )

    try:
        with Path(ucd, PROFILES_FILE) as f:
            ctx.cfg.profiles = loads( f.read_text(encoding='UTF-8') )
            ctx.cfg.profile = ctx.cfg.profiles.get( ctx.cfg.config.get( 'profile' ) )
    except FileNotFoundError:
        print( f'Error reading profiles file {f}, exiting ...' )
        sysexit( -1 )

    try:
        with Path(ucd, SESSIONS_FILE) as f:
            ctx.cfg.sessions = loads(f.read_text(encoding='UTF-8'))
            ctx.cfg.session = ctx.cfg.sessions.get( ctx.cfg.config.get( 'profile' ) )
    except FileNotFoundError:
        pass
