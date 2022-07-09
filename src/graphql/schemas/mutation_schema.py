import strawberry

from src.graphql.resolvers.stickynote_resolver import add_stickynotes, delete_stickynotes, update_stickynotes
from src.graphql.resolvers.user_resolver import add_user, delete_user
from src.graphql.fragments.stickynotes_fragments import AddStickyNotesResponse, DeleteStickyNotesResponse, UpdateStickyNotesResponse
from src.graphql.fragments.user_fragments import AddUserResponse, DeleteUserResponse


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_stickynotes(self, text: str, user_id: int) -> AddStickyNotesResponse:
        """ Add sticky note """
        add_stickynotes_resp = await add_stickynotes(text, user_id)
        return add_stickynotes_resp

    @strawberry.mutation
    async def add_user(self, name: str) -> AddUserResponse:
        """ Add user """
        add_user_resp = await add_user(name)
        return add_user_resp

    @strawberry.mutation
    async def delete_user(self, user_id: int) -> DeleteUserResponse:
        """ Delete user """
        delete_user_resp = await delete_user(user_id)
        return delete_user_resp

    @strawberry.mutation
    async def delete_stickynote(self, stickynote_id: int) -> DeleteStickyNotesResponse:
        """ Delete Sticky Notes """
        delete_stickynote_resp = await delete_stickynotes(stickynote_id)
        return delete_stickynote_resp

    @strawberry.mutation
    async def update_stickynote(self, stickynote_id: int, text: str) -> UpdateStickyNotesResponse:
        """ Update Sticky Notes """
        update_stickynote_resp = await update_stickynotes(stickynote_id, text)
        return update_stickynote_resp