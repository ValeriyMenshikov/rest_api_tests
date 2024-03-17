from __future__ import annotations

from pydantic import Field, BaseModel, StrictStr, ConfigDict


class BadRequestError(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: StrictStr | None = Field(None, description="Client message")
    invalid_properties: dict[str, list[StrictStr]] | None = Field(
        None,
        alias="invalidProperties",
        description="Key-value pairs of invalid request properties",
    )
