import strawberry
from pydantic import Field, typing
from src.graphql.scalars.stickynotes_scalar import StickyNotes

@strawberry.type
class User:
    id: int
    name: typing.Optional[str] = ""
    stickynotes: typing.Optional[typing.List[StickyNotes]] = Field(default_factory=list)

@strawberry.type
class AddUser:
    id: int
    name: typing.Optional[str] = ""

@strawberry.type
class UserExists:
    message: str = "User with this name already exists"

@strawberry.type
class UserNotFound:
    message: str = "Couldn't find user with the supplied id"

@strawberry.type
class UserNameMissing:
    message: str = "Please supply user name"

@strawberry.type
class UserIdMissing:
    message: str = "Please supply user id"

@strawberry.type
class UserDeleted:
    message: str = "User deleted"

