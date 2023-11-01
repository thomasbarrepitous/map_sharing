import dash
from dash import Dash, dcc, Output, Input, State, html

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
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
