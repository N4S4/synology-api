import json
from typing import List
import copy
from . import base_api
from .core_share_keymanager_store import KeyManagerStore
from .core_share_keymanager_autokey import KeyManagerAutoKey

class KeyManager(base_api.BaseApi):
    """
    Core Share KeyManager API implementation.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._store: KeyManagerStore = None
        self._autokey: KeyManagerAutoKey = None
        
    @property
    def store(self) -> KeyManagerStore:
        if self._store is None:
            self._store = KeyManagerStore.__new__(KeyManagerStore)
            self._store.__dict__ = self.__dict__
        return self._store
    
    @property
    def autokey(self) -> KeyManagerAutoKey:
        if self._autokey is None:
            self._autokey = KeyManagerAutoKey.__new__(KeyManagerAutoKey)
            self._autokey.__dict__ = self.__dict__
        return self._autokey