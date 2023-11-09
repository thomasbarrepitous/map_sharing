import os
import requests

PLAYLIST_API_URL = os.environ.get(
    "AUTH_API_URL", "http://127.0.0.1:8000/api/playlists/"
)


def fetch_all_playlists(username: str, password: str, email: str):
    data = {"username": username, "password": password, "email": email}
    r = requests.post(f"{PLAYLIST_API_URL}/", data=data)
    if r.status_code == 200:
        return True
    return False


def remove_playlist_by_id(id: int, access_token: str):
    headers = {
        "User-Agent": "insomnia/8.3.0",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NjI1MDY3LCJpYXQiOjE2OTk1Mzg2NjcsImp0aSI6IjczMzM4MjNjZDhmMzRmODViYzRmM2YxNjY5NTYzNzY5IiwidXNlcl9pZCI6N30.aIs84W0If718ESSLdMz-9SGv_f9ol4sVKi3sMiSCLJE",
    }
    r = requests.post(
        f"{PLAYLIST_API_URL}{id}/",
        headers=headers,
    )
    if r.status_code == 200:
        return True
    return False
