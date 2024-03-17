from __future__ import annotations

from pydantic import Field, BaseModel, StrictStr, ConfigDict


class ResetPassword(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None = Field(None, description="Login")
    email: StrictStr | None = Field(None, description="Email")
