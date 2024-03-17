from __future__ import annotations

from pydantic import Field, BaseModel, StrictStr, ConfigDict


class ChangePassword(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None = Field(None, description="User login")
    token: StrictStr | None = Field(None, description="Password reset token")
    oldPassword: StrictStr | None = Field(
        None,
        alias="old_password",
        description="Old password",
    )
    newPassword: StrictStr | None = Field(
        None,
        alias="new_password",
        description="New password",
    )
