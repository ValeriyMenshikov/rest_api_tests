from sqlalchemy import create_engine, text, Column, String, Boolean, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Name = Column(String(100))
    Activated = Column(Boolean, nullable=False)
