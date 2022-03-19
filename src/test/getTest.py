import requests
import json
import jsonpath


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
    assert resposta_return["data"][0]["employee_name"] == "Tiger Nixon"


def test_search_registration():
    path = "https://reqres.in/api/users/4"
    response = requests.get(url=path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.email')[0] == "eve.holt@reqres.in"

