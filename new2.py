from dash import dcc, html

def create_layout(df):
    id_camion = df["id_camion"].unique()[0]
    id_conducteur = df["id_conducteur"].unique()[0]

    return html.Div([
        html.H1(
            f"Télémétrie du Camion {id_camion}",
            style={"textAlign": "center", "marginTop": "20px"}
        ),

        html.Div([
            html.Div([
                html.H3("Informations"),
                html.P(f"Camion: {id_camion}"),
                html.P(f"Conducteur: {id_conducteur}"),
                html.P(f"Enregistrements: {len(df)}"),
                html.Hr(),
                html.Label("Vitesse minimale (km/h):"),
                dcc.Slider(
                    id="speed_filter",
                    min=0, max=120, step=5, value=0,
                    marks={i: str(i) for i in range(0, 121, 20)}
                ),
                html.Br(),
                html.Label("Efficacité minimale:"),
                dcc.Slider(
                    id="eff_filter",
                    min=0, max=1, step=0.05, value=0,
                    marks={0: "0", 0.5: "0.5", 1: "1"}
                ),
            ], className="sidebar"),

            html.Div([
                dcc.Graph(id="map_animation", style={"height": "85vh"})
            ], className="content")
        ], className="container")
    ])