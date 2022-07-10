from tests.graphql.queries import get_users_query

def test_get_users(test_client):
    response = test_client.get(
        "/graphql",
        params = {
            "query": get_users_query,
        }
    )
    assert response.status_code == 200
    assert response.json()["data"]["users"] == []