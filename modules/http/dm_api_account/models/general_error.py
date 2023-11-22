from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field, ConfigDict


class GeneralError(BaseModel):
    model_config = ConfigDict(extra='forbid')

    message: Optional[StrictStr] = Field(None, description='Client message')
