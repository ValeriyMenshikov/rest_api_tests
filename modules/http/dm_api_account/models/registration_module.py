from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field


class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    password: Optional[StrictStr] = Field(None, description='Password')
    email: Optional[StrictStr] = Field(None, description='Email')
