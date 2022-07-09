from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from pydantic.typing import Optional
from . import Base, User

class StickyNotes(Base):
    __tablename__ = "stickynotes"
    id: int = Column(Integer, primary_key=True, index=True)
    text: str = Column(String, nullable=True)
    created_datetime: DateTime = Column(DateTime, nullable=False)
    user_id: Optional[int] = Column(Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "created_datetime": self.created_datetime,
            "user_id": self.user_id
        }