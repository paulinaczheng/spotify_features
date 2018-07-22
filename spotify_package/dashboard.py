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
        options=list_of_artists_for_dropdown(), value='all_artists'),
html.H1('Artist Features Plot'),
html.Div(id='plot-container')])

def generate_plot(plot_data):
    return dcc.Graph(id = 'artist_features',
    figure = {
    'data': plot_data,
    'layout': {'title' :  'Artist Features', 'updatemenus': updatemenus}})

# def generate_table(table_data):
#     return html.Table(id='artist-avg-table', children=
#         # create table headers (the first table row)
#         [html.Tr(id='headers', children=[html.Th(feature) for feature in table_data.keys()]
#         # combine the table headers and table data lists into one list
#         +
#         # create more table rows containing table cells with all our data
#         [html.Tr(id='row-data', children=[
#             html.Td(table_data[k]) for k in table_data.keys()
#         ])])])

@app.callback(
    Output(component_id='plot-container', component_property='children'),
    [Input(component_id='select-artist', component_property='value')])
def filter_plot(input_value):
    global data
    # if input_value == 'all_artists':
    #     data = []
    #     for artist in [artist.name for artist in Artist.query.all()]:
    #         trace_list = list_of_traces(artist)
    #         top_tracks = tempo_normalization_list(trace_list[0])
    #         oth_tracks = tempo_normalization_list(trace_list[1])
    #         data.extend(top_tracks)
    #         data.extend(oth_tracks)
    # else:
    trace_list = list_of_traces(input_value)
    top_tracks = tempo_normalization_list(trace_list[0])
    oth_tracks = tempo_normalization_list(trace_list[1])
    data = top_tracks + oth_tracks
    return generate_plot(data)

# @app.callback(
#     Output(component_id='container', component_property='children'),
#     [Input(component_id='select-artist', component_property='value')])
# def filter_table(input_value):
#     global tbl_fin_data
#     tbl_fin_data = avg_featurevalues_artist(input_value)
#     return generate_table(tbl_fin_data)
