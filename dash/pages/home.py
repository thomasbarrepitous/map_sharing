import dash
from dash import (
    callback,
    Output,
    Input,
    State,
    html,
    ctx,
    ALL,
    no_update,
    DiskcacheManager,
)
import googlemaps
import os
import uuid
import dash_leaflet as dl
from dash.exceptions import PreventUpdate
import utils.components.home as home_components
import utils.mapsharing_playlists as msplay
import utils.mapsharing_points as mspoints
import diskcache

dash.register_page(__name__, path="/")


# API Auth
gmaps = googlemaps.Client(key=os.environ.get("GCP_KEY"))
session_token = uuid.uuid4().hex

cache = diskcache.Cache("./cache")
background_callback_manager = DiskcacheManager(cache)


layout = html.Div(id="home-layout")


def validate_token(access_token):
    if access_token is None:
        return False
    return True


@callback(
    Output("home-layout", "children"),
    Input("access-token", "data"),
    Input("username", "data"),
)
def authenticated_layout_handler(access_token, username):
    if validate_token(access_token):
        return home_components.display_signed_in_layout(username)
    return home_components.signed_out_layout


@callback(
    Output("select", "data"),
    [Input("select", "searchValue")],
    prevent_initial_call=True,
)
def update_select(search_query):
    if search_query:
        try:
            # Fetch data from the API
            search_results = gmaps.places_autocomplete(
                session_token=session_token, input_text=search_query
            )
            # Create a map using the fetched data
            return [
                {"value": result["place_id"], "label": result["description"]}
                for result in search_results
            ]
        except Exception as e:
            print("ERROR : ", e)
    return []


@callback(
    Output("map", "viewport"),
    Output("map", "children"),
    [Input("select", "value")],
    prevent_initial_call=True,
)
def update_map(select_value):
    if select_value:
        try:
            geocode_result = gmaps.geocode(place_id=select_value)
            geocode_lon = geocode_result[0]["geometry"]["location"]["lng"]
            geocode_lat = geocode_result[0]["geometry"]["location"]["lat"]
            map_viewport = dict(
                center=[geocode_lat, geocode_lon], zoom=11, transition="flyTo"
            )
            map_children = [
                dl.TileLayer(),
                dl.Marker(position=[geocode_lat, geocode_lon]),
            ]
            return map_viewport, map_children
        except Exception as e:
            print("ERROR : ", e)
    return {}, [
        dl.TileLayer(),
    ]


@callback(
    Output({"type": "points-menu-accordion", "index": ALL}, "children"),
    Input({"type": "points-menu-accordion", "index": ALL}, "id"),
    Input("access-token", "data"),
)
def populate_points_menu(id, access_token):
    if access_token:
        clicked_index = id[0]["index"]
        points = mspoints.fetch_geocode_point_by_playlist(clicked_index, access_token)
        return [[home_components.single_geocode_template(point) for point in points]]


@callback(
    Output({"type": "playlists-menu-accordion", "index": ALL}, "children"),
    Input("toggle-menu-btn", "checked"),
    Input("access-token", "data"),
)
def populate_playlist_menu(checked, access_token):
    if checked:
        if access_token:
            # Probably quite expensive to fetch all playlists on every click
            # TODO: Handle caching using background callbacks
            # TODO: Delay for 1 second to avoid rate limiting
            playlists = msplay.fetch_all_playlists(access_token)
            return [
                [
                    home_components.single_playlist_template(playlist)
                    for playlist in playlists
                ]
            ]
    return [[]]


@callback(
    Output("playlist-container", "children", allow_duplicate=True),
    Output("playlist-container", "span", allow_duplicate=True),
    Input("toggle-menu-btn", "checked"),
    Input("access-token", "data"),
    prevent_initial_call=True,
)
def toggle_playlist_container(checked, access_token):
    if access_token is None:
        raise PreventUpdate
    if checked:
        return home_components.generate_playlists_menu(), 4
    return [], 0


@callback(
    Output("playlist-container", "children", allow_duplicate=True),
    Output("playlist-container", "span", allow_duplicate=True),
    Input({"type": "goto-playlist-btn", "index": ALL}, "n_clicks"),
    Input("access-token", "data"),
    prevent_initial_call=True,
)
def display_points_menu(n_clicks, access_token):
    if access_token is None or sum(filter(None, n_clicks)) == 0:
        raise PreventUpdate
    if n_clicks:
        index_clicked = ctx.triggered_id["index"]
        return home_components.generate_points_menu(index_clicked), 4
    return [], 0


@callback(
    Output("playlist-container", "children", allow_duplicate=True),
    Output("playlist-container", "span", allow_duplicate=True),
    Input({"type": "delete-playlist-btn", "index": ALL}, "n_clicks"),
    Input("access-token", "data"),
    prevent_initial_call=True,
)
def delete_playlist_btn(n_clicks, access_token):
    if access_token is None or sum(filter(None, n_clicks)) == 0:
        raise PreventUpdate
    if n_clicks:
        if msplay.remove_playlist_by_id(ctx.triggered_id["index"], access_token):
            return home_components.generate_playlists_menu(), 4
    return no_update, no_update


@callback(
    Output("playlist-container", "children", allow_duplicate=True),
    Output("playlist-container", "span", allow_duplicate=True),
    Input({"type": "close-playlist-btn", "index": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def previous_btn_clicked(n_clicks):
    if sum(filter(None, n_clicks)) == 0:
        raise PreventUpdate
    return home_components.generate_playlists_menu(), 4


@callback(
    Output("access-token", "data", allow_duplicate=True),
    Output("refresh-token", "data", allow_duplicate=True),
    Input("sign-out-btn", "n_clicks"),
    prevent_initial_call=True,
)
def disconnect_user(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    return None, None


@callback(
    Output("add-playlist-modal", "opened"),
    Input("add-playlist-btn", "n_clicks"),
    Input("close-playlist-modal-btn", "n_clicks"),
    State("add-playlist-modal", "opened"),
    prevent_initial_call=True,
)
def toggle_playlist_modal(n_add, n_close, opened):
    return not opened


@callback(
    Output("url", "href", allow_duplicate=True),
    Output("playlist-name-modal-input", "error"),
    Input("submit-playlist-modal-btn", "n_clicks"),
    State("add-playlist-modal", "opened"),
    State("playlist-name-modal-input", "value"),
    State("access-token", "data"),
    State("username", "data"),
    prevent_initial_call=True,
)
def submit_playlist_modal(n_submit, opened, playlist_name, access_token, username):
    if n_submit:
        if playlist_name:
            if msplay.create_playlist(
                playlist_name, "lorem ipsum", username, access_token
            ):
                return "/", no_update
        return no_update, "Please enter a playlist name"
    return no_update, no_update
