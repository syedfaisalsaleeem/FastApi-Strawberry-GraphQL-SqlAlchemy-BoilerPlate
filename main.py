from sqlalchemy import select
from sqlalchemy.orm import subqueryload,load_only
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import uvicorn
import asyncio
import db
from helper import get_valid_data, get_only_selected_fields
import models
import typing
from schema import User
from strawberry.types import Info

@strawberry.type
class Query:

    @strawberry.field
    async def users(self, info:Info) -> typing.List[User]:
        """ Get all users """
        selected_fields = get_only_selected_fields(models.User,info)
        async with db.get_session() as s:
            sql = select(models.User).options(load_only(*selected_fields)).options(subqueryload(models.User.stickynotes)).order_by(models.User.name)
            db_users = (await s.execute(sql)).scalars().unique().all()

        users_data_list = []
        for user in db_users:
            user_dict = get_valid_data(user,models.User)
            user_dict["stickynotes"] = user.stickynotes
            users_data_list.append(User(**user_dict))

        return users_data_list

    
    @strawberry.field
    async def user(self, info:Info, id: int) -> User:
        """ Get user by id """
        selected_fields = get_only_selected_fields(models.User,info)
        async with db.get_session() as s:
            sql = select(models.User).options(load_only(*selected_fields)).options(subqueryload(models.User.stickynotes)) \
            .filter(models.User.id == id).order_by(models.User.name)
            db_user = (await s.execute(sql)).scalars().unique().one()
        
        user_dict = get_valid_data(db_user,models.User)
        return User(**user_dict)

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

async def _async_main():
    async with db.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    await db.engine.dispose()

if __name__ == "__main__":
    print("creating tables")
    asyncio.run(_async_main())
    print("Done.")
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)