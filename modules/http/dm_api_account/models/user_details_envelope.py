from __future__ import annotations

from enum import Enum
from typing import Any
from datetime import datetime

from pydantic import Field, BaseModel, StrictStr, ConfigDict


class BbParseMode(Enum):
    common = "Common"
    info = "Info"
    post = "Post"
    chat = "Chat"


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


class InfoBbText(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: StrictStr | None = Field(None, description="Text")
    parse_mode: BbParseMode | None = Field(None, alias="parseMode")


class PagingSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    posts_per_page: int | None = Field(
        None,
        alias="postsPerPage",
        description="Number of posts on a game room page",
    )
    comments_per_page: int | None = Field(
        None,
        alias="commentsPerPage",
        description="Number of commentaries on a game or a topic page",
    )
    topics_per_page: int | None = Field(
        None,
        alias="topicsPerPage",
        description="Number of detached topics on a forum page",
    )
    messages_per_page: int | None = Field(
        None,
        alias="messagesPerPage",
        description="Number of private messages and conversations on dialogue page",
    )
    entities_per_page: int | None = Field(
        None,
        alias="entitiesPerPage",
        description="Number of other entities on page",
    )


class ColorSchema(Enum):
    modern = "Modern"
    pale = "Pale"
    classic = "Classic"
    classic_pale = "ClassicPale"
    night = "Night"


class UserSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    color_schema: ColorSchema | None = Field(None, alias="colorSchema")
    nanny_greetings_message: StrictStr | None = Field(
        None,
        alias="nannyGreetingsMessage",
        description="Message that user's newbies will receive once they are connected",
    )
    paging: PagingSettings | None = None


class UserDetails(BaseModel):
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
    icq: StrictStr | None = Field(None, description="User ICQ number")
    skype: StrictStr | None = Field(None, description="User Skype login")
    original_picture_url: StrictStr | None = Field(
        None,
        alias="originalPictureUrl",
        description="URL of profile picture original",
    )
    info: Any | None
    settings: UserSettings | None = None


class UserDetailsEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")

    resource: UserDetails | None = None
    metadata: Any | None = Field("None", description="Additional metadata")
