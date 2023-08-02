import requests

def test_update_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    new_data = {
        'id': 1,
        'title': 'Test Python',
        'body': 'Projeto de teste',
        'userId': '1'
    }

    post_id = 1

    url = "https://jsonplaceholder.typicode.com/posts/"

    resposta = requests.put(url+str(post_id), data=new_data, headers=headers)
    resposta_return = resposta.json()

    if resposta.status_code == 200:
        assert resposta_return == new_data

    else:
        assert False
