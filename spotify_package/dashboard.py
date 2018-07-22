import dash_core_components as dcc
import dash_html_components as html
from spotify_package import app
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotify_package.charts import *
import json
import dash
from dash.dependencies import Input, Output

app.layout = html.Div(children= [
 dcc.Dropdown(
        id='select-artist',
        options=list_of_artists_for_dropdown(), value='Artist'),
html.H1('Artist Features Plot'),
html.Div(id='plot-container')])

def generate_plot(plot_data):
    return dcc.Graph(id = 'artist_features',
    figure = {
    'data': plot_data,
    'layout': {'title' :  'Artist Features', 'updatemenus': updatemenus}})

@app.callback(
    Output(component_id='plot-container', component_property='children'),
    [Input(component_id='select-artist', component_property='value')])
def filter_plot(input_value):
    global data
    trace_list = list_of_traces(input_value)
    top_tracks = tempo_normalization_list(trace_list[0])
    oth_tracks = tempo_normalization_list(trace_list[1])
    data = top_tracks + oth_tracks
    return generate_plot(data)
