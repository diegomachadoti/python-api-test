import requests

def test_status_and_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = "http://dummy.restapiexample.com/api/v1/employees"

    resposta = requests.get(url, headers=headers)
    resposta_return = resposta.json()

    status = resposta_return['status']
    tamanho_list = len(resposta_return['data'])

    assert status == 'success'
    assert tamanho_list > 0