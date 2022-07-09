import strawberry

from src.graphql.scalars.user_scalar import User, UserDeleted, UserExists, UserIdMissing, UserNotFound


AddUserResponse = strawberry.union("AddUserResponse", (User, UserExists))
DeleteUserResponse = strawberry.union("DeleteUserResponse", (UserDeleted,UserNotFound, UserIdMissing))