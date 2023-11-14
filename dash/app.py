import dash
from dash import Dash, dcc, callback, html, Output, Input
from utils import mapsharing_login as mslogin

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
        dcc.Store(id="access-token", storage_type="local", data=None),
        dcc.Store(id="refresh-token", storage_type="local", data=None),
        dcc.Store(id="username", storage_type="local", data=None),
        dash.page_container,
    ]
)


@callback(
    Output("username", "data"),
    Input("access-token", "data"),
)
def set_username(access_token):
    if access_token:
        return mslogin.decode_jwt(access_token).get("username")
    return None


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
