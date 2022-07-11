import asyncio
import unittest
import pytest
from src.graphql.db.session import get_session
from tests.graphql.db import overide_get_session
from main import application as app
app.dependency_overrides[get_session] = overide_get_session

@pytest.mark.usefixtures("event_loop_instance")
class TestAsynchronously(unittest.TestCase):

    def get_async_result(self, coro):
        """ Run a coroutine synchronously. """
        return self.event_loop.run_until_complete(coro)
        
@pytest.fixture(scope="class")
def event_loop_instance(request):
    """ Add the event_loop as an attribute to the unittest style test class. """
    request.cls.event_loop = asyncio.get_event_loop_policy().new_event_loop()
    yield
    request.cls.event_loop.close()
