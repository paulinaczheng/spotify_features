import dash_core_components as dcc
import dash_html_components as html
from spotify_package import app
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotify_package.charts import *
import json

app.layout = html.Div(children= [html.H1('Artist Features Plot'),
dcc.Graph(id = 'artist_features',
figure = {
'data': data,
'layout': {'title' :  'Artist Features', 'updatemenus': updatemenus

             }}
)
])

# app.layout = html.Div(children=[dcc.Dropdown(
#         id='sort-by-selector',
#         options=[
#             {'label': 'Country', 'value': 'Country'},
#             {'label': 'Pho', 'value': 'Pho'},
#             {'label': 'Ramen', 'value': 'Ramen'},
#             {'label': 'Soba', 'value': 'Soba'}
#         ], value="Country"), html.H1("Song and Artist Features, Using the Spotify API"),
# html.H3("Graph Title:"),
# dcc.Graph(id = 'uber_pricing_graph', figure = {'data': [
#     {'name': "Brooklyn",
#     'x': [0.86, 1.5, 2.2, 2.6, 2.7, 3, 3.67],
#     'y': [6.40, 8.34, 9.46, 11.13, 12.55, 18.68],
#     'type': "line"},
#     {'name': "Manhattan",
#     'x': [0.93, 1.33, 2.4, 2.6, 2.94, 3.34, 4.11],
#     'y': [9.34, 10.09, 13.24, 16.53, 15.64, 25.65],
#     'type': "line"}
# ], 'layout': {'title': 'Uber Pricing in Brooklyn and Manhattan'}}
# ), html.Div(id='table-container')
#
# ])

# def generate_table(table_data=data):
#     return html.Table(id='food-table', children=
#         # create table headers (the first table row)
#         [html.Tr(id='headers', children=[html.Th(col) for col in table_data[0].keys()])]
#         # combine the table headers and table data lists into one list
#         +
#         # create more table rows containing table cells with all our data
#         [html.Tr(id='row-data', children=[
#             html.Td(data_dict[column]) for column in data_dict.keys()
#         ]) for data_dict in table_data]
#     )
# # how do you call this in app.layout?
# @app.callback(Output(component_id='table-container', component_property='children'),
#     [Input(component_id='sort-by-selector', component_property='value')])
# def sort_table(input_value):
#     global data #allows you to share data between callbacks?
#     sorted_data = sorted(data, key=lambda datum: datum[input_value]) #sort data on the input value from @callback
#     return generate_table(sorted_data)
