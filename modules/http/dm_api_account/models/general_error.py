from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, StrictStr, Extra, Field


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
