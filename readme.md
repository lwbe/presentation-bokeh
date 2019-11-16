# Présentation de Bokeh

Réunion de développement novembre 2019

youtube video
-  https://www.youtube.com/watch?v=HmI1foA0MZc



## matplotlib

interactive plot with ipython

in ipython type %pylab


# jupyter notebook and bokeh

jupyter labextension install @bokeh/jupyter_bokeh

il faut faire 
from bokeh.io import output_notebook

....

output_notebook() 

....

show(p)

et il faut utiliser output_notebook() function from bokeh.io instead of (or in addition to) the output_file() f