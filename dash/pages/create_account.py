import dash
from dash import html, dcc
import dash_mantine_components as dmc
from dash import html, Output, Input, State, no_update, callback
from dash_iconify import DashIconify
import re

# Custom modules
from utils import mapsharing_login as mslogin

dash.register_page(__name__, path="/create-account")


signup_form = (
    dmc.LoadingOverlay(
        dmc.Stack(
            id="loading-form",
            children=[
                dmc.TextInput(
                    label="Username",
                    required="True",
                    placeholder="Your username",
                    icon=DashIconify(icon="radix-icons:person"),
                    id="signup-username-input",
                ),
                dmc.TextInput(
                    label="Your Email",
                    required="True",
                    placeholder="Your Email",
                    icon=DashIconify(icon="ic:round-alternate-email"),
                    id="signup-email-input",
                ),
                dmc.TextInput(
                    label="Password",
                    required="True",
                    type="password",
                    placeholder="Your password",
                    icon=DashIconify(icon="radix-icons:lock-closed"),
                    id="signup-password-input",
                ),
                dmc.TextInput(
                    label="Confirm password",
                    required="True",
                    type="password",
                    placeholder="Confirm your password",
                    icon=DashIconify(icon="radix-icons:lock-closed"),
                    id="signup-confirm-password-input",
                ),
                dmc.Button(
                    "Create account",
                    id="signup-create-btn",
                    variant="gradient",
                    gradient={"from": "indigo", "to": "cyan"},
                    fullWidth=True,
                ),
            ],
        )
    ),
)


layout = html.Div(
    children=[
        dcc.Location(id="url-login"),
        dmc.Container(
            [
                dmc.Anchor(
                    dmc.Button(
                        "Previous",
                        leftIcon=DashIconify(icon="uil:previous", width=20),
                    ),
                    href="/login",
                ),
                dmc.Center(
                    signup_form,
                    style={"height": "75vh"},
                ),
            ],
            style={"height": "100vh"},
        ),
    ],
    style={"height": "100vh"},
)


def validate_username(username: str):
    return "Username cannot be empty." if not bool(username) else False


def validate_email(email: str):
    email_format = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if not bool(email):
        return "Email cannot be empty."
    if not re.match(email_format, email):
        return "Email format is not valid."
    return False


def validate_password(password: str):
    return "Password cannot be empty." if not bool(password) else False


def valide_confirm_password(password: str, confirm_password: str):
    if password != confirm_password:
        return "Passwords confirmation doesn't match."
    if not bool(confirm_password):
        return "Confirm password cannot be empty."
    return False


@callback(
    Output("signup-username-input", "error"),
    Output("signup-email-input", "error"),
    Output("signup-password-input", "error"),
    Output("signup-confirm-password-input", "error"),
    Input("signup-create-btn", "n_clicks"),
    State("signup-username-input", "value"),
    State("signup-password-input", "value"),
    State("signup-confirm-password-input", "value"),
    State("signup-email-input", "value"),
    prevent_initial_call=True,
)
def validate_login(n_clicks, username, password, confirm_password, email):
    return (
        validate_username(username),
        validate_email(email),
        validate_password(password),
        valide_confirm_password(password, confirm_password),
    )


@callback(
    Output("loading-form", "loading"),
    Output("signup-create-btn", "disabled"),
    Output("signup-create-btn", "children"),
    Output("signup-create-btn", "leftIcon"),
    Output("url-login", "pathname"),
    Input("signup-create-btn", "n_clicks"),
    State("signup-username-input", "value"),
    State("signup-password-input", "value"),
    State("signup-confirm-password-input", "value"),
    State("signup-email-input", "value"),
    prevent_initial_call=True,
)
def create_account(n_clicks, username, password, confirm_password, email):
    if n_clicks:
        if (
            not validate_username(username)
            and not validate_email(email)
            and not validate_password(password)
            and not valide_confirm_password(password, confirm_password)
        ):
            if mslogin.create_account(username, password, email):
                return (
                    False,
                    True,
                    "Account created successfully",
                    DashIconify(icon="uil:check"),
                    "/",
                )
            else:
                return (
                    False,
                    False,
                    "An error occured while creating your account",
                    DashIconify(icon="uil:warning"),
                    no_update,
                )
        return False, False, "Create account", DashIconify(icon="uil:next"), no_update
    return False, False, "Create account", DashIconify(icon="uil:next"), no_update
