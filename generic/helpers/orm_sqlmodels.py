# noqa sqlacodegen==3.0.0rc2 + sqlmodels

from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, SmallInteger, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel

class Conversations(SQLModel, table=True):
    __tablename__ = 'Conversations'
    __table_args__ = (
        ForeignKeyConstraint(['LastMessageId'], ['Messages.MessageId'], ondelete='RESTRICT', name='FK_Conversations_Messages_LastMessageId'),
        PrimaryKeyConstraint('ConversationId', name='PK_Conversations'),
        Index('IX_Conversations_LastMessageId', 'LastMessageId')
    )

    ConversationId: str = Field(sa_column=Column('ConversationId', UUID))
    Visavi: bool = Field(sa_column=Column('Visavi', Boolean, nullable=False, server_default=text('false')))
    LastMessageId: Optional[str] = Field(default=None, sa_column=Column('LastMessageId', UUID))

    Messages: Optional['Messages'] = Relationship(back_populates='Conversations_')
    Messages_: List['Messages'] = Relationship(back_populates='Conversations1')
    UserConversationLinks: List['UserConversationLinks'] = Relationship(back_populates='Conversations_')


class Fora(SQLModel, table=True):
    __tablename__ = 'Fora'
    __table_args__ = (
        PrimaryKeyConstraint('ForumId', name='PK_Fora'),
    )

    ForumId: str = Field(sa_column=Column('ForumId', UUID))
    Order: int = Field(sa_column=Column('Order', Integer, nullable=False))
    ViewPolicy: int = Field(sa_column=Column('ViewPolicy', Integer, nullable=False))
    CreateTopicPolicy: int = Field(sa_column=Column('CreateTopicPolicy', Integer, nullable=False))
    Title: Optional[str] = Field(default=None, sa_column=Column('Title', Text))
    Description: Optional[str] = Field(default=None, sa_column=Column('Description', Text))

    ForumModerators: List['ForumModerators'] = Relationship(back_populates='Fora_')
    ForumTopics: List['ForumTopics'] = Relationship(back_populates='Fora_')


class Messages(SQLModel, table=True):
    __tablename__ = 'Messages'
    __table_args__ = (
        ForeignKeyConstraint(['ConversationId'], ['Conversations.ConversationId'], ondelete='CASCADE', name='FK_Messages_Conversations_ConversationId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Messages_Users_UserId'),
        PrimaryKeyConstraint('MessageId', name='PK_Messages'),
        Index('IX_Messages_ConversationId', 'ConversationId'),
        Index('IX_Messages_UserId', 'UserId')
    )

    MessageId: str = Field(sa_column=Column('MessageId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    ConversationId: str = Field(sa_column=Column('ConversationId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))

    Conversations_: List['Conversations'] = Relationship(back_populates='Messages')
    Conversations1: Optional['Conversations'] = Relationship(back_populates='Messages_')
    Users: Optional['Users'] = Relationship(back_populates='Messages_')


class TagGroups(SQLModel, table=True):
    __tablename__ = 'TagGroups'
    __table_args__ = (
        PrimaryKeyConstraint('TagGroupId', name='PK_TagGroups'),
    )

    TagGroupId: str = Field(sa_column=Column('TagGroupId', UUID))
    Title: Optional[str] = Field(default=None, sa_column=Column('Title', Text))

    Tags: List['Tags'] = Relationship(back_populates='TagGroups_')


