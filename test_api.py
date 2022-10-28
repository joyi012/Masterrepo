import requests
import json
import jsonpath
import random

baseUrl = "https://reqres.in/"


def test_successfull_registration():
    path = "api/register"
    responce = requests.post(url=baseUrl + path,
                             json=json.loads('{"email": "eve.holt@reqres.in","password": "' + randomDigits(5) + '"}'))
    responceJSon = json.loads(responce.text)
    assert responce.status_code == 200
    assert type(jsonpath.jsonpath(responceJSon, '$.token')[0]) == str

def test_unsccessfull_registration():
    path = "api/register"
    responce = requests.post(url=baseUrl + path,
                             json=json.loads('{"email": "testemail@pytest.com"}'))
    responceJSon = json.loads(responce.text)
    assert responce.status_code == 400
    assert type(jsonpath.jsonpath(responceJSon, '$.token')[0]) == str


def randomDigits(digits):
    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1
    return str(random.randint(lower, upper))
