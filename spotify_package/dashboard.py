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

app.layout = html.Div(style={'fontFamily': 'Sans-Serif'}, children=[
    html.H1('Spotify Feature Analysis', style={
            'textAlign': 'center', 'margin': '48px 0', 'fontFamily': 'Sans-Serif'}),
    dcc.Markdown('[Spotify Audio Feature Guide](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)'),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Average Feature Values', children=[
            html.Div([
dcc.Graph(
       id='example-graph',
       figure={
           'data': all_bars(),
           'layout': {
               'title': 'Average Feature Values by Artist'}}),
dcc.Markdown('*Note: data for tempo normalized to 0-1 range*')
            ])
        ]),
        dcc.Tab(label='Track Values by Feature', children=[
            html.Div([
dcc.Dropdown(
           id='select-artist',
           options=list_of_artists_for_dropdown(),
           placeholder="Select an artist", value ='Artist'
       ),
html.Div(id= 'plot-container'),
dcc.Markdown('*Note: for all features, data for tempo normalized to 0-1 range*')
            ])
        ]),
dcc.Tab(label='Genre Comparisons', children=[
          html.Div([
dcc.Dropdown(
         id='select-genre',
         options=[{'label': 'Hip-Hop', 'value': 'hiphop'},
           {'label': 'Pop', 'value': 'pop'}],
         placeholder="Select a Genre", value ='Genre'
     ),
html.Div(id= 'box-container'),
dcc.Markdown('*Note: for all features, data for tempo normalized to 0-1 range*')
          ])
      ]),
        dcc.Tab(label='Feature Distribution', children=[
            html.Div([dcc.Graph(
       id='dist-plot',
       figure=histogram),dcc.Markdown(
       '*Note: data for tempo normalized to 0-1 range and acousticness excluded from analysis due to extreme skew*'
            )])
        ])
,
dcc.Tab(label='Artist Comparisons', children=[
        html.Div([
dcc.Dropdown(
       id='select-artist-1',
       options=list_of_artists_for_dropdown(),
       placeholder="Select an Artist", value ='Artist'
   ),dcc.Dropdown(
           id='select-artist-2',
           options=list_of_artists_for_dropdown(),
           placeholder="Select another Artist", value ='Artist_2'
       ),
html.Div(id= 'artist-box-container'),
dcc.Markdown('*Note: for all features, data for tempo normalized to 0-1 range*')
        ])
    ])
    ]
,
        style={
    'width': '100%',
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

def generate_box(box_data):
   return dcc.Graph(
   id='generation',
   figure={
   'data': box_data,'layout': go.Layout(
      xaxis={'title': 'feature'},
      yaxis={'title': 'feature value'},
      boxmode='group',
   )})

def generate_artist_box(box_data):
    return dcc.Graph(
    id='generation',
    figure={
    'data': box_data,'layout': go.Layout(
     xaxis={'title': 'feature'},
     yaxis={'title': 'feature value'},
     boxmode='group',
    )})

@app.callback(Output(component_id = 'box-container', component_property ='children'),
[Input(component_id = 'select-genre',component_property = 'value')])
def filter_box(input_value):
   trace0 = go.Box(y=box_y_values(input_value)[0],x=box_x_values(input_value),name=genres_names_box(input_value)[0],marker=dict(color='#3D9970'))
   trace1 = go.Box(y=box_y_values(input_value)[1],x=box_x_values(input_value),name=genres_names_box(input_value)[1],marker=dict(color='#FF4136'))
   trace_list = [trace0, trace1]
   return generate_box(trace_list)

@app.callback(Output(component_id = 'artist-box-container', component_property ='children'),
[Input(component_id = 'select-artist-1',component_property = 'value'),
Input(component_id = 'select-artist-2',component_property = 'value')]
)
def filter_artist_box(input_value, input_value_2):
    trace0 = go.Box(y=artist_box_y_values(input_value),x=artist_box_x_values(input_value),name=input_value,marker=dict(color='#3D9970'))
    trace1 = go.Box(y=artist_box_y_values(input_value_2),x=artist_box_x_values(input_value_2),name=input_value_2,marker=dict(color='#FF4136'))
    trace_list = [trace0, trace1]
    return generate_artist_box(trace_list)
