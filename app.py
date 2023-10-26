import dash
from dash import Dash, Output, Input, State, html

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
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
