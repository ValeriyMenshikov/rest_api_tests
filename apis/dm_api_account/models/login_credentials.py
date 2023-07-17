from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field


class LoginCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr]
    password: Optional[StrictStr]
    remember_me: Optional[bool] = Field(None, alias='rememberMe')
