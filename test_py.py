import pytest
from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_search_empty_query(client):
    response = client.post('/search', data={'query': ''})
    assert response.status_code == 400
    assert b"Query is required" in response.data

def test_search_no_results(client):
    response = client.post('/search', data={'query': 'nonexistent query'})
    assert response.status_code == 404
    assert b"No results found" in response.data

def test_search_value_error(client):
    response = client.post('/search', data={'query': 'heart failure prevention'})
    assert response.status_code == 500
    assert b"Could not process the search query" in response.data