class Users(SQLModel, table=True):
    __tablename__ = 'Users'
    __table_args__ = (
        PrimaryKeyConstraint('UserId'),
    )

    UserId: str = Field(sa_column=Column('UserId', UUID), primary_key=True)
    RegistrationDate: datetime = Field(sa_column=Column('RegistrationDate', DateTime(True), nullable=False))
    Role: int = Field(sa_column=Column('Role', Integer, nullable=False))
    AccessPolicy: int = Field(sa_column=Column('AccessPolicy', Integer, nullable=False))
    RatingDisabled: bool = Field(sa_column=Column('RatingDisabled', Boolean, nullable=False))
    QualityRating: int = Field(sa_column=Column('QualityRating', Integer, nullable=False))
    QuantityRating: int = Field(sa_column=Column('QuantityRating', Integer, nullable=False))
    Activated: bool = Field(sa_column=Column('Activated', Boolean, nullable=False))
    CanMerge: bool = Field(sa_column=Column('CanMerge', Boolean, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Login: Optional[str] = Field(default=None, sa_column=Column('Login', String(100)))
    Email: Optional[str] = Field(default=None, sa_column=Column('Email', String(100)))
    LastVisitDate: Optional[datetime] = Field(default=None, sa_column=Column('LastVisitDate', DateTime(True)))
    TimezoneId: Optional[str] = Field(default=None, sa_column=Column('TimezoneId', Text))
    Salt: Optional[str] = Field(default=None, sa_column=Column('Salt', String(120)))
    PasswordHash: Optional[str] = Field(default=None, sa_column=Column('PasswordHash', String(300)))
    MergeRequested: Optional[str] = Field(default=None, sa_column=Column('MergeRequested', UUID))
    Status: Optional[str] = Field(default=None, sa_column=Column('Status', String(200)))
    Name: Optional[str] = Field(default=None, sa_column=Column('Name', String(100)))
    Location: Optional[str] = Field(default=None, sa_column=Column('Location', String(100)))
    Icq: Optional[str] = Field(default=None, sa_column=Column('Icq', String(20)))
    Skype: Optional[str] = Field(default=None, sa_column=Column('Skype', String(50)))
    Info: Optional[str] = Field(default=None, sa_column=Column('Info', Text))
    ProfilePictureUrl: Optional[str] = Field(default=None, sa_column=Column('ProfilePictureUrl', String(200)))
    MediumProfilePictureUrl: Optional[str] = Field(default=None, sa_column=Column('MediumProfilePictureUrl', String(200)))
    SmallProfilePictureUrl: Optional[str] = Field(default=None, sa_column=Column('SmallProfilePictureUrl', String(200)))



class EFMigrationsHistory(SQLModel, table=True):
    __tablename__ = '__EFMigrationsHistory'
    __table_args__ = (
        PrimaryKeyConstraint('MigrationId'),
    )

    MigrationId: str = Field(sa_column=Column('MigrationId', String(150)))
    ProductVersion: str = Field(sa_column=Column('ProductVersion', String(32), nullable=False))


class Bans(SQLModel, table=True):
    __tablename__ = 'Bans'
    __table_args__ = (
        ForeignKeyConstraint(['ModeratorId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Bans_Users_ModeratorId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Bans_Users_UserId'),
        PrimaryKeyConstraint('BanId', name='PK_Bans'),
        Index('IX_Bans_ModeratorId', 'ModeratorId'),
        Index('IX_Bans_UserId', 'UserId')
    )

    BanId: str = Field(sa_column=Column('BanId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    ModeratorId: str = Field(sa_column=Column('ModeratorId', UUID, nullable=False))
    StartDate: datetime = Field(sa_column=Column('StartDate', DateTime(True), nullable=False))
    EndDate: datetime = Field(sa_column=Column('EndDate', DateTime(True), nullable=False))
    AccessRestrictionPolicy: int = Field(sa_column=Column('AccessRestrictionPolicy', Integer, nullable=False))
    IsVoluntary: bool = Field(sa_column=Column('IsVoluntary', Boolean, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Comment: Optional[str] = Field(default=None, sa_column=Column('Comment', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Bans')
    Users1: Optional['Users'] = Relationship(back_populates='Bans_')


class ChatMessages(SQLModel, table=True):
    __tablename__ = 'ChatMessages'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ChatMessages_Users_UserId'),
        PrimaryKeyConstraint('ChatMessageId', name='PK_ChatMessages'),
        Index('IX_ChatMessages_UserId', 'UserId')
    )

    ChatMessageId: str = Field(sa_column=Column('ChatMessageId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))

    Users_: Optional['Users'] = Relationship(back_populates='ChatMessages')


class Comments(SQLModel, table=True):
    __tablename__ = 'Comments'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Comments_Users_UserId'),
        PrimaryKeyConstraint('CommentId', name='PK_Comments'),
        Index('IX_Comments_EntityId', 'EntityId'),
        Index('IX_Comments_UserId', 'UserId')
    )

    CommentId: str = Field(sa_column=Column('CommentId', UUID))
    EntityId: str = Field(sa_column=Column('EntityId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    LastUpdateDate: Optional[datetime] = Field(default=None, sa_column=Column('LastUpdateDate', DateTime(True)))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Comments')
    ForumTopics: List['ForumTopics'] = Relationship(back_populates='Comments_')


class ForumModerators(SQLModel, table=True):
    __tablename__ = 'ForumModerators'
    __table_args__ = (
        ForeignKeyConstraint(['ForumId'], ['Fora.ForumId'], ondelete='CASCADE', name='FK_ForumModerators_Fora_ForumId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ForumModerators_Users_UserId'),
        PrimaryKeyConstraint('ForumModeratorId', name='PK_ForumModerators'),
        Index('IX_ForumModerators_ForumId', 'ForumId'),
        Index('IX_ForumModerators_UserId', 'UserId')
    )

    ForumModeratorId: str = Field(sa_column=Column('ForumModeratorId', UUID))
    ForumId: str = Field(sa_column=Column('ForumId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))

    Fora_: Optional['Fora'] = Relationship(back_populates='ForumModerators')
    Users_: Optional['Users'] = Relationship(back_populates='ForumModerators')


class Games(SQLModel, table=True):
    __tablename__ = 'Games'
    __table_args__ = (
        ForeignKeyConstraint(['AssistantId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Games_Users_AssistantId'),
        ForeignKeyConstraint(['MasterId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Games_Users_MasterId'),
        ForeignKeyConstraint(['NannyId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Games_Users_NannyId'),
        PrimaryKeyConstraint('GameId', name='PK_Games'),
        Index('IX_Games_AssistantId', 'AssistantId'),
        Index('IX_Games_MasterId', 'MasterId'),
        Index('IX_Games_NannyId', 'NannyId')
    )

    GameId: str = Field(sa_column=Column('GameId', UUID))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    Status: int = Field(sa_column=Column('Status', Integer, nullable=False))
    MasterId: str = Field(sa_column=Column('MasterId', UUID, nullable=False))
    HideTemper: bool = Field(sa_column=Column('HideTemper', Boolean, nullable=False))
    HideSkills: bool = Field(sa_column=Column('HideSkills', Boolean, nullable=False))
    HideInventory: bool = Field(sa_column=Column('HideInventory', Boolean, nullable=False))
    HideStory: bool = Field(sa_column=Column('HideStory', Boolean, nullable=False))
    DisableAlignment: bool = Field(sa_column=Column('DisableAlignment', Boolean, nullable=False))
    HideDiceResult: bool = Field(sa_column=Column('HideDiceResult', Boolean, nullable=False))
    ShowPrivateMessages: bool = Field(sa_column=Column('ShowPrivateMessages', Boolean, nullable=False))
    CommentariesAccessMode: int = Field(sa_column=Column('CommentariesAccessMode', Integer, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    ReleaseDate: Optional[datetime] = Field(default=None, sa_column=Column('ReleaseDate', DateTime(True)))
    AssistantId: Optional[str] = Field(default=None, sa_column=Column('AssistantId', UUID))
    NannyId: Optional[str] = Field(default=None, sa_column=Column('NannyId', UUID))
    AttributeSchemaId: Optional[str] = Field(default=None, sa_column=Column('AttributeSchemaId', UUID))
    Title: Optional[str] = Field(default=None, sa_column=Column('Title', Text))
    SystemName: Optional[str] = Field(default=None, sa_column=Column('SystemName', Text))
    SettingName: Optional[str] = Field(default=None, sa_column=Column('SettingName', Text))
    Info: Optional[str] = Field(default=None, sa_column=Column('Info', Text))
    Notepad: Optional[str] = Field(default=None, sa_column=Column('Notepad', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Games')
    Users1: Optional['Users'] = Relationship(back_populates='Games_')
    Users2: Optional['Users'] = Relationship(back_populates='Games1')
    BlackListLinks: List['BlackListLinks'] = Relationship(back_populates='Games_')
    Characters: List['Characters'] = Relationship(back_populates='Games_')
    GameTags: List['GameTags'] = Relationship(back_populates='Games_')
    Readers: List['Readers'] = Relationship(back_populates='Games_')
    Rooms: List['Rooms'] = Relationship(back_populates='Games_')
    Votes: List['Votes'] = Relationship(back_populates='Games_')


class Likes(SQLModel, table=True):
    __tablename__ = 'Likes'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Likes_Users_UserId'),
        PrimaryKeyConstraint('LikeId', name='PK_Likes'),
        Index('IX_Likes_EntityId', 'EntityId'),
        Index('IX_Likes_UserId', 'UserId')
    )

    LikeId: str = Field(sa_column=Column('LikeId', UUID))
    EntityId: str = Field(sa_column=Column('EntityId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))

    Users_: Optional['Users'] = Relationship(back_populates='Likes')


class Reports(SQLModel, table=True):
    __tablename__ = 'Reports'
    __table_args__ = (
        ForeignKeyConstraint(['AnswerAuthorId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Reports_Users_AnswerAuthorId'),
        ForeignKeyConstraint(['TargetId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reports_Users_TargetId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reports_Users_UserId'),
        PrimaryKeyConstraint('ReportId', name='PK_Reports'),
        Index('IX_Reports_AnswerAuthorId', 'AnswerAuthorId'),
        Index('IX_Reports_TargetId', 'TargetId'),
        Index('IX_Reports_UserId', 'UserId')
    )

    ReportId: str = Field(sa_column=Column('ReportId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    TargetId: str = Field(sa_column=Column('TargetId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    ReportText: Optional[str] = Field(default=None, sa_column=Column('ReportText', Text))
    Comment: Optional[str] = Field(default=None, sa_column=Column('Comment', Text))
    AnswerAuthorId: Optional[str] = Field(default=None, sa_column=Column('AnswerAuthorId', UUID))
    Answer: Optional[str] = Field(default=None, sa_column=Column('Answer', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Reports')
    Users1: Optional['Users'] = Relationship(back_populates='Reports_')
    Users2: Optional['Users'] = Relationship(back_populates='Reports1')


class Reviews(SQLModel, table=True):
    __tablename__ = 'Reviews'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reviews_Users_UserId'),
        PrimaryKeyConstraint('ReviewId', name='PK_Reviews'),
        Index('IX_Reviews_UserId', 'UserId')
    )

    ReviewId: str = Field(sa_column=Column('ReviewId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    IsApproved: bool = Field(sa_column=Column('IsApproved', Boolean, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False, server_default=text('false')))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Reviews')


class Tags(SQLModel, table=True):
    __tablename__ = 'Tags'
    __table_args__ = (
        ForeignKeyConstraint(['TagGroupId'], ['TagGroups.TagGroupId'], ondelete='CASCADE', name='FK_Tags_TagGroups_TagGroupId'),
        PrimaryKeyConstraint('TagId', name='PK_Tags'),
        Index('IX_Tags_TagGroupId', 'TagGroupId')
    )

    TagId: str = Field(sa_column=Column('TagId', UUID))
    TagGroupId: str = Field(sa_column=Column('TagGroupId', UUID, nullable=False))
    Title: Optional[str] = Field(default=None, sa_column=Column('Title', Text))

    TagGroups_: Optional['TagGroups'] = Relationship(back_populates='Tags')
    GameTags: List['GameTags'] = Relationship(back_populates='Tags_')


class Tokens(SQLModel, table=True):
    __tablename__ = 'Tokens'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Tokens_Users_UserId'),
        PrimaryKeyConstraint('TokenId', name='PK_Tokens'),
        Index('IX_Tokens_EntityId', 'EntityId'),
        Index('IX_Tokens_UserId', 'UserId')
    )

    TokenId: str = Field(sa_column=Column('TokenId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    Type: int = Field(sa_column=Column('Type', Integer, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    EntityId: Optional[str] = Field(default=None, sa_column=Column('EntityId', UUID))

    Users_: Optional['Users'] = Relationship(back_populates='Tokens')


class Uploads(SQLModel, table=True):
    __tablename__ = 'Uploads'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Uploads_Users_UserId'),
        PrimaryKeyConstraint('UploadId', name='PK_Uploads'),
        Index('IX_Uploads_EntityId', 'EntityId'),
        Index('IX_Uploads_UserId', 'UserId')
    )

    UploadId: str = Field(sa_column=Column('UploadId', UUID))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Original: bool = Field(sa_column=Column('Original', Boolean, nullable=False, server_default=text('false')))
    EntityId: Optional[str] = Field(default=None, sa_column=Column('EntityId', UUID))
    FilePath: Optional[str] = Field(default=None, sa_column=Column('FilePath', Text))
    FileName: Optional[str] = Field(default=None, sa_column=Column('FileName', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Uploads')


class UserConversationLinks(SQLModel, table=True):
    __tablename__ = 'UserConversationLinks'
    __table_args__ = (
        ForeignKeyConstraint(['ConversationId'], ['Conversations.ConversationId'], ondelete='CASCADE', name='FK_UserConversationLinks_Conversations_ConversationId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_UserConversationLinks_Users_UserId'),
        PrimaryKeyConstraint('UserConversationLinkId', name='PK_UserConversationLinks'),
        Index('IX_UserConversationLinks_ConversationId', 'ConversationId'),
        Index('IX_UserConversationLinks_UserId', 'UserId')
    )

    UserConversationLinkId: str = Field(sa_column=Column('UserConversationLinkId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    ConversationId: str = Field(sa_column=Column('ConversationId', UUID, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))

    Conversations_: Optional['Conversations'] = Relationship(back_populates='UserConversationLinks')
    Users_: Optional['Users'] = Relationship(back_populates='UserConversationLinks')


class Warnings(SQLModel, table=True):
    __tablename__ = 'Warnings'
    __table_args__ = (
        ForeignKeyConstraint(['ModeratorId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Warnings_Users_ModeratorId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Warnings_Users_UserId'),
        PrimaryKeyConstraint('WarningId', name='PK_Warnings'),
        Index('IX_Warnings_EntityId', 'EntityId'),
        Index('IX_Warnings_ModeratorId', 'ModeratorId'),
        Index('IX_Warnings_UserId', 'UserId')
    )

    WarningId: str = Field(sa_column=Column('WarningId', UUID))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    ModeratorId: str = Field(sa_column=Column('ModeratorId', UUID, nullable=False))
    EntityId: str = Field(sa_column=Column('EntityId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    Points: int = Field(sa_column=Column('Points', Integer, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))

    Users_: Optional['Users'] = Relationship(back_populates='Warnings')
    Users1: Optional['Users'] = Relationship(back_populates='Warnings_')


class BlackListLinks(SQLModel, table=True):
    __tablename__ = 'BlackListLinks'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_BlackListLinks_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_BlackListLinks_Users_UserId'),
        PrimaryKeyConstraint('BlackListLinkId', name='PK_BlackListLinks'),
        Index('IX_BlackListLinks_GameId', 'GameId'),
        Index('IX_BlackListLinks_UserId', 'UserId')
    )

    BlackListLinkId: str = Field(sa_column=Column('BlackListLinkId', UUID))
    GameId: str = Field(sa_column=Column('GameId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))

    Games_: Optional['Games'] = Relationship(back_populates='BlackListLinks')
    Users_: Optional['Users'] = Relationship(back_populates='BlackListLinks')


class Characters(SQLModel, table=True):
    __tablename__ = 'Characters'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Characters_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Characters_Users_UserId'),
        PrimaryKeyConstraint('CharacterId', name='PK_Characters'),
        Index('IX_Characters_GameId', 'GameId'),
        Index('IX_Characters_UserId', 'UserId')
    )

    CharacterId: str = Field(sa_column=Column('CharacterId', UUID))
    GameId: str = Field(sa_column=Column('GameId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    Status: int = Field(sa_column=Column('Status', Integer, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    IsNpc: bool = Field(sa_column=Column('IsNpc', Boolean, nullable=False))
    AccessPolicy: int = Field(sa_column=Column('AccessPolicy', Integer, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    LastUpdateDate: Optional[datetime] = Field(default=None, sa_column=Column('LastUpdateDate', DateTime(True)))
    Name: Optional[str] = Field(default=None, sa_column=Column('Name', Text))
    Race: Optional[str] = Field(default=None, sa_column=Column('Race', Text))
    Class: Optional[str] = Field(default=None, sa_column=Column('Class', Text))
    Alignment: Optional[int] = Field(default=None, sa_column=Column('Alignment', Integer))
    Appearance: Optional[str] = Field(default=None, sa_column=Column('Appearance', Text))
    Temper: Optional[str] = Field(default=None, sa_column=Column('Temper', Text))
    Story: Optional[str] = Field(default=None, sa_column=Column('Story', Text))
    Skills: Optional[str] = Field(default=None, sa_column=Column('Skills', Text))
    Inventory: Optional[str] = Field(default=None, sa_column=Column('Inventory', Text))

    Games_: Optional['Games'] = Relationship(back_populates='Characters')
    Users_: Optional['Users'] = Relationship(back_populates='Characters')
    CharacterAttributes: List['CharacterAttributes'] = Relationship(back_populates='Characters_')
    Posts: List['Posts'] = Relationship(back_populates='Characters_')
    RoomClaims: List['RoomClaims'] = Relationship(back_populates='Characters_')


class ForumTopics(SQLModel, table=True):
    __tablename__ = 'ForumTopics'
    __table_args__ = (
        ForeignKeyConstraint(['ForumId'], ['Fora.ForumId'], ondelete='CASCADE', name='FK_ForumTopics_Fora_ForumId'),
        ForeignKeyConstraint(['LastCommentId'], ['Comments.CommentId'], ondelete='RESTRICT', name='FK_ForumTopics_Comments_LastCommentId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ForumTopics_Users_UserId'),
        PrimaryKeyConstraint('ForumTopicId', name='PK_ForumTopics'),
        Index('IX_ForumTopics_ForumId', 'ForumId'),
        Index('IX_ForumTopics_LastCommentId', 'LastCommentId'),
        Index('IX_ForumTopics_UserId', 'UserId')
    )

    ForumTopicId: str = Field(sa_column=Column('ForumTopicId', UUID))
    ForumId: str = Field(sa_column=Column('ForumId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    Attached: bool = Field(sa_column=Column('Attached', Boolean, nullable=False))
    Closed: bool = Field(sa_column=Column('Closed', Boolean, nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Title: Optional[str] = Field(default=None, sa_column=Column('Title', Text))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))
    LastCommentId: Optional[str] = Field(default=None, sa_column=Column('LastCommentId', UUID))

    Fora_: Optional['Fora'] = Relationship(back_populates='ForumTopics')
    Comments_: Optional['Comments'] = Relationship(back_populates='ForumTopics')
    Users_: Optional['Users'] = Relationship(back_populates='ForumTopics')


class GameTags(SQLModel, table=True):
    __tablename__ = 'GameTags'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_GameTags_Games_GameId'),
        ForeignKeyConstraint(['TagId'], ['Tags.TagId'], ondelete='CASCADE', name='FK_GameTags_Tags_TagId'),
        PrimaryKeyConstraint('GameTagId', name='PK_GameTags'),
        Index('IX_GameTags_GameId', 'GameId'),
        Index('IX_GameTags_TagId', 'TagId')
    )

    GameTagId: str = Field(sa_column=Column('GameTagId', UUID))
    GameId: str = Field(sa_column=Column('GameId', UUID, nullable=False))
    TagId: str = Field(sa_column=Column('TagId', UUID, nullable=False))

    Games_: Optional['Games'] = Relationship(back_populates='GameTags')
    Tags_: Optional['Tags'] = Relationship(back_populates='GameTags')


class Readers(SQLModel, table=True):
    __tablename__ = 'Readers'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Readers_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Readers_Users_UserId'),
        PrimaryKeyConstraint('ReaderId', name='PK_Readers'),
        Index('IX_Readers_GameId', 'GameId'),
        Index('IX_Readers_UserId', 'UserId')
    )

    ReaderId: str = Field(sa_column=Column('ReaderId', UUID))
    GameId: str = Field(sa_column=Column('GameId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))

    Games_: Optional['Games'] = Relationship(back_populates='Readers')
    Users_: Optional['Users'] = Relationship(back_populates='Readers')
    RoomClaims: List['RoomClaims'] = Relationship(back_populates='Readers_')


class Rooms(SQLModel, table=True):
    __tablename__ = 'Rooms'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Rooms_Games_GameId'),
        ForeignKeyConstraint(['NextRoomId'], ['Rooms.RoomId'], ondelete='RESTRICT', name='FK_Rooms_Rooms_NextRoomId'),
        ForeignKeyConstraint(['PreviousRoomId'], ['Rooms.RoomId'], ondelete='RESTRICT', name='FK_Rooms_Rooms_PreviousRoomId'),
        PrimaryKeyConstraint('RoomId', name='PK_Rooms'),
        Index('IX_Rooms_GameId', 'GameId'),
        Index('IX_Rooms_NextRoomId', 'NextRoomId', unique=True),
        Index('IX_Rooms_PreviousRoomId', 'PreviousRoomId')
    )

    RoomId: str = Field(sa_column=Column('RoomId', UUID))
    GameId: str = Field(sa_column=Column('GameId', UUID, nullable=False))
    AccessType: int = Field(sa_column=Column('AccessType', Integer, nullable=False))
    Type: int = Field(sa_column=Column('Type', Integer, nullable=False))
    OrderNumber: float = Field(sa_column=Column('OrderNumber', Float(53), nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    Title: Optional[str] = Field(default=None, sa_column=Column('Title', Text))
    PreviousRoomId: Optional[str] = Field(default=None, sa_column=Column('PreviousRoomId', UUID))
    NextRoomId: Optional[str] = Field(default=None, sa_column=Column('NextRoomId', UUID))

    Games_: Optional['Games'] = Relationship(back_populates='Rooms')
    Rooms: Optional['Rooms'] = Relationship(back_populates='Rooms_reverse')
    Rooms_reverse: List['Rooms'] = Relationship(back_populates='Rooms')
    Rooms_: Optional['Rooms'] = Relationship(back_populates='Rooms__reverse')
    Rooms__reverse: List['Rooms'] = Relationship(back_populates='Rooms_')
    PendingPosts: List['PendingPosts'] = Relationship(back_populates='Rooms_')
    Posts: List['Posts'] = Relationship(back_populates='Rooms_')
    RoomClaims: List['RoomClaims'] = Relationship(back_populates='Rooms_')


class CharacterAttributes(SQLModel, table=True):
    __tablename__ = 'CharacterAttributes'
    __table_args__ = (
        ForeignKeyConstraint(['CharacterId'], ['Characters.CharacterId'], ondelete='CASCADE', name='FK_CharacterAttributes_Characters_CharacterId'),
        PrimaryKeyConstraint('CharacterAttributeId', name='PK_CharacterAttributes'),
        Index('IX_CharacterAttributes_CharacterId', 'CharacterId')
    )

    CharacterAttributeId: str = Field(sa_column=Column('CharacterAttributeId', UUID))
    AttributeId: str = Field(sa_column=Column('AttributeId', UUID, nullable=False))
    CharacterId: str = Field(sa_column=Column('CharacterId', UUID, nullable=False))
    Value: Optional[str] = Field(default=None, sa_column=Column('Value', Text))

    Characters_: Optional['Characters'] = Relationship(back_populates='CharacterAttributes')


class PendingPosts(SQLModel, table=True):
    __tablename__ = 'PendingPosts'
    __table_args__ = (
        ForeignKeyConstraint(['AwaitingUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_PendingPosts_Users_AwaitingUserId'),
        ForeignKeyConstraint(['PendingUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_PendingPosts_Users_PendingUserId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_PendingPosts_Rooms_RoomId'),
        PrimaryKeyConstraint('PendingPostId', name='PK_PendingPosts'),
        Index('IX_PendingPosts_AwaitingUserId', 'AwaitingUserId'),
        Index('IX_PendingPosts_PendingUserId', 'PendingUserId'),
        Index('IX_PendingPosts_RoomId', 'RoomId')
    )

    PendingPostId: str = Field(sa_column=Column('PendingPostId', UUID))
    AwaitingUserId: str = Field(sa_column=Column('AwaitingUserId', UUID, nullable=False))
    PendingUserId: str = Field(sa_column=Column('PendingUserId', UUID, nullable=False))
    RoomId: str = Field(sa_column=Column('RoomId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))

    Users_: Optional['Users'] = Relationship(back_populates='PendingPosts')
    Users1: Optional['Users'] = Relationship(back_populates='PendingPosts_')
    Rooms_: Optional['Rooms'] = Relationship(back_populates='PendingPosts')


class Posts(SQLModel, table=True):
    __tablename__ = 'Posts'
    __table_args__ = (
        ForeignKeyConstraint(['CharacterId'], ['Characters.CharacterId'], ondelete='RESTRICT', name='FK_Posts_Characters_CharacterId'),
        ForeignKeyConstraint(['LastUpdateUserId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Posts_Users_LastUpdateUserId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_Posts_Rooms_RoomId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Posts_Users_UserId'),
        PrimaryKeyConstraint('PostId', name='PK_Posts'),
        Index('IX_Posts_CharacterId', 'CharacterId'),
        Index('IX_Posts_LastUpdateUserId', 'LastUpdateUserId'),
        Index('IX_Posts_RoomId', 'RoomId'),
        Index('IX_Posts_UserId', 'UserId')
    )

    PostId: str = Field(sa_column=Column('PostId', UUID))
    RoomId: str = Field(sa_column=Column('RoomId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    IsRemoved: bool = Field(sa_column=Column('IsRemoved', Boolean, nullable=False))
    CharacterId: Optional[str] = Field(default=None, sa_column=Column('CharacterId', UUID))
    LastUpdateUserId: Optional[str] = Field(default=None, sa_column=Column('LastUpdateUserId', UUID))
    LastUpdateDate: Optional[datetime] = Field(default=None, sa_column=Column('LastUpdateDate', DateTime(True)))
    Text_: Optional[str] = Field(default=None, sa_column=Column('Text', Text))
    Commentary: Optional[str] = Field(default=None, sa_column=Column('Commentary', Text))
    MasterMessage: Optional[str] = Field(default=None, sa_column=Column('MasterMessage', Text))

    Characters_: Optional['Characters'] = Relationship(back_populates='Posts')
    Users_: Optional['Users'] = Relationship(back_populates='Posts')
    Rooms_: Optional['Rooms'] = Relationship(back_populates='Posts')
    Users1: Optional['Users'] = Relationship(back_populates='Posts_')
    Votes: List['Votes'] = Relationship(back_populates='Posts_')


class RoomClaims(SQLModel, table=True):
    __tablename__ = 'RoomClaims'
    __table_args__ = (
        ForeignKeyConstraint(['ParticipantId'], ['Readers.ReaderId'], ondelete='CASCADE', name='FK_RoomClaims_Readers_ParticipantId'),
        ForeignKeyConstraint(['ParticipantId'], ['Characters.CharacterId'], ondelete='CASCADE', name='FK_RoomClaims_Characters_ParticipantId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_RoomClaims_Rooms_RoomId'),
        PrimaryKeyConstraint('RoomClaimId', name='PK_RoomClaims'),
        Index('IX_RoomClaims_ParticipantId', 'ParticipantId'),
        Index('IX_RoomClaims_RoomId', 'RoomId')
    )

    RoomClaimId: str = Field(sa_column=Column('RoomClaimId', UUID))
    ParticipantId: str = Field(sa_column=Column('ParticipantId', UUID, nullable=False))
    RoomId: str = Field(sa_column=Column('RoomId', UUID, nullable=False))
    Policy: int = Field(sa_column=Column('Policy', Integer, nullable=False))

    Readers_: Optional['Readers'] = Relationship(back_populates='RoomClaims')
    Characters_: Optional['Characters'] = Relationship(back_populates='RoomClaims')
    Rooms_: Optional['Rooms'] = Relationship(back_populates='RoomClaims')


class Votes(SQLModel, table=True):
    __tablename__ = 'Votes'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Votes_Games_GameId'),
        ForeignKeyConstraint(['PostId'], ['Posts.PostId'], ondelete='CASCADE', name='FK_Votes_Posts_PostId'),
        ForeignKeyConstraint(['TargetUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Votes_Users_TargetUserId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Votes_Users_UserId'),
        PrimaryKeyConstraint('VoteId', name='PK_Votes'),
        Index('IX_Votes_GameId', 'GameId'),
        Index('IX_Votes_PostId', 'PostId'),
        Index('IX_Votes_TargetUserId', 'TargetUserId'),
        Index('IX_Votes_UserId', 'UserId')
    )

    VoteId: str = Field(sa_column=Column('VoteId', UUID))
    PostId: str = Field(sa_column=Column('PostId', UUID, nullable=False))
    GameId: str = Field(sa_column=Column('GameId', UUID, nullable=False))
    UserId: str = Field(sa_column=Column('UserId', UUID, nullable=False))
    TargetUserId: str = Field(sa_column=Column('TargetUserId', UUID, nullable=False))
    CreateDate: datetime = Field(sa_column=Column('CreateDate', DateTime(True), nullable=False))
    Type: int = Field(sa_column=Column('Type', Integer, nullable=False))
    SignValue: int = Field(sa_column=Column('SignValue', SmallInteger, nullable=False))

    Games_: Optional['Games'] = Relationship(back_populates='Votes')
    Posts_: Optional['Posts'] = Relationship(back_populates='Votes')
    Users_: Optional['Users'] = Relationship(back_populates='Votes')
    Users1: Optional['Users'] = Relationship(back_populates='Votes_')
