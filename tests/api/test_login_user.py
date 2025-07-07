import pytest
import requests
import pytest_check as check
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.api
def test_login_user():
    headers = {"x-api-key": os.getenv("X_API_KEY")}
    response = requests.post("https://reqres.in/api/login", json={"email": "eve.holt@reqres.in", "password": "cityslicka"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"