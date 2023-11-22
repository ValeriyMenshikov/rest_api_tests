from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field, ConfigDict


class Registration(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = Field(None, description='Login')
    password: Optional[StrictStr] = Field(None, description='Password')
    email: Optional[StrictStr] = Field(None, description='Email')
