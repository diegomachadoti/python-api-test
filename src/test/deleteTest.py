import requests

def test_delete_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    post_id = 1

    url = "https://jsonplaceholder.typicode.com/posts/"

    resposta = requests.put(url+str(post_id), headers=headers)
    resposta_return = resposta.json()

    assert resposta.status_code == 200
