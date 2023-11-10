import os
import requests

PLAYLIST_API_URL = os.environ.get(
    "PLAYLIST_API_URL", "http://127.0.0.1:8000/api/playlists/"
)


def fetch_all_playlists(access_token: str) -> list:
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    r = requests.get(
        PLAYLIST_API_URL,
        headers=headers,
    )
    if r.status_code == 200:
        return r.json()
    return []


def create_playlist(title: str, description: str, username: str, access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = {
        "title": title,
        "description": description,
        "username": username,
    }
    r = requests.post(
        PLAYLIST_API_URL,
        headers=headers,
        data=data,
    )
    if r.status_code == 201:
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
