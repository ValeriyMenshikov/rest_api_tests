from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Extra, Field, StrictStr


class LoginCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    remember_me: Optional[bool] = Field(None, alias='rememberMe')
