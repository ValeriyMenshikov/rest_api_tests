from __future__ import annotations
from typing import Optional, Dict, List
from pydantic import BaseModel, Extra, Field, StrictStr, ConfigDict


class BadRequestError(BaseModel):
    model_config = ConfigDict(extra='forbid')

    message: Optional[StrictStr] = Field(None, description='Client message')
    invalid_properties: Optional[Dict[str, List[StrictStr]]] = Field(
        None,
        alias='invalidProperties',
        description='Key-value pairs of invalid request properties',
    )
