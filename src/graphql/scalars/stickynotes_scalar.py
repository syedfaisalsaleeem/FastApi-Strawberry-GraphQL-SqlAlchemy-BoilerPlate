from datetime import datetime
from pydantic import Field, typing
import strawberry

@strawberry.type
class StickyNotes:
    id: int
    text: typing.Optional[str] = ""
    created_datetime : typing.Optional[datetime] = Field(default_factory=datetime.now)
    user_id: typing.Optional[int] = Field(description="User id")

@strawberry.type
class StickyNotesNotFound:
    message: str = "Couldn't find sticky notes with the supplied id"

@strawberry.type
class StickyNotesDeleted:
    message: str = "Sticky Notes deleted"

