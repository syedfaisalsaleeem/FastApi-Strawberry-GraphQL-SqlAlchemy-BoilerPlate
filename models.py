from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from typing import List, Optional
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False, unique=True)

    stickynotes = relationship("StickyNotes")

class StickyNotes(Base):
    __tablename__ = "stickynotes"
    id: int = Column(Integer, primary_key=True, index=True)
    text: str = Column(String, nullable=True)
    created_datetime: DateTime = Column(DateTime, nullable=False)
    user_id: Optional[int] = Column(Integer, ForeignKey(User.id), nullable=True)