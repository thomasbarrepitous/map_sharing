import dash
from dash import Dash, dcc, callback, html, Output, Input, State
from utils import mapsharing_login as mslogin
import jwt

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap",
    ],
    use_pages=True,
)


app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=True),
        dcc.Store(id="access-token", storage_type="local", data=None),
        dcc.Store(id="refresh-token", storage_type="local", data=None),
        dcc.Store(id="username", storage_type="local", data=None),
        dash.page_container,
    ]
)


@callback(
    Output("access-token", "data", allow_duplicate=True),
    Output("refresh-token", "data", allow_duplicate=True),
    State("access-token", "data"),
    Input("refresh-token", "data"),
    prevent_initial_call=True,
)
def refresh_acces_token(
    access_token,
    refresh_token,
):
    # If tokens are set
    if access_token and refresh_token:
        # If access token is expired
        try:
            mslogin.decode_jwt(access_token)
        except jwt.exceptions.ExpiredSignatureError:
            # Refresh access token
            new_access_token = mslogin.refresh_jwt(refresh_token)
            # If refresh failed
            if new_access_token is None:
                return None, None
            return new_access_token, refresh_token
    return access_token, refresh_token


@callback(
    Output("username", "data"),
    Input("access-token", "data"),
)
def set_username(access_token):
    if access_token is None:
        return None
    try:
        decoded_token = mslogin.decode_jwt(access_token)
        username = decoded_token.get("username")
    except (
        jwt.exceptions.ExpiredSignatureError,
        jwt.exceptions.DecodeError,
        AttributeError,
    ):
        return None
    return username


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
