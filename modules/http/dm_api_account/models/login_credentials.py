from __future__ import annotations
from pydantic import BaseModel, StrictStr, Field, ConfigDict


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None
    password: StrictStr | None
    rememberMe: bool | None = Field(None, alias="remember_me")
