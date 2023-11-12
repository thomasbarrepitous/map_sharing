import os
import requests

API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000/api/")


def fetch_all_geocode_points(access_token: str) -> list:
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    r = requests.get(
        f"{API_URL}geocode-points/",
        headers=headers,
    )
    if r.status_code == 200:
        return r.json()
    return []


def fetch_geocode_point_by_playlist(id: int, access_token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    r = requests.get(
        f"{API_URL}playlists/{id}/geocode-points/",
        headers=headers,
    )
    if r.status_code == 200:
        return r.json()
    return {}


def create_geocode_point(
    title: str, description: str, username: str, access_token: str
):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = {}
    r = requests.post(
        f"{API_URL}geocode-points/",
        headers=headers,
        data=data,
    )
    if r.status_code == 201:
        return True
    return False


def remove_geocode_point_by_id(id: int, access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    r = requests.post(
        f"{API_URL}geocode-points/{id}/",
        headers=headers,
    )
    if r.status_code == 200:
        return True
    return False
