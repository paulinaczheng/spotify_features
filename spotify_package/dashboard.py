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

app.layout = html.Div([
    html.H1('Spotify Feature Analysis', style={
            'textAlign': 'center', 'margin': '48px 0', 'fontFamily': 'Sans-Serif'}),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Average Feature Values', children=[
            html.Div([
dcc.Graph(
       id='example-graph',
       figure={
           'data': all_bars(),
           'layout': {
               'title': 'Average Feature Values by Artist'}})
            ])
        ]),
        dcc.Tab(label='Track Values by Feature', children=[
            html.Div([
dcc.Dropdown(
           id='select-artist',
           options=list_of_artists_for_dropdown(),
           placeholder="Select an artist", value ='Artist'
       ),
html.Div(id= 'plot-container')
            ])
        ]),
        dcc.Tab(label='Artists Comparison', children=[
            html.Div([
    dcc.Graph(
       id='generation',
       figure={
           'data': data_box,'layout': go.Layout(
               xaxis={'title': 'feature'},
               yaxis={'title': 'feature value'},
               boxmode='group',
           )})
            ])
        ]),
        dcc.Tab(label='Feature Distribution', children=[
            html.Div([
html.H1('Distribution Plot'),dcc.Graph(
       id='dist-plot',
       figure=create_histogram())
            ])
        ])]
,
        style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto',
},
        content_style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '44px'
    },
        parent_style={
        'maxWidth': '1000px',
        'margin': '0 auto'
    }
    )
])



def generate_scatter(scatter_data):
    return dcc.Graph(id = 'artist_features',
    figure = {
    'data': scatter_data,
    'layout': {'title' : 'Artist Tracks by Feature', 'updatemenus': updatemenus}})

@app.callback(Output(component_id = 'plot-container', component_property ='children'),
[Input(component_id = 'select-artist',component_property = 'value' )]
)
def filter_scatter(input_value):
    global scatter_data
    trace_list = list_of_traces(input_value)
    top_tracks = tempo_normalization_list(trace_list[0])
    oth_tracks = tempo_normalization_list(trace_list[1])
    scatter_data = top_tracks + oth_tracks
    return generate_scatter(scatter_data)
