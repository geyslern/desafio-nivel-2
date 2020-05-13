from django.test import Client

def test_redirect_api_status_code(client: Client):
    response = client.get('/api')
    assert response.status_code == 301
def test_api_status_code(client: Client):
    response = client.get('/api/')
    assert response.status_code == 200