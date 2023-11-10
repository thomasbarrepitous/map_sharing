import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html
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

# Buttons for a selected playlist
inside_playlist_buttons_layout = dmc.Grid(
    [
        dmc.Col(
            dmc.Button(
                "Add to Playlist",
                leftIcon=DashIconify(icon="mdi:plus", width=20),
                variant="gradient",
                gradient={"from": "teal", "to": "lime", "deg": 105},
                fullWidth=True,
            ),
            span=6,
        ),
        dmc.Col(
            dmc.Button(
                "Delete Playlist",
                leftIcon=DashIconify(icon="mdi:bin", width=20),
                color="red",
                fullWidth=True,
            ),
            span=6,
        ),
    ]
)

# Buttons on top of the playlist layout when no playlist is selected
outside_playlist_buttons_layout = dmc.Grid(
    [
        dmc.Col(
            dmc.Button(
                "New Playlist",
                leftIcon=DashIconify(icon="material-symbols:add", width=20),
                variant="gradient",
                gradient={"from": "teal", "to": "lime", "deg": 105},
                fullWidth=True,
            ),
            span="auto",
        ),
        # dmc.Col(
        #     dmc.Button(
        #         "Hide Menu",
        #         leftIcon=DashIconify(icon="mdi:hide", width=20),
        #         color="gray",
        #         fullWidth=True,
        #     ),
        #     span=6,
        # ),
    ]
)


def single_geocode_template(point: dict):
    return dmc.AccordionItem(
        [
            dmc.AccordionControl(point["title"]),
            dmc.AccordionPanel(
                point["description"],
            ),
        ],
    )


def single_playlist_template(playlist: dict):
    return dmc.AccordionItem(
        [
            dmc.AccordionControl(playlist["title"]),
            dmc.AccordionPanel(
                playlist["description"],
            ),
        ],
        value=f'{playlist["id"]}',
    )


# Base layout for the playlist container
def generate_playlists_menu(playlists: list):
    return dmc.Grid(
        [
            dmc.Col(outside_playlist_buttons_layout, span=12),
            dmc.Col(
                dmc.Accordion(
                    [single_playlist_template(playlist) for playlist in playlists]
                )
            ),
        ]
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
                                dmc.ActionIcon(
                                    DashIconify(icon="mdi:hide", width=20),
                                    size="lg",
                                    variant="filled",
                                    id="hide-menu-btn",
                                    mb=10,
                                    n_clicks=0,
                                ),
                                id="hide-menu-btn-container",
                                span="content",
                            ),
                        ],
                        id="search-container",
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
