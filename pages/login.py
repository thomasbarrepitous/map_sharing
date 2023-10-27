import dash
from dash import html
import time
import dash_mantine_components as dmc
from dash import html, Output, Input, no_update, callback
from dash_iconify import DashIconify

# Custom modules
from utils import mapsharing_login as mslogin

dash.register_page(__name__, path="/login")

login_component = (
    dmc.LoadingOverlay(
        dmc.Stack(
            id="loading-form",
            children=[
                dmc.TextInput(
                    label="Username",
                    placeholder="Your username",
                    icon=DashIconify(icon="radix-icons:person"),
                ),
                dmc.TextInput(
                    label="Password",
                    type="password",
                    placeholder="Your password",
                    icon=DashIconify(icon="radix-icons:lock-closed"),
                ),
                # dmc.Checkbox(
                #     label="Remember me",
                #     checked=True,
                # ),
                dmc.Button(
                    "Login", id="load-button", variant="outline", fullWidth=True
                ),
            ],
        )
    ),
)


layout = html.Div(
    # style={"width": 200},
    children=dmc.Container(
        dmc.Center(
            login_component,
            style={"height": "100vh"},
        ),
        style={"height": "100vh"},
    ),
    style={"height": "100vh"},
)


@callback(
    Output("loading-form", "children"),
    Input("load-button", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    mslogin.login("", "")
    return no_update
