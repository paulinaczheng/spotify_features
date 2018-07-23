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

# app.layout = html.Div(children= [
# # dcc.Dropdown(
# # id='select-plot',
# # options=
# # [{'label': 'Average Feature Values', 'value': 'bar'},
# # {'label': 'Track Features by Artist', 'value': 'scatter'}],
# # placeholder='Select a plot',
# # ),

# html.H1('Artist Features Plot'),
# html.Div(id='plot-container')])

app.layout = html.Div(children= [html.H1('Artist Features Plot'),dcc.Graph(
       id='example-graph',
       figure={
           'data': all_bars(),
           'layout': {
               'title': 'Average Feature Values'}}),
dcc.Dropdown(
           id='select-artist',
           options=list_of_artists_for_dropdown(),
           placeholder="Select an artist", value ='Artist'
       ),
html.Div(id= 'plot-container'),])

def generate_scatter(scatter_data):
    return dcc.Graph(id = 'artist_features',
    figure = {
    'data': scatter_data,
    'layout': {'title' :  'Artist Tracks by Feature', 'updatemenus': updatemenus}})

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

# @app.callback(
#     Output(component_id='plot-container', component_property='children'),
#     [Input(component_id='select-artist', component_property='value')])
# def filter_bar(input_value):
#     global final_bar_data
#     feature_values = avg_featurevalues_artist(input_value)
#     x = [feature for feature in feature_values.keys()]
#     y = [avg for avg in feature_values.values()]
#     title = 'Feature Averages for ' + input_value
#     final_bar_data = {'name': title, 'x': x, 'y': y, 'type': 'bar'}
#     return generate_bar(final_bar_data)
    # return final_bar_data

@app.callback(Output(component_id = 'plot-container', component_property ='children'),
[Input(component_id = 'select-artist',component_property = 'value' )]
)
def filter_scatter(input_value):
    global scatter_data
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
    scatter_data = top_tracks + oth_tracks
    return generate_scatter(scatter_data)

# @app.callback(
#     Output(component_id='container', component_property='children'),
#     [Input(component_id='select-artist', component_property='value')])
# def filter_table(input_value):
#     global tbl_fin_data
#     tbl_fin_data = avg_featurevalues_artist(input_value)
#     return generate_table(tbl_fin_data)
#
# @app.callback(
#     Output(component_id='plot-container', component_property='children'),
#     [Input(component_id='select-plot', component_property='value'),
#     Input(component_id='select-artist', component_property='value')])
# def return_plot(plot_value, artist_value):
#     if plot_value == 'scatter':
#         return filter_scatter(artist_value)
#     elif plot_value == 'bar':
#         return filter_bar(artist_value)
