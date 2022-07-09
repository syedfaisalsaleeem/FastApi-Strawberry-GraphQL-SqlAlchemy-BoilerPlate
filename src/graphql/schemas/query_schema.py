import strawberry
from pydantic import typing
from strawberry.types import Info
from src.graphql.scalars.stickynotes_scalar import StickyNotes

from src.graphql.resolvers.stickynote_resolver import get_stickynote, get_stickynotes
from src.graphql.resolvers.user_resolver import get_user, get_users
from src.graphql.scalars.user_scalar import User

@strawberry.type
class Query:

    @strawberry.field
    async def users(self, info:Info) -> typing.List[User]:
        """ Get all users """
        users_data_list = await get_users(info)
        return users_data_list

    @strawberry.field
    async def user(self, info:Info, user_id: int) -> User:
        """ Get user by id """
        user_dict = await get_user(user_id, info)
        return user_dict

    @strawberry.field
    async def stickynotes(self, info:Info) -> typing.List[StickyNotes]:
        """ Get all stickynotes """
        stickynotes_data_list = await get_stickynotes(info)
        return stickynotes_data_list

    @strawberry.field
    async def stickynote(self, info:Info, stickynote_id: int) -> StickyNotes:
        """ Get stickynote by id """
        stickynote_dict = await get_stickynote(stickynote_id, info)
        return stickynote_dict