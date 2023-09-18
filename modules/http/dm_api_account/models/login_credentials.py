from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field


class LoginCredentials(BaseModel):
    class Config:
        extra = 'forbid'

    login: Optional[StrictStr]
    password: Optional[StrictStr]
    rememberMe: Optional[bool] = Field(None, alias='remember_me')

