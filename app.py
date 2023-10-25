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
                dmc.Center(
                    dcc.Graph(id="map", style={"height": "80vh", "width": "100%"})
                ),
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
            return [
                {"value": result["place_id"], "label": result["description"]}
                for result in search_results
            ]
        except Exception as e:
            print("ERROR : ", e)
    return []


@app.callback(
    Output("map", "figure"),
    [Input("select", "value")],
)
def update_map(select_value):
    if select_value:
        try:
            geocode_result = gmaps.geocode(place_id=select_value)
            geocode_lon = geocode_result[0]["geometry"]["location"]["lng"]
            geocode_lat = geocode_result[0]["geometry"]["location"]["lat"]
            # Create a map using the fetched data
            fig = px.scatter_geo(
                lon=[geocode_lon],
                lat=[geocode_lat],
                # center={"lat": geocode_lat, "lon": geocode_lon},
                projection="orthographic",
                scope="world",
            )
            fig.update_layout(
                geo=dict(
                    projection_scale=10,
                    fitbounds="locations",
                    center=dict(
                        lat=geocode_lat,
                        lon=geocode_lon,
                    ),
                    showland=True,
                    landcolor="rgb(212, 212, 212)",
                    subunitcolor="rgb(255, 255, 255)",
                    countrycolor="rgb(255, 255, 255)",
                    showlakes=True,
                    lakecolor="rgb(255, 255, 255)",
                    showsubunits=True,
                    showcountries=True,
                    resolution=50,
                )
            )
            return fig
        except Exception as e:
            print("ERROR : ", e)
    fig = px.scatter_geo(lon=[], lat=[], projection="orthographic")
    fig.update_layout(
        geo=dict(
            projection_scale=10,
            fitbounds="locations",
            showland=True,
            landcolor="rgb(212, 212, 212)",
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)",
            showlakes=True,
            lakecolor="rgb(255, 255, 255)",
            showsubunits=True,
            showcountries=True,
            resolution=50,
        )
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
