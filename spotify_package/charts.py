import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotify_package.etl import *

marker1 = dict(
size = 20,
color = 'green',)
marker2 = dict(
size = 20,
color = 'blue',
line = dict(
width = 2,))
marker3 = dict(
size = 20,
color = 'green',)
trace1 = create_trace('Charlie Puth', 'danceability', 'Puth top tracks danceability', marker1, top_track=True)
trace2 = create_trace('Charlie Puth', 'danceability', 'Puth other tracks danceability', marker2)
trace3 = create_trace('Charlie Puth', 'valence', 'Puth top tracks valence', marker1, top_track=True)
trace4 = create_trace('Charlie Puth', 'valence', 'Puth other tracks valence', marker2)
trace_dance_top = go.Scatter(
trace1)

trace_dance = go.Scatter(
trace2
)
trace_pitch_top = go.Scatter(
trace3
)

trace_pitch = go.Scatter(
trace4
)

data = [trace_dance, trace_dance_top, trace_pitch, trace_pitch_top]

# high_annotations=[dict(x='2016-03-01',
#                        y=df.High.mean(),
#                        xref='x', yref='y',
#                        text='High Average:<br>'+str(df.High.mean()),
#                        ax=0, ay=-40),
#                   dict(x=df.High.idxmax(),
#                        y=df.High.max(),
#                        xref='x', yref='y',
#                        text='High Max:<br>'+str(df.High.max()),
#                        ax=0, ay=-40)]
# low_annotations=[dict(x='2015-05-01',
#                       y=df.Low.mean(),
#                       xref='x', yref='y',
#                       text='Low Average:<br>'+str(df.Low.mean()),
#                       ax=0, ay=40),
#                  dict(x=df.High.idxmin(),
#                       y=df.Low.min(),
#                       xref='x', yref='y',
#                       text='Low Min:<br>'+str(df.Low.min()),
#                       ax=0, ay=40)]

updatemenus = list([
dict(type="buttons",
active=-1,
buttons=list([
dict(label = 'Dance',
 method = 'update',
 args = [{'visible': [True, True, False, False]},
         {'title': 'Tracks by Dance Measure'}]),
dict(label = 'Pitch',
 method = 'update',
 args = [{'visible': [False, False, True, True]},
         {'title': 'Tracks by Pitch Measure'}]),
dict(label = 'All',
 method = 'update',
 args = [{'visible': [True, True, True, True]},
         {'title': 'All Measures'}])]),
#     # direction = 'down',
# x = 0,
# xanchor = 'left',
# y = 0,
# yanchor = 'top',
# bgcolor = 'white',
# bordercolor = 'white',
# fontcolor = 'black',
font = dict(size=20),
#     buttons=list([
#     dict(args=['type', 'surface'],
#         label='Migos',
#         method='restyle'
#     ),
#
#     dict(
#         args=['type', 'heatmap'],
#         label='Charlie Puth',
#         method='restyle'
#     )]),
#      direction = 'left',
# pad = {'r': 10, 't': 10},
# showactive = True,
# type = 'buttons',
# x = 0.1,
# xanchor = 'left',
# y = 1.1,
# yanchor = 'top'
),
])
