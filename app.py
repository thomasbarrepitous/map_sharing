from dash import Dash, Output, Input, State, dcc, html
import plotly.express as px
import dash_mantine_components as dmc
import googlemaps
import os
import uuid

app = Dash(
    __name__,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

# API Auth
gmaps = googlemaps.Client(key=os.environ.get("GCP_KEY"))
session_token = uuid.uuid4().hex

app.layout = html.Div(
    [
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
                dmc.Center(dcc.Graph(id="map")),
            ]
        )
    ]
)


@app.callback(
    Output("select", "data"),
    [Input("select", "searchValue")],
    prevent_initial_call=True,
)
def update_select(search_query):
    if search_query:
        try:
            # Fetch data from the API
            search_results = gmaps.places_autocomplete(
                session_token=session_token, input_text=search_query
            )
            # Create a map using the fetched data
            return [result["description"] for result in search_results]
        except Exception as e:
            print("ERROR : ", e)
            return []
    return []


@app.callback(
    Output("map", "figure"),
    [Input("select", "value")],
)
def update_map(select_value):
    try:
        # Create a map using the fetched data
        fig = px.scatter_geo(lon=[0], lat=[0])
        return fig
    except Exception as e:
        print("ERROR : ", e)
        return px.scatter_geo(lon=[0], lat=[0])


if __name__ == "__main__":
    app.run_server(debug=True)
