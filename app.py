from dash import Dash, Output, Input, State, html
import dash_mantine_components as dmc
import googlemaps
import os
import uuid
import dash_leaflet as dl

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

container_style = {
    "marginTop": 20,
    "marginBottom": 20,
}

app.layout = html.Div(
    [
        dmc.Container(
            [
                dmc.Header(
                    height=60,
                    children=[dmc.Text("Map Sharing")],
                    style={"backgroundColor": "#9c86e2"},
                )
            ],
            style=container_style,
        ),
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
            ],
            style=container_style,
        ),
        dmc.Container(
            [
                html.Div(
                    dl.Map(
                        [dl.TileLayer()],
                        center=[40, 15],
                        zoom=2,
                        id="map",
                        style={"height": "50vh", "z-index": 0, "tabindex": -2},
                    ),
                    id="map-container",
                ),
            ],
            style=container_style,
        ),
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
            return [
                {"value": result["place_id"], "label": result["description"]}
                for result in search_results
            ]
        except Exception as e:
            print("ERROR : ", e)
    return []


@app.callback(
    Output("map", "viewport"),
    [Input("select", "value")],
    prevent_initial_call=True,
)
def update_map(select_value):
    if select_value:
        try:
            geocode_result = gmaps.geocode(place_id=select_value)
            geocode_lon = geocode_result[0]["geometry"]["location"]["lng"]
            geocode_lat = geocode_result[0]["geometry"]["location"]["lat"]
            # Create a map using the fetched data
            return dict(center=[geocode_lat, geocode_lon], zoom=11, transition="flyTo")
        except Exception as e:
            print("ERROR : ", e)
    return {}


if __name__ == "__main__":
    app.run_server(debug=True)
