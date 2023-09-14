from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field


class ChangePassword(BaseModel):
    class Config:
        extra = 'forbid'

    login: Optional[StrictStr] = Field(None, description='User login')
    token: Optional[StrictStr] = Field(None, description='Password reset token')
    oldPassword: Optional[StrictStr] = Field(
        None, alias='old_password', description='Old password'
    )
    newPassword: Optional[StrictStr] = Field(
        None, alias='new_password', description='New password'
    )
