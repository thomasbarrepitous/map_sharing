import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html, ALL
import dash_leaflet as dl

####################
#### HEADERS #######
####################


def display_logout_area(username: str):
    return dmc.Grid(
        [
            dmc.Col(html.P(f"Hello {username}"), span=5),
            dmc.Col(
                dmc.Anchor(
                    dmc.Button(
                        "Sign out",
                        leftIcon=DashIconify(icon="pepicons-pop:leave", width=20),
                        id="sign-out-btn",
                        color="red",
                    ),
                    href="/login",
                ),
                span=7,
            ),
        ],
        align="center",
        justify="center",
    )


# Header for signed out users
signed_out_header = dmc.Container(
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
                            dmc.Grid(
                                dmc.Col(
                                    dmc.Anchor(
                                        dmc.Button(
                                            "Login",
                                            leftIcon=DashIconify(
                                                icon="carbon:settings-check", width=20
                                            ),
                                        ),
                                        href="/login",
                                    ),
                                    span="content",
                                ),
                                justify="center",
                                align="center",
                            ),
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
)


# Header for signed in users
def display_signed_in_header(username: str):
    return dmc.Container(
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
                                display_logout_area(username),
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
    )


####################
#### PLAYLISTS #####
####################

add_playlist_btn = dmc.Button(
    "New Playlist",
    leftIcon=DashIconify(icon="material-symbols:add", width=20),
    variant="gradient",
    gradient={"from": "teal", "to": "lime", "deg": 105},
    fullWidth=True,
    id="add-playlist-btn",
)


def add_current_point(playlist_id: int):
    return dmc.Button(
        "Add Current Address",
        leftIcon=DashIconify(icon="material-symbols:add", width=20),
        variant="gradient",
        gradient={"from": "teal", "to": "lime", "deg": 105},
        fullWidth=True,
        id={"id": "add-current-point-btn", "index": playlist_id},
    )


def add_point_btn(playlist_id: int):
    return dmc.Button(
        "New Address",
        leftIcon=DashIconify(icon="material-symbols:add", width=20),
        variant="gradient",
        gradient={"from": "indigo", "to": "cyan", "deg": 105},
        fullWidth=True,
        id={"id": "add-point-btn", "index": playlist_id},
    )


def add_point_modal(playlist_id: int):
    return dmc.Modal(
        title="Add a new point in your playlist !",
        id={"id": "add-point-modal", "index": playlist_id},
        centered=True,
        zIndex=10000,
        children=[
            dmc.Center(
                dmc.TextInput(
                    label="Point name:",
                    id="point-name-modal-input",
                    style={"width": 200},
                ),
            ),
            dmc.Center(
                dmc.TextInput(
                    label="Address:",
                    id="address-modal-input",
                    style={"width": 200},
                ),
            ),
            dmc.Center(
                dmc.TextInput(
                    label="Description:",
                    id="description-modal-input",
                    style={"width": 200},
                ),
            ),
            dmc.Center(
                dmc.TextInput(
                    label="Latitude:",
                    id="latitude-modal-input",
                    style={"width": 200},
                ),
            ),
            dmc.Center(
                dmc.TextInput(
                    label="Longitude:",
                    id="longitude-modal-input",
                    style={"width": 200},
                ),
            ),
            dmc.Space(h=30),
            dmc.Group(
                [
                    dmc.Button(
                        "Submit",
                        variant="gradient",
                        gradient={"from": "teal", "to": "lime", "deg": 105},
                        id="submit-point-modal-btn",
                    ),
                    dmc.Button(
                        "Close",
                        color="red",
                        # variant="outline",
                        id="close-point-modal-btn",
                    ),
                ],
                position="right",
            ),
        ],
    )


add_playlist_modal = dmc.Modal(
    title="Add a new playlist",
    id="add-playlist-modal",
    centered=True,
    zIndex=10000,
    children=[
        dmc.Center(
            dmc.TextInput(
                label="Playlist name:",
                id="playlist-name-modal-input",
                style={"width": 200},
            ),
        ),
        dmc.Space(h=30),
        dmc.Group(
            [
                dmc.Button(
                    "Submit",
                    variant="gradient",
                    gradient={"from": "teal", "to": "lime", "deg": 105},
                    id="submit-playlist-modal-btn",
                ),
                dmc.Button(
                    "Close",
                    color="red",
                    # variant="outline",
                    id="close-playlist-modal-btn",
                ),
            ],
            position="right",
        ),
    ],
)


# Buttons for a selected playlist
def inside_playlist_buttons_layout(index_clicked):
    return dmc.Grid(
        [
            dmc.Col(
                dmc.Button(
                    "Previous",
                    leftIcon=DashIconify(icon="uil:previous", width=20),
                    variant="gradient",
                    gradient={"from": "indigo", "to": "cyan"},
                    fullWidth=True,
                    id={"type": "close-playlist-btn", "index": 1},
                ),
                span=6,
            ),
            dmc.Col(
                dmc.Button(
                    "Delete",
                    leftIcon=DashIconify(icon="mdi:bin", width=20),
                    color="red",
                    fullWidth=True,
                    id={"type": "delete-playlist-btn", "index": index_clicked},
                ),
                span=6,
            ),
        ]
    )


