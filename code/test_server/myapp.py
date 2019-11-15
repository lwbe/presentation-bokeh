# myapp.py

from random import random
import time

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from bokeh.models.sources import ColumnDataSource

# create a plot and style its properties
#p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
#p.border_fill_color = 'black'
#p.background_fill_color = 'black'
#p.outline_line_color = None
#p.grid.grid_line_color = None

# add a text renderer to our plot (no data yet)
#r = p.text(x=[], y=[], text=[], text_color=[], text_font_size="20pt",
#           text_baseline="middle", text_align="center")

#i = 0

#ds = r.data_source

# create a callback that will add a number in a random location

import numpy as np

from bokeh.plotting import figure, show, output_file

N = 500
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
xx, yy = np.meshgrid(x, y)

# amplitude variation
a_a = 1.
s_a = 5.
x_a = 6.
y_a = 5.

# a "nasty"peak
a_p = 100.
s_p = .01
x_p = 4.
y_p = 4.

A = a_a*np.exp(-((xx-x_a)**2+(yy-y_a)**2)/s_a**2)

B = np.sin(xx)*np.cos(yy)
C = a_p*np.exp(-((xx-x_p)**2+(yy-y_p)**2)/s_p**2)

d= A*B+C

d_min_a = np.min(d)
d_max_a = np.max(d)

cds = ColumnDataSource({"data":d})

p = figure(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
p.x_range.range_padding = p.y_range.range_padding = 0

# must give a vector of image data for image parameter
image = p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Spectral11")

# add a button widget and configure with the call back
button = Button(label="Press Me")

max_i=10
i=0
print("OK")
def callback():
    global i,max_i

    if i < max_i:
        d_min = d_min_a+0.4*i/max_i*(d_max_a-d_min_a)
        d_max = d_max_a-0.4*i/max_i*(d_max_a-d_min_a)
        print(d_min,d_max)
        image.data_source.data["image"] = np.where(d<d_min,d_min,np.where(d>d_max,d_max,d))
        i += 1
    else:
        pass

button.on_click(callback)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, p))
