import requests
import json
import jsonpath
import random


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


def test_successful_registration():
    baseUrl = "https://reqres.in/"
    path = "api/register"
    response = requests.post(url=baseUrl+path, json=json.loads('{"email": "eve.holt@reqres.in","password": "'+randomDigits(5)+'"}'))
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert type(jsonpath.jsonpath(responseJson,'$.token')[0]) == str


def test_unsuccessful_registration():
    baseUrl = "https://reqres.in/"
    path = "api/register"
    response = requests.post(url=baseUrl+path, json=json.loads('{"email": "testemail@pytest.com"}'))
    responseJson = json.loads(response.text)
    assert response.status_code == 400
    assert jsonpath.jsonpath(responseJson,'$.error')[0] == 'Missing password'


def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return str(random.randint(lower, upper))