# Buttons on top of the playlist layout when no playlist is selected
outside_playlist_buttons_layout = dmc.Grid(
    [
        dmc.Col(
            add_playlist_btn,
            span="auto",
        ),
        add_playlist_modal,
    ]
)


def single_playlist_template(playlist: dict):
    return dmc.AccordionItem(
        [
            dmc.AccordionControl(
                [
                    dmc.Grid(
                        [
                            dmc.Col(playlist["title"], span="auto"),
                            dmc.Col(
                                dmc.ActionIcon(
                                    DashIconify(icon="icon-park:go-end"),
                                    size="lg",
                                    variant="gradient",
                                    id={
                                        "type": "goto-playlist-btn",
                                        "index": playlist["id"],
                                    },
                                    gradient={"from": "teal", "to": "lime", "deg": 105},
                                ),
                                span="content",
                            ),
                        ],
                        align="center",
                    )
                ]
            ),
        ],
        value=f'{playlist["id"]}',
    )


# Base layout for the playlist menu container
def generate_playlists_menu():
    return dmc.Grid(
        [
            dmc.Col(
                dmc.Center(
                    dmc.Text(
                        "Playlists",
                        weight=700,
                        underline=True,
                        variant="gradient",
                        gradient={"from": "teal", "to": "lime", "deg": 105},
                    )
                ),
                span=12,
            ),
            dmc.Col(
                dmc.Accordion(
                    id={"type": "playlists-menu-accordion", "index": 0},
                    variant="contained",
                    chevronSize=0,
                    disableChevronRotation=True,
                )
            ),
            dmc.Col(outside_playlist_buttons_layout, span=12),
        ],
        style={"border": "1px solid #e0e0e0", "border-radius": 5},
    )


# Template for a single geocode point
def single_geocode_template(point: dict):
    return dmc.AccordionItem(
        [
            dmc.AccordionControl(
                dmc.Grid(
                    [
                        dmc.Col(
                            dmc.Center(
                                dmc.Text(
                                    point["address"],
                                    weight=700,
                                    underline=True,
                                    variant="gradient",
                                    gradient={"from": "indigo", "to": "cyan"},
                                )
                            ),
                            span=12,
                        ),
                        dmc.Col(f'Latitude : {point["latitude"]}', span=12),
                        dmc.Col(f'Longitude : {point["longitude"]}', span=12),
                    ],
                    justify="center",
                )
            )
        ],
        value="test",
    )


# Base layout for the geococde point menu container
def generate_points_menu(index_clicked: int):
    return dmc.Grid(
        [
            dmc.Col(inside_playlist_buttons_layout(index_clicked), span=12),
            dmc.Col(
                dmc.Accordion(
                    id={"type": "points-menu-accordion", "index": index_clicked},
                    variant="contained",
                    chevronSize=0,
                    disableChevronRotation=True,
                )
            ),
            dmc.Col(
                dmc.Stack(
                    [
                        add_point_btn(index_clicked),
                        add_current_point(index_clicked),
                    ],
                    spacing="xs",
                ),
                span=12,
            ),
            add_point_modal(index_clicked),
        ],
        style={"border": "1px solid #e0e0e0", "border-radius": 5},
    )


####################
#### LAYOUTS #######
####################


# Layout for signed in users
def display_signed_in_layout(username: str):
    return html.Div(
        children=[
            display_signed_in_header(username),
            dmc.Container(
                [
                    dmc.Grid(
                        [
                            dmc.Col(
                                dmc.Select(
                                    data=[],
                                    value="",
                                    clearable=True,
                                    nothingFound="No results found",
                                    searchable=True,
                                    id="select",
                                ),
                                span="auto",
                            ),
                            dmc.Col(
                                dmc.Switch(
                                    offLabel=DashIconify(icon="mdi:hide", width=20),
                                    onLabel=DashIconify(icon="mdi:menu", width=20),
                                    size="lg",
                                    checked=True,
                                    id="toggle-menu-btn",
                                ),
                                id="toggle-menu-btn-container",
                                span="content",
                            ),
                        ],
                        id="search-container",
                        align="center",
                    )
                ],
                style={"marginTop": 20, "marginbottom": 20},
            ),
            dmc.Container(
                [
                    dmc.Grid(
                        [
                            dmc.Col(
                                html.Div(
                                    dl.Map(
                                        [
                                            dl.TileLayer(),
                                        ],
                                        center=[40, 15],
                                        trackViewport=True,
                                        zoom=2,
                                        id="map",
                                        style={
                                            "height": "75vh",
                                            "z-index": 0,
                                            "tabindex": -2,
                                        },
                                    ),
                                    id="map-container",
                                ),
                                span="auto",
                            ),
                            dmc.Col(
                                generate_playlists_menu(),
                                id="playlist-container",
                                span=4,
                            ),
                        ]
                    )
                ],
                style={"marginTop": 20, "marginbottom": 20},
            ),
        ]
    )


# Layout for signed out users
signed_out_layout = html.Div(
    [
        signed_out_header,
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
                        style={"height": "75vh", "z-index": 0, "tabindex": -2},
                    ),
                    id="map-container",
                ),
            ],
            style={"marginTop": 20, "marginbottom": 20},
        ),
    ]
)

if __name__ == "__main__":
    print("This is a module for the Map Sharing app")
