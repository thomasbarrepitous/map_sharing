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
        "Authorization": f"Bearer {access_token}",
    }
    r = requests.post(
        f"{PLAYLIST_API_URL}{id}/",
        headers=headers,
    )
    if r.status_code == 200:
        return True
    return False
