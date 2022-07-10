## test graphql

import load_env
import asyncio
import pytest
from main import application as app
from populate import create_tables
from tests.graphql.db import overide_get_session, engine
from src.graphql.db.session import get_session

app.dependency_overrides[get_session] = overide_get_session

if __name__ == "__main__":
    print("Populating database...")
    asyncio.run(create_tables(engine))
    print("Database populated.")
    
    pytest.main(args=[ "--cov=tests","tests/graphql","-s","--disable-warnings"])