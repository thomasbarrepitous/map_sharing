import os
import requests

AUTH_API_URL = os.environ.get("AUTH_API_URL", "http://127.0.0.1:8000/api/account/")


def create_account(username: str, password: str, email: str):
    data = {"username": username, "password": password, "email": email}
    r = requests.post(f"{AUTH_API_URL}register/", data=data)
    if r.status_code == 201:
        return True
    return False


def login_jwt(email: str, password: str):
    data = {"email": email, "password": password}
    r = requests.post(
        f"{AUTH_API_URL}login/",
        data=data,
    )
    if r.status_code == 200:
        return r.json()["access"], r.json()["refresh"]
    return None, None
