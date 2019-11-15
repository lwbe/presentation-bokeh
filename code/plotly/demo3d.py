import chart_studio.plotly as py

from plotly.graph_objs.layout import Scene
import plotly.graph_objs as go
from plotly.graph_objs.layout.scene import XAxis,YAxis,ZAxis


import numpy as np

xx=np.linspace(-3.5, 3.5, 100)
yy=np.linspace(-3.5, 3.5, 100)
x,y=np.meshgrid(xx, yy)
z=np.exp(-(x-1)**2-y**2)-10*(x**3+y**4-x/5)*np.exp(-(x**2+y**2))


colorscale=[[0.0, 'rgb(20,29,67)'],
           [0.1, 'rgb(28,76,96)'],
           [0.2, 'rgb(16,125,121)'],
           [0.3, 'rgb(92,166,133)'],
           [0.4, 'rgb(182,202,175)'],
           [0.5, 'rgb(253,245,243)'],
           [0.6, 'rgb(230,183,162)'],
           [0.7, 'rgb(211,118,105)'],
           [0.8, 'rgb(174,63,95)'],
           [0.9, 'rgb(116,25,93)'],
           [1.0, 'rgb(51,13,53)']]


textz=[['x: '+'{:0.5f}'.format(x[i][j])+'<br>y: '+'{:0.5f}'.format(y[i][j])+
        '<br>z: '+'{:0.5f}'.format(z[i][j]) for j in range(z.shape[1])] for i in range(z.shape[0])]

trace1= go.Surface(z=z,
                x=x,
                y=y,
                colorscale=colorscale,
                text=textz,
                hoverinfo='text',
                )


axis = dict(
showbackground=True,
backgroundcolor="rgb(230, 230,230)",
showgrid=False,
zeroline=False,
showline=False)

ztickvals=list(range(-6,4))
layout = go.Layout(title="Projections of a surface onto coordinate planes" ,
                autosize=False,
                width=700,
                height=600,
                scene=Scene(xaxis=XAxis(axis, range=[-3.5, 3.5]),
                            yaxis=YAxis(axis, range=[-3.5, 3.5]),
                            zaxis=ZAxis(axis , tickvals=ztickvals),
                            aspectratio=dict(x=1,
                                             y=1,
                                             z=0.95)
                           )
                )
z_offset=(np.min(z)-2)*np.ones(z.shape)#
x_offset=np.min(xx)*np.ones(z.shape)
y_offset=np.min(yy)*np.ones(z.shape)

proj_z=lambda x, y, z: z#projection in the z-direction
colorsurfz=proj_z(x,y,z)
proj_x=lambda x, y, z: x
colorsurfx=proj_z(x,y,z)
proj_y=lambda x, y, z: y
colorsurfy=proj_z(x,y,z)

textx=[['y: '+'{:0.5f}'.format(y[i][j])+'<br>z: '+'{:0.5f}'.format(z[i][j])+
        '<br>x: '+'{:0.5f}'.format(x[i][j]) for j in range(z.shape[1])]  for i in range(z.shape[0])]
texty=[['x: '+'{:0.5f}'.format(x[i][j])+'<br>z: '+'{:0.5f}'.format(z[i][j]) +
        '<br>y: '+'{:0.5f}'.format(y[i][j]) for j in range(z.shape[1])] for i in range(z.shape[0])]

tracex =go.Surface(z=z,
                x=x_offset,
                y=y,
                colorscale=colorscale,
                showlegend=False,
                showscale=False,
                surfacecolor=colorsurfx,
                text=textx,
                hoverinfo='text'
               )
tracey =go.Surface(z=z,
                x=x,
                y=y_offset,
                colorscale=colorscale,
                showlegend=False,
                showscale=False,
                surfacecolor=colorsurfy,
                text=texty,
                hoverinfo='text'
               )
tracez =go.Surface(z=z_offset,
                x=x,
                y=y,
                colorscale=colorscale,
                showlegend=False,
                showscale=False,
                surfacecolor=colorsurfx,
                text=textz,
                hoverinfo='text'
               )

data=Data([trace1, tracex, tracey, tracez])
fig = Figure(data=data, layout=layout)
py.iplot(fig)
