from __future__ import annotations
from pydantic import BaseModel, StrictStr, Field, ConfigDict


class GeneralError(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: StrictStr | None = Field(None, description="Client message")
