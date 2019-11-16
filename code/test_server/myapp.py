# myapp.py

from random import random
import time

from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.layouts import row, layout,column
from bokeh.models import Slider
from bokeh.models.mappers import LinearColorMapper
from bokeh.palettes import Spectral6, Dark2
import numpy as np

from bokeh.plotting import figure, show, output_file

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


N = 501
x_0, y_0 = 0, 0
x_1, y_1 = 10, 10

x = np.linspace(x_0, x_1, N)
y = np.linspace(y_0, y_1, N)
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
d_step = 100
cds = ColumnDataSource(data={"image":d})

p = figure(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
p.x_range.range_padding = p.y_range.range_padding = 0

# must give a vector of image data for image parameter
image = p.image(image="image",
                x=x_0,
                y=y_0,
                dw=x_1-x_0,
                dh=y_1-y_0,
                source=cds,
                color_mapper = LinearColorMapper(low=d_min_a, high=d_max_a, palette=Spectral6))


def change_image_contrast(attr, old, new):
    image.glyph.color_mapper.update(low=graph_min_slider.value, high=graph_max_slider.value)
    image.trigger('glyph', image.glyph, image.glyph)


graph_min_slider = Slider(title="Min", start=d_min_a, end=d_max_a, step=(d_max_a-d_min_a)/d_step, value=d_min_a)
graph_max_slider = Slider(title="Max", start=d_min_a, end=d_max_a, step=(d_max_a-d_min_a)/d_step, value=d_max_a)

graph_min_slider.on_change('value', change_image_contrast)
graph_max_slider.on_change('value', change_image_contrast)

#fig = figure(plot_width=500, plot_height=500, x_range=(0, 10), y_range=(0, 10))

#fig_im = fig.image(image=[np.random.randint(0, 100, (10, 10), dtype='int16')], x=[0], y=[0], dw=[10], dh=[10],
#                  color_mapper=LinearColorMapper(low=0, high=100, palette=Greys9))
sliders = column(graph_min_slider, graph_max_slider)#row(text, offset, amplitude, phase, freq)

curdoc().add_root(column(p, sliders, width=800))
