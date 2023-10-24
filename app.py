from dash import Dash, dcc, html
import plotly.express as px
import dash_mantine_components as dmc

app = Dash(
    __name__,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)


lat, lon = [0], [0]
# Create a simple map using Plotly Express
map_fig = px.scatter_geo(lon=lon, lat=lat)

app.layout = html.Div(
    [
        dmc.Container(
            dmc.Center(dcc.Graph(figure=map_fig)),
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
