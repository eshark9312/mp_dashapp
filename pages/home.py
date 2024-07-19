import dash
from dash import html, callback, Input, Output, dcc

dash.register_page(__name__, path='/')

def layout(**kwargs):
    return html.Div([
        html.H1('This is our Home page'),
        dcc.Link("Go to homepage", href="/materials"),
    ])

