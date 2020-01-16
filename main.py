import panel as pn
import numpy as np
import pandas as pd
import hvplot.pandas
import holoviews as hv
from bokeh.io import curdoc
import circlify


radio = 1

data = sorted(np.random.randint(10, 10000, 150), key=lambda x: -x)
circles = circlify.circlify(data, target_enclosure=circlify.Circle(x=0,y=0,r=radio))

new_df = pd.DataFrame.from_records([{"x":cir.x, "y":cir.y, "siz":cir.r} for cir in circles])

circulo = pd.DataFrame({"x": [0],
                        "y": [0],
                        "r": [radio]})


from bokeh.plotting import Figure, ColumnDataSource

circulos_ds = ColumnDataSource(data=new_df)

circulos = Figure(tools=["hover", "reset", "pan", "tap", "box_select"],
                  match_aspect=True,
                  width=900,
                  height=500
                 )

scatter_1 = circulos.scatter(x="x",
                            y="y",
                            radius="siz",
                            source=circulos_ds)

mi_markdown = pn.pane.Markdown(object="### Selected: ")

def handler(attr, old, new):
    mi_markdown.object = "### Selected: %s, %s, %s" % (attr, old, new)

circulos_ds.selected.on_change("indices", handler)


pane_one = pn.pane.Bokeh(circulos, name="lineas_1")
pane_two = mi_markdown



pane_one.servable()
pane_two.servable()

curdoc().title = "Dashboard de Panel"


