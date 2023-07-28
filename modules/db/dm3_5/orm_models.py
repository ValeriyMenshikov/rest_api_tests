from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, SmallInteger, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Conversation(Base):
    __tablename__ = 'Conversations'

    ConversationId = Column(UUID, primary_key=True)
    LastMessageId = Column(ForeignKey('Messages.MessageId', ondelete='RESTRICT'), index=True)
    Visavi = Column(Boolean, nullable=False, server_default=text("false"))

    Message = relationship('Message', primaryjoin='Conversation.LastMessageId == Message.MessageId')


class Fora(Base):
    __tablename__ = 'Fora'

    ForumId = Column(UUID, primary_key=True)
    Title = Column(Text)
    Description = Column(Text)
    Order = Column(Integer, nullable=False)
    ViewPolicy = Column(Integer, nullable=False)
    CreateTopicPolicy = Column(Integer, nullable=False)


class Message(Base):
    __tablename__ = 'Messages'

    MessageId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ConversationId = Column(ForeignKey('Conversations.ConversationId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)

    Conversation = relationship('Conversation', primaryjoin='Message.ConversationId == Conversation.ConversationId')
    User = relationship('User')


class TagGroup(Base):
    __tablename__ = 'TagGroups'

    TagGroupId = Column(UUID, primary_key=True)
    Title = Column(Text)


class User(Base):
    __tablename__ = 'Users'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    RegistrationDate = Column(DateTime(True), nullable=False)
    LastVisitDate = Column(DateTime(True))
    TimezoneId = Column(Text)
    Role = Column(Integer, nullable=False)
    AccessPolicy = Column(Integer, nullable=False)
    Salt = Column(String(120))
    PasswordHash = Column(String(300))
    RatingDisabled = Column(Boolean, nullable=False)
    QualityRating = Column(Integer, nullable=False)
    QuantityRating = Column(Integer, nullable=False)
    Activated = Column(Boolean, nullable=False)
    CanMerge = Column(Boolean, nullable=False)
    MergeRequested = Column(UUID)
    IsRemoved = Column(Boolean, nullable=False)
    Status = Column(String(200))
    Name = Column(String(100))
    Location = Column(String(100))
    Icq = Column(String(20))
    Skype = Column(String(50))
    Info = Column(Text)
    ProfilePictureUrl = Column(String(200))
    MediumProfilePictureUrl = Column(String(200))
    SmallProfilePictureUrl = Column(String(200))


class EFMigrationsHistory(Base):
    __tablename__ = '__EFMigrationsHistory'

    MigrationId = Column(String(150), primary_key=True)
    ProductVersion = Column(String(32), nullable=False)


class Ban(Base):
    __tablename__ = 'Bans'

    BanId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ModeratorId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    StartDate = Column(DateTime(True), nullable=False)
    EndDate = Column(DateTime(True), nullable=False)
    Comment = Column(Text)
    AccessRestrictionPolicy = Column(Integer, nullable=False)
    IsVoluntary = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User', primaryjoin='Ban.ModeratorId == User.UserId')
    User1 = relationship('User', primaryjoin='Ban.UserId == User.UserId')


class ChatMessage(Base):
    __tablename__ = 'ChatMessages'

    ChatMessageId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(Text)

    User = relationship('User')


class Comment(Base):
    __tablename__ = 'Comments'

    CommentId = Column(UUID, primary_key=True)
    EntityId = Column(UUID, nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    LastUpdateDate = Column(DateTime(True))
    Text = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User')


class ForumModerator(Base):
    __tablename__ = 'ForumModerators'

    ForumModeratorId = Column(UUID, primary_key=True)
    ForumId = Column(ForeignKey('Fora.ForumId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    Fora = relationship('Fora')
    User = relationship('User')


class Game(Base):
    __tablename__ = 'Games'

    GameId = Column(UUID, primary_key=True)
    CreateDate = Column(DateTime(True), nullable=False)
    ReleaseDate = Column(DateTime(True))
    Status = Column(Integer, nullable=False)
    MasterId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    AssistantId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    NannyId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    AttributeSchemaId = Column(UUID)
    Title = Column(Text)
    SystemName = Column(Text)
    SettingName = Column(Text)
    Info = Column(Text)
    HideTemper = Column(Boolean, nullable=False)
    HideSkills = Column(Boolean, nullable=False)
    HideInventory = Column(Boolean, nullable=False)
    HideStory = Column(Boolean, nullable=False)
    DisableAlignment = Column(Boolean, nullable=False)
    HideDiceResult = Column(Boolean, nullable=False)
    ShowPrivateMessages = Column(Boolean, nullable=False)
    CommentariesAccessMode = Column(Integer, nullable=False)
    Notepad = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User', primaryjoin='Game.AssistantId == User.UserId')
    User1 = relationship('User', primaryjoin='Game.MasterId == User.UserId')
    User2 = relationship('User', primaryjoin='Game.NannyId == User.UserId')


class Like(Base):
    __tablename__ = 'Likes'

    LikeId = Column(UUID, primary_key=True)
    EntityId = Column(UUID, nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    User = relationship('User')


class Report(Base):
    __tablename__ = 'Reports'

    ReportId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    TargetId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    ReportText = Column(Text)
    Comment = Column(Text)
    AnswerAuthorId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    Answer = Column(Text)

    User = relationship('User', primaryjoin='Report.AnswerAuthorId == User.UserId')
    User1 = relationship('User', primaryjoin='Report.TargetId == User.UserId')
    User2 = relationship('User', primaryjoin='Report.UserId == User.UserId')


class Review(Base):
    __tablename__ = 'Reviews'

    ReviewId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(Text)
    IsApproved = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False, server_default=text("false"))

    User = relationship('User')


class Tag(Base):
    __tablename__ = 'Tags'

    TagId = Column(UUID, primary_key=True)
    TagGroupId = Column(ForeignKey('TagGroups.TagGroupId', ondelete='CASCADE'), nullable=False, index=True)
    Title = Column(Text)

    TagGroup = relationship('TagGroup')


class Token(Base):
    __tablename__ = 'Tokens'

    TokenId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    EntityId = Column(UUID, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Type = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User')


class Upload(Base):
    __tablename__ = 'Uploads'

    UploadId = Column(UUID, primary_key=True)
    CreateDate = Column(DateTime(True), nullable=False)
    EntityId = Column(UUID, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    FilePath = Column(Text)
    FileName = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)
    Original = Column(Boolean, nullable=False, server_default=text("false"))

    User = relationship('User')


class UserConversationLink(Base):
    __tablename__ = 'UserConversationLinks'

    UserConversationLinkId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ConversationId = Column(ForeignKey('Conversations.ConversationId', ondelete='CASCADE'), nullable=False, index=True)
    IsRemoved = Column(Boolean, nullable=False)

    Conversation = relationship('Conversation')
    User = relationship('User')


class Warning(Base):
    __tablename__ = 'Warnings'

    WarningId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ModeratorId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    EntityId = Column(UUID, nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(Text)
    Points = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User', primaryjoin='Warning.ModeratorId == User.UserId')
    User1 = relationship('User', primaryjoin='Warning.UserId == User.UserId')


class BlackListLink(Base):
    __tablename__ = 'BlackListLinks'

    BlackListLinkId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    Game = relationship('Game')
    User = relationship('User')


class Character(Base):
    __tablename__ = 'Characters'

    CharacterId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    Status = Column(Integer, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    LastUpdateDate = Column(DateTime(True))
    Name = Column(Text)
    Race = Column(Text)
    Class = Column(Text)
    Alignment = Column(Integer)
    Appearance = Column(Text)
    Temper = Column(Text)
    Story = Column(Text)
    Skills = Column(Text)
    Inventory = Column(Text)
    IsNpc = Column(Boolean, nullable=False)
    AccessPolicy = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    Game = relationship('Game')
    User = relationship('User')


class ForumTopic(Base):
    __tablename__ = 'ForumTopics'

    ForumTopicId = Column(UUID, primary_key=True)
    ForumId = Column(ForeignKey('Fora.ForumId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Title = Column(Text)
    Text = Column(Text)
    Attached = Column(Boolean, nullable=False)
    Closed = Column(Boolean, nullable=False)
    LastCommentId = Column(ForeignKey('Comments.CommentId', ondelete='RESTRICT'), index=True)
    IsRemoved = Column(Boolean, nullable=False)

    Fora = relationship('Fora')
    Comment = relationship('Comment')
    User = relationship('User')


class GameTag(Base):
    __tablename__ = 'GameTags'

    GameTagId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    TagId = Column(ForeignKey('Tags.TagId', ondelete='CASCADE'), nullable=False, index=True)

    Game = relationship('Game')
    Tag = relationship('Tag')


class Reader(Base):
    __tablename__ = 'Readers'

    ReaderId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    Game = relationship('Game')
    User = relationship('User')


class Room(Base):
    __tablename__ = 'Rooms'

    RoomId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    Title = Column(Text)
    AccessType = Column(Integer, nullable=False)
    Type = Column(Integer, nullable=False)
    OrderNumber = Column(Float(53), nullable=False)
    PreviousRoomId = Column(ForeignKey('Rooms.RoomId', ondelete='RESTRICT'), index=True)
    NextRoomId = Column(ForeignKey('Rooms.RoomId', ondelete='RESTRICT'), unique=True)
    IsRemoved = Column(Boolean, nullable=False)

    Game = relationship('Game')
    parent = relationship('Room', remote_side=[RoomId], primaryjoin='Room.NextRoomId == Room.RoomId')
    parent1 = relationship('Room', remote_side=[RoomId], primaryjoin='Room.PreviousRoomId == Room.RoomId')


class CharacterAttribute(Base):
    __tablename__ = 'CharacterAttributes'

    CharacterAttributeId = Column(UUID, primary_key=True)
    AttributeId = Column(UUID, nullable=False)
    CharacterId = Column(ForeignKey('Characters.CharacterId', ondelete='CASCADE'), nullable=False, index=True)
    Value = Column(Text)

    Character = relationship('Character')


class PendingPost(Base):
    __tablename__ = 'PendingPosts'

    PendingPostId = Column(UUID, primary_key=True)
    AwaitingUserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    PendingUserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    RoomId = Column(ForeignKey('Rooms.RoomId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)

    User = relationship('User', primaryjoin='PendingPost.AwaitingUserId == User.UserId')
    User1 = relationship('User', primaryjoin='PendingPost.PendingUserId == User.UserId')
    Room = relationship('Room')


class Post(Base):
    __tablename__ = 'Posts'

    PostId = Column(UUID, primary_key=True)
    RoomId = Column(ForeignKey('Rooms.RoomId', ondelete='CASCADE'), nullable=False, index=True)
    CharacterId = Column(ForeignKey('Characters.CharacterId', ondelete='RESTRICT'), index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    LastUpdateUserId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    LastUpdateDate = Column(DateTime(True))
    Text = Column(String)
    Commentary = Column(String)
    MasterMessage = Column(String)
    IsRemoved = Column(Boolean, nullable=False)

    Character = relationship('Character')
    User = relationship('User', primaryjoin='Post.LastUpdateUserId == User.UserId')
    Room = relationship('Room')
    User1 = relationship('User', primaryjoin='Post.UserId == User.UserId')


class RoomClaim(Base):
    __tablename__ = 'RoomClaims'

    RoomClaimId = Column(UUID, primary_key=True)
    ParticipantId = Column(ForeignKey('Readers.ReaderId', ondelete='CASCADE'),
                           ForeignKey('Characters.CharacterId', ondelete='CASCADE'), nullable=False, index=True)
    RoomId = Column(ForeignKey('Rooms.RoomId', ondelete='CASCADE'), nullable=False, index=True)
    Policy = Column(Integer, nullable=False)

    Character = relationship('Character')
    Reader = relationship('Reader')
    Room = relationship('Room')


class Vote(Base):
    __tablename__ = 'Votes'

    VoteId = Column(UUID, primary_key=True)
    PostId = Column(ForeignKey('Posts.PostId', ondelete='CASCADE'), nullable=False, index=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    TargetUserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Type = Column(Integer, nullable=False)
    SignValue = Column(SmallInteger, nullable=False)

    Game = relationship('Game')
    Post = relationship('Post')
    User = relationship('User', primaryjoin='Vote.TargetUserId == User.UserId')
    User1 = relationship('User', primaryjoin='Vote.UserId == User.UserId')
