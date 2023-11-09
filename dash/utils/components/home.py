import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html
import dash_leaflet as dl


####################
#### HEADERS #######
####################

login_area_signed_in = dmc.Grid(
    [
        dmc.Col(html.P("Hello User"), span=5),
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
signed_in_header = dmc.Container(
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
                            login_area_signed_in,
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
            span=6,
        ),
        dmc.Col(
            dmc.Button(
                "Hide Menu",
                leftIcon=DashIconify(icon="mdi:hide", width=20),
                color="gray",
                fullWidth=True,
            ),
            span=6,
        ),
    ]
)

# Base layout for the playlist container
playlist_layout = dmc.Grid(
    [
        dmc.Col(outside_playlist_buttons_layout, span=12),
        dmc.Col(
            dmc.Accordion(
                children=[
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl("Customization"),
                            dmc.AccordionPanel(
                                "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                            ),
                        ],
                        value="customization",
                    ),
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl("Flexibility"),
                            dmc.AccordionPanel(
                                "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
                                "component styles "
                            ),
                        ],
                        value="flexibility",
                    ),
                ],
                id="playlist-accordion",
            )
        ),
    ]
)


####################
#### LAYOUTS #######
####################

# Layout for signed in users
signed_in_layout = html.Div(
    children=[
        signed_in_header,
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
                            span=8,
                        ),
                        dmc.Col(
                            playlist_layout,
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
