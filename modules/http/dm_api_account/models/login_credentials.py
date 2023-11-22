from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field, ConfigDict


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr]
    password: Optional[StrictStr]
    rememberMe: Optional[bool] = Field(None, alias='remember_me')

