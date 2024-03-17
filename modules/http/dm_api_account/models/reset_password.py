from __future__ import annotations
from pydantic import BaseModel, StrictStr, Field, ConfigDict


class ResetPassword(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None = Field(None, description="Login")
    email: StrictStr | None = Field(None, description="Email")
