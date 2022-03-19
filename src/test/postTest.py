import requests

def test_insert_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = "http://dummy.restapiexample.com/api/v1/create"

    data_request = {'name': 'Teste Python Diego', 'salary': '8500', 'age': 36}

    resposta = requests.post(url, headers=headers, data=data_request)
    resposta_return = resposta.json()

    if resposta.status_code == 200:
        status = resposta_return['status']
        employee_response = resposta_return['data']

        assert status == 'success'
        assert employee_response['id'] is not None
    else:
        assert False
