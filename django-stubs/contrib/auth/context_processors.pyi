from typing import Any, Dict, Optional, Union

from django.contrib.auth.models import AnonymousUser, User
from django.http.request import HttpRequest
from django.utils.functional import SimpleLazyObject

class PermLookupDict:
    app_label: django.utils.safestring.SafeText
    user: SimpleLazyObject
    def __init__(self, user: SimpleLazyObject, app_label: str) -> None: ...
    def __getitem__(self, perm_name: str) -> bool: ...
    def __iter__(self) -> Any: ...
    def __bool__(self) -> bool: ...

class PermWrapper:
    user: SimpleLazyObject = ...
    def __init__(self, user: Union[AnonymousUser, User]) -> None: ...
    def __getitem__(self, app_label: str) -> PermLookupDict: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, perm_name: Union[bool, str]) -> bool: ...

def auth(request: HttpRequest) -> Dict[str, Union[PermWrapper, AnonymousUser, User]]: ...
