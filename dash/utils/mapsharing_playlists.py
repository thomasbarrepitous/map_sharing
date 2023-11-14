import os
import requests

API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000/api/")


def fetch_all_playlists(access_token: str) -> list:
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    r = requests.get(
        f"{API_URL}playlists/",
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
        f"{API_URL}playlists/",
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
    r = requests.delete(
        f"{API_URL}playlists/{id}/",
        headers=headers,
    )
    if r.status_code == 204:
        return True
    return False
