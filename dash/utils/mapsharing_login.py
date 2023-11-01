import os
import requests

AUTH_API_URL = os.environ.get("AUTH_API_URL", "http://localhost:8000/api/token/")


def jwt_login(username: str, password: str):
    data = {"username": username, "password": password}
    # headers = {"Content-Type": "application/json"}
    r = requests.post(AUTH_API_URL, data=data)
    if r.status_code == 200:
        return r.json()["access"], r.json()["refresh"]
    return None, None
