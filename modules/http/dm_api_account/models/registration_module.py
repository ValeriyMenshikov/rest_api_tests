from __future__ import annotations
from pydantic import BaseModel, StrictStr, Field, ConfigDict


class Registration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None = Field(None, description="Login")
    password: StrictStr | None = Field(None, description="Password")
    email: StrictStr | None = Field(None, description="Email")
