from __future__ import annotations

from pydantic import Field, BaseModel, StrictStr, ConfigDict


class ChangeEmail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None = Field(None, description="User login")
    password: StrictStr | None = Field(None, description="User password")
    email: StrictStr | None = Field(None, description="New user email")
