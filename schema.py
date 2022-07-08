import strawberry
import typing
from pydantic import Field

@strawberry.type
class StickyNotes:
    id: int
    text: str

@strawberry.type
class User:
    id: int
    name: typing.Optional[str] = ""
    data = []
    stickynotes: typing.Optional[typing.List[StickyNotes]] = Field(default_factory=list)