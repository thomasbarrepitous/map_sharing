import dash
from dash import callback, Output, Input, State, html, dcc
import googlemaps
import os
import uuid
import dash_leaflet as dl
from dash.exceptions import PreventUpdate
import utils.components.home as home_components
import utils.mapsharing_playlists as msp
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dash.register_page(__name__, path="/")


# API Auth
gmaps = googlemaps.Client(key=os.environ.get("GCP_KEY"))
session_token = uuid.uuid4().hex


# Layout

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
    Output("playlist-container", "children"),
    Output("playlist-container", "span"),
    Input("hide-menu-btn", "n_clicks"),
    Input("access-token", "data"),
)
def update_playlist_container(n_clicks, access_token):
    print(n_clicks, flush=True)
    if n_clicks is None:
        raise PreventUpdate
    if n_clicks % 2 == 0:
        if access_token:
            # Probably quite expensive to fetch all playlists on every click
            # TODO: Handle caching using background callbacks
            # TODO: Delay for 1 second to avoid rate limiting
            playlists = msp.fetch_all_playlists(access_token)
            return home_components.generate_playlists_menu(playlists), 4
    return [], 0


@callback(
    Output("hide-menu-btn-container", "children"),
    Input("hide-menu-btn", "n_clicks"),
)
def toggle_hide_menu_btn(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    if n_clicks % 2 == 0:
        return dmc.ActionIcon(
            DashIconify(icon="mdi:hide", width=20),
            size="lg",
            variant="filled",
            color="gray",
            id="hide-menu-btn",
            mb=10,
            n_clicks=n_clicks,
        )
    return dmc.ActionIcon(
        DashIconify(icon="mdi:menu", width=20),
        size="lg",
        variant="filled",
        color="lime",
        id="hide-menu-btn",
        mb=10,
        n_clicks=n_clicks,
    )


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
