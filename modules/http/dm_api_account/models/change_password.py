from __future__ import annotations
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, StrictStr, Extra, Field


class ChangePassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    token: Optional[StrictStr] = Field(None, description='Password reset token')
    old_password: Optional[StrictStr] = Field(
        None, alias='oldPassword', description='Old password'
    )
    new_password: Optional[StrictStr] = Field(
        None, alias='newPassword', description='New password'
    )
