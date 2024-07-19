import dash
from dash import Dash, html, dcc, Output, Input, callback, no_update
import crystal_toolkit.components as ctc
import dash_mp_components as dmc

app = Dash(__name__, use_pages=True, pages_folder="pages", suppress_callback_exceptions=True)

app.layout = html.Div([
    dmc.Navbar(
        id = "dmc_navbar",
        className = "is-dark",
        brandItem = {"label": "The Materials Project", 
                     "href": "/",
                     "image": "assets/images/brand.png"
                     },
        items = [
            {"label": "API", "href": "/api"},
            {"label": "Materials", "href": "/materials"},
            {"label": "Apps", "isRight": True, "items":[
                {"label": "Materials", "href": "/materials"},
                {"label": "API", "href": "/api"},
            ]}
        ]
      ),
    dcc.Location(id='url'),
    dash.page_container,
])

if __name__ == '__main__':
    for page in dash.page_registry.values():
        print(page['path'])
    app.run(debug=True, port=8080)