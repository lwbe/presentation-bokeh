import numpy as np

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import figure, curdoc

N = 500
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*yy

p = figure(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
p.x_range.range_padding = p.y_range.range_padding = 0

# must give a vector of image data for image parameter
p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Spectral11")

# add a button widget and configure with the call back
button = Button(label="Press Me")
# button.on_click(callback)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, p))
