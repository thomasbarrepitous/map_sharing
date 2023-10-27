import dash
from dash import html
import dash_mantine_components as dmc
from dash import html, Output, Input, State, no_update, callback
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
                    id="username-input",
                ),
                dmc.TextInput(
                    label="Password",
                    type="password",
                    placeholder="Your password",
                    icon=DashIconify(icon="radix-icons:lock-closed"),
                    id="password-input",
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
    children=[
        dmc.Container(
            [
                dmc.Anchor(
                    dmc.Button(
                        "Previous",
                        leftIcon=DashIconify(icon="uil:previous", width=20),
                    ),
                    href="/",
                ),
                dmc.Center(
                    login_component,
                    style={"height": "75vh"},
                ),
            ],
            style={"height": "100vh"},
        ),
    ],
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


@callback(
    Output("username-input", "error"),
    Output("password-input", "error"),
    Input("load-button", "n_clicks"),
    State("username-input", "value"),
    State("password-input", "value"),
    prevent_initial_call=True,
)
def validate_login(n_clicks, username, password):
    print(bool(username))
    print(username)
    return (
        "Username cannot be empty." if not bool(username) else False,
        "Password cannot be empty." if not bool(password) else False,
    )
