import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotify_package.etl import *

updatemenus = list([
dict(type="buttons",
active=-1,
buttons=list([
dict(label = 'Danceability',
 method = 'update',
 args = [{'visible': [True, False, False, False, False]},
         {'title': 'Tracks by Danceability'}]),
dict(label = 'Energy',
 method = 'update',
 args = [{'visible': [False, True, False, False, False]},
         {'title': 'Tracks by Energy'}]),
dict(label = 'Acousticness',
 method = 'update',
 args = [{'visible': [False, False, True, False, False]},
         {'title': 'Tracks by Acousticness'}]),
dict(label = 'Valence',
 method = 'update',
 args = [{'visible': [False, False, False, True, False]},
         {'title': 'Tracks by Valence'}]),
dict(label = 'Tempo',
 method = 'update',
 args = [{'visible': [False, False, False, False, True]},
         {'title': 'Tracks by Tempo'}]),
dict(label = 'All',
 method = 'update',
 args = [{'visible': [True, True, True, True, True]},
         {'title': 'All Measures'}])]),
font = dict(size=12),
        direction = 'left',
        pad = {'r': 10, 't': 10},
        x = 0.1,
        xanchor = 'left',
        y = 1.3,
        yanchor = 'top'
),
])
