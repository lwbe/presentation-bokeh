import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.layouts import row, layout
from bokeh.models import Slider
from bokeh.models.mappers import LinearColorMapper
from bokeh.palettes import Greys9

def change_image_contrast(attr, old, new):
    fig_im.glyph.color_mapper.update(low=graph_min_slider.value, high=graph_max_slider.value)
    fig_im.trigger('glyph', fig_im.glyph, fig_im.glyph)

graph_min_slider = Slider(title="Min", start=0, end=99, step=1, value=0)
graph_max_slider = Slider(title="Max", start=1, end=100, step=1, value=100)

graph_min_slider.on_change('value', change_image_contrast)
graph_max_slider.on_change('value', change_image_contrast)

fig = figure(plot_width=500, plot_height=500, x_range=(0, 10), y_range=(0, 10))

fig_im = fig.image(image=[np.random.randint(0, 100, (10, 10), dtype='int16')], x=[0], y=[0], dw=[10], dh=[10],
                   color_mapper=LinearColorMapper(low=0, high=100, palette=Greys9))

curdoc().add_root(layout([fig], [row([graph_min_slider, graph_max_slider])]))
