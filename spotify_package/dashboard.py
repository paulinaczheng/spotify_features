import dash_core_components as dcc
import dash_html_components as html
from spotify_package import app
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotify_package.charts import *
import json

app.layout = html.Div(children= [
html.H1('Artist Features Plot'),
dcc.Graph(id = 'artist_features',
figure = {
'data': data,
'layout': {'title' :  'Artist Features', 'updatemenus': updatemenus

             }}
)
])
