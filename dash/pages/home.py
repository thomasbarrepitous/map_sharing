import dash
from dash import callback, Output, Input, State, html, dcc
import dash_mantine_components as dmc
import googlemaps
import os
import uuid
import dash_leaflet as dl
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate

dash.register_page(__name__, path="/")


# API Auth
gmaps = googlemaps.Client(key=os.environ.get("GCP_KEY"))
session_token = uuid.uuid4().hex


login_area_signed_out = dmc.Grid(
    dmc.Col(
        dmc.Anchor(
            dmc.Button(
                "Login",
                leftIcon=DashIconify(icon="carbon:settings-check", width=20),
            ),
            href="/login",
        ),
        span="content",
    ),
    justify="center",
    align="center",
)

login_area_signed_in = dmc.Grid(
    [
        dmc.Col(html.P("Hello User"), span=5),
        dmc.Col(
            dmc.Anchor(
                dmc.Button(
                    "Sign out",
                    leftIcon=DashIconify(icon="pepicons-pop:leave", width=20),
                    id="sign-out-btn",
                ),
                href="/login",
            ),
            span=7,
        ),
    ],
    align="center",
    justify="center",
)

layout = html.Div(
    [
        dmc.Container(
            [
                dmc.Header(
                    height=60,
                    children=[
                        dmc.Grid(
                            [
                                dmc.Col(span="auto"),
                                dmc.Col(
                                    dmc.Center(
                                        dmc.Group(
                                            [
                                                dmc.Image(
                                                    src="/assets/logo.png",
                                                    width=40,
                                                    height=40,
                                                ),
                                                dmc.Text(
                                                    "Map Sharing",
                                                    style={
                                                        "font-family": "Tahoma, Geneva, sans-serif",
                                                        "font-size": "23px",
                                                        "letter-spacing": "0px",
                                                        "word-spacing": "-3px",
                                                        "color": "#1B8CFF",
                                                        "font-weight": "700",
                                                        "text-decoration": "none",
                                                        "font-style": "normal",
                                                        "font-variant": "small-caps",
                                                        "text-transform": "none",
                                                    },
                                                ),
                                            ],
                                            position="apart",
                                        )
                                    ),
                                    span=6,
                                ),
                                dmc.Col(
                                    id="login-area",
                                    span="auto",
                                ),
                            ],
                            align="center",
                            justify="flex-end",
                        ),
                    ],
                    style={"backgroundColor": "white"},
                )
            ],
            style={"marginTop": 20, "marginbottom": 20},
        ),
        dmc.Container(
            [
                dmc.Select(
                    data=[],
                    value="",
                    clearable=True,
                    nothingFound="No results found",
                    searchable=True,
                    id="select",
                ),
            ],
            style={"marginTop": 20, "marginbottom": 20},
        ),
        dmc.Container(
            [
                html.Div(
                    dl.Map(
                        [
                            dl.TileLayer(),
                        ],
                        center=[40, 15],
                        zoom=2,
                        id="map",
                        style={"height": "50vh", "z-index": 0, "tabindex": -2},
                    ),
                    id="map-container",
                ),
            ],
            style={"marginTop": 20, "marginbottom": 20},
        ),
    ]
)


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


@callback(Output("login-area", "children"), Input("access-token", "data"))
def authenticated_layout_handler(access_token):
    if access_token is not None:
        return login_area_signed_in
    return login_area_signed_out


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
