## test graphql

import asyncio
from tests import load_test_env
import pytest
from populate import create_tables
from tests.graphql.db import engine 

if __name__ == "__main__":
    asyncio.run(create_tables(engine))
    pytest.main(args=[ "--cov=tests","tests/graphql/test_user_stickynotes.py","-s","--disable-warnings"])