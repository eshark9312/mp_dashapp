import dash
from dash import html, callback, Input, Output, dcc, State
from dash.exceptions import PreventUpdate
import requests
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import crystal_toolkit.components as ctc
from crystal_toolkit.core.plugin import CrystalToolkitPlugin
from crystal_toolkit.core.mpcomponent import MPComponent

import flask
from flask_caching import Cache

app = dash.get_app()
dash.register_page(__name__, path_template="/materials/<mp_id>")
cache = Cache(config={"CACHE_TYPE": "simple"})
cache.init_app(app.server)
ct_structure_comp = ctc.StructureMoleculeComponent()

def _get_pymatgen_str(mp_id:str):
    backend_base_url = f"http://{flask.request.host.split(':')[0]}:8000"
    # backend_base_url = "http://127.0.0.1:8000"
    # Make the API call
    response = requests.get(f"{backend_base_url}/summary/{mp_id}")
    print(f"{backend_base_url}/summary/{mp_id}")
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        pymat_structure = Structure.from_dict(data['structure'])
        return pymat_structure
    else:
        return "Error fetching API response"

def layout(mp_id:str = "", **kwargs):
    layout = html.Div([
        dcc.Input(id=f"mp_id_holder", type="hidden", value=mp_id),
        html.Div(children=[
            ct_structure_comp.title_layout(),
            ct_structure_comp.layout()]),
    ])
    layout.children += MPComponent._app_stores_dict[ct_structure_comp.id()]
    return layout

# generate callbacks for ct_components
ct_structure_comp.generate_callbacks(app = app, cache = cache)

@callback(
    Output('CTStructureMoleculeComponent', 'data'),
    Input('mp_id_holder','value'),
)
def update_output(mp_id:str):
    new_str = _get_pymatgen_str(mp_id)
    return new_str
