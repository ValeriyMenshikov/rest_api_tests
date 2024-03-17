from __future__ import annotations

from enum import Enum
from typing import Any
from datetime import datetime

from pydantic import Field, BaseModel, StrictStr, ConfigDict


class UserRole(Enum):
    guest = "Guest"
    player = "Player"
    administrator = "Administrator"
    nanny_moderator = "NannyModerator"
    regular_moderator = "RegularModerator"
    senior_moderator = "SeniorModerator"


class Rating(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool | None = Field(None, description="Rating participation flag")
    quality: int | None = Field(None, description="Quality rating")
    quantity: int | None = Field(None, description="Quantity rating")


class User(BaseModel):
    model_config = ConfigDict(extra="forbid")

    login: StrictStr | None = Field(None, description="Login")
    roles: list[UserRole] | None = Field(None, description="Roles")
    medium_picture_url: StrictStr | None = Field(
        None,
        alias="mediumPictureUrl",
        description="Profile picture URL M-size",
    )
    small_picture_url: StrictStr | None = Field(
        None,
        alias="smallPictureUrl",
        description="Profile picture URL S-size",
    )
    status: StrictStr | None = Field(None, description="User defined status")
    rating: Rating | None = None
    online: datetime | None = Field(None, description="Last seen online moment")
    name: StrictStr | None = Field(None, description="User real name")
    location: StrictStr | None = Field(None, description="User real location")
    registration: datetime | None = Field(None, description="User registration moment")


class UserEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")

    resource: User | None = None
    metadata: Any | None = Field(None, description="Additional metadata")
