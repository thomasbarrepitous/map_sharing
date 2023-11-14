import os
import requests
import jwt

API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000/api/")
DJANGO_SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")


def create_account(username: str, password: str, email: str):
    data = {"username": username, "password": password, "email": email}
    r = requests.post(f"{API_URL}account/register/", data=data)
    if r.status_code == 201:
        return True
    return False


def login_jwt(email: str, password: str):
    data = {"email": email, "password": password}
    r = requests.post(
        f"{API_URL}account/login/",
        data=data,
    )
    if r.status_code == 200:
        return r.json()["access"], r.json()["refresh"]
    return None, None


def refresh_jwt(refresh_token: str):
    data = {"refresh": refresh_token}
    r = requests.post(
        f"{API_URL}account/login/refresh/",
        data=data,
    )
    if r.status_code == 200:
        return r.json()["access"]
    return None


def decode_jwt(token: str) -> dict | None:
    try:
        decoded_data = jwt.decode(
            jwt=token, key=DJANGO_SECRET_KEY, algorithms=["HS256"]
        )
    except jwt.exceptions.DecodeError:
        return None
    return decoded_data
