from tests.conftest import TestAsynchronously
from tests.graphql.queries import get_users_query, get_specific_user_query, get_sticky_notes_query, get_specific_sticky_note_query
from tests.graphql.mutations import create_user, create_sticky_notes, delete_specific_user, update_specific_sticky_note, delete_specific_sticky_note
from src.app import schema

class TestUsers(TestAsynchronously):

    def test_01_an_async_get_all_users(self):
        resp = self.get_async_result(schema.execute(
            get_users_query,
        ))
        assert resp.data["users"] == []

    def test_02_an_async_create_users(self):
        resp = self.get_async_result(schema.execute(
            create_user,
        ))
        assert resp.data["addUser"] == {'id': 1, 'name': 'test'}

    def test_03_an_async_create_users_again(self):
        resp = self.get_async_result(schema.execute(
            create_user,
        ))
        assert resp.data == {'addUser': {'message': 'User with this name already exists'}}

    def test_04_an_async_create_sticky_notes_relative_to_user(self):
        resp = self.get_async_result(schema.execute(
            create_sticky_notes,
        ))

        for key_sticky_note in resp.data['addStickynotes'].keys():
            assert key_sticky_note in ['id','createdDatetime','text','userId'] 

    def test_05_an_async_get_all_users_with_created_user(self):
        resp = self.get_async_result(schema.execute(
            get_users_query,
        ))
        assert len(resp.data["users"]) == 1
        for key_user in resp.data["users"][0].keys():
            assert key_user in ['id','name','stickynotes'] 

        for key_sticky_note in resp.data["users"][0]['stickynotes'][0].keys():
            assert key_sticky_note in ['id','createdDatetime','text','userId'] 

    def test_06_an_async_get_specific_user(self):
        resp = self.get_async_result(schema.execute(
            get_specific_user_query,
        ))
        for key_user in resp.data["user"].keys():
            assert key_user in ['id','name','stickynotes'] 
      
        for key_sticky_note in resp.data["user"]['stickynotes'][0].keys():
            assert key_sticky_note in ['id','createdDatetime','text','userId']

    def test_07_an_async_get_all_stickynotes(self):
        resp = self.get_async_result(schema.execute(
            get_sticky_notes_query,
        ))

        assert len(resp.data["stickynotes"]) == 1
        for key_sticky_note in resp.data['stickynotes'][0].keys():
            assert key_sticky_note in ['id','createdDatetime','text','userId']
    
    def test_08_an_async_get_specific_stickynote(self):
        resp = self.get_async_result(schema.execute(
            get_specific_sticky_note_query,
        ))

        for key_sticky_note in resp.data['stickynote'].keys():
            assert key_sticky_note in ['id','createdDatetime','text','userId']

    def test_09_an_async_update_specific_stickynote(self):
        resp = self.get_async_result(schema.execute(
            update_specific_sticky_note,
            variable_values={
            "stickynoteId": 1,
            "text": "new text",
            }
        ))

        assert resp.data["updateStickynote"]["text"] == "new text"
        for key_sticky_note in resp.data["updateStickynote"].keys():
            assert key_sticky_note in ['id','createdDatetime','text','userId']

    def test_10_an_async_delete_specific_stickynote(self):
        resp = self.get_async_result(schema.execute(
            delete_specific_sticky_note,
        ))

        assert resp.data == {"deleteStickynote": {"message": "Sticky Notes deleted"}}

        resp = self.get_async_result(schema.execute(
            delete_specific_sticky_note,
        ))
        assert resp.data == {"deleteStickynote": { "message": "Couldn't find sticky notes with the supplied id"}}

    def test_11_an_async_delete_specific_user(self):
        resp = self.get_async_result(schema.execute(
            delete_specific_user,
        ))
        assert resp.data == {"deleteUser": {"message": "User deleted"}}
        resp = self.get_async_result(schema.execute(
            delete_specific_user,
        ))
        assert resp.data == {"deleteUser": { "message": "Couldn't find user with the supplied id"}}
    
    def test_12_an_async_get_all_users(self):
        resp = self.get_async_result(schema.execute(
            get_users_query,
        ))
        assert resp.data["users"] == []