import dash
from dash import html
import dash_mantine_components as dmc
from dash import dcc, html, Output, Input, State, no_update, callback
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify
from requests import status_codes

# Custom modules
from utils import mapsharing_login as mslogin

dash.register_page(__name__, path="/login")

login_component = (
    dmc.LoadingOverlay(
        dmc.Stack(
            id="loading-form",
            children=[
                dmc.TextInput(
                    label="Email",
                    placeholder="Your email",
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
                    "Login",
                    id="login-button",
                    variant="gradient",
                    gradient={"from": "indigo", "to": "cyan"},
                    fullWidth=True,
                    type="submit",
                ),
                dmc.Anchor(
                    dmc.Button(
                        "Create an Account",
                        id="create-account-btn",
                        variant="outline",
                        fullWidth=True,
                    ),
                    href="/create-account",
                ),
            ],
        )
    ),
)


layout = html.Div(
    children=[
        dmc.Container(
            [
                dcc.Location(id="url", refresh=True),
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
    Output("username", "data"),
    Input("access-token", "data"),
)
def set_username(access_token):
    if access_token:
        return mslogin.decode_jwt(access_token).get("username")
    return None


@callback(
    Output("access-token", "data"),
    Output("refresh-token", "data"),
    # Output("loading-form", "children"),
    Output("username-input", "error"),
    Output("password-input", "error"),
    Output("url", "pathname"),
    Input("login-button", "n_clicks"),
    State("username-input", "value"),
    State("password-input", "value"),
    prevent_initial_call=True,
)
def login_button_handler(n_clicks, email, password):
    if n_clicks is None:
        raise PreventUpdate
    is_form_valid, email_feedback, password_feedback = validate_form(email, password)
    if n_clicks:
        if is_form_valid:
            access_token, refresh_token = populate_jwt(email, password)
            if access_token and refresh_token:
                return access_token, refresh_token, no_update, no_update, "/"
    return None, None, email_feedback, password_feedback, no_update


def validate_form(email, password):
    email_feedback = "Email cannot be empty." if not bool(email) else False
    password_feedback = "Password cannot be empty." if not bool(password) else False
    is_form_valid = not email_feedback and not password_feedback
    return (
        is_form_valid,
        email_feedback,
        password_feedback,
    )


def populate_jwt(username, password):
    return mslogin.login_jwt(username, password)
