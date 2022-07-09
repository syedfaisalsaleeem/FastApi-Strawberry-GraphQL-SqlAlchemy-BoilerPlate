from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from src.graphql.schemas.mutation_schema import Mutation
from src.graphql.schemas.query_schema import Query

schema = strawberry.Schema(query=Query,mutation=Mutation)
graphql_app = GraphQLRouter(schema)

def create_app():
    
    app = FastAPI()
    app.include_router(graphql_app, prefix="/graphql",include_in_schema=False)

    return app