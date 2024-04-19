from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 990),
    ("上海市", 1200),
    ("安徽省", 200),
    ("广东省", 2000),
]
map.add("出口量", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 500, "label": "1-500", "color": "#CCFFFF"},
            {"min": 500, "max": 1000, "label": "500-1000", "color": "#FF6666"},
            {"min": 1000, "max": 5000, "label": "1000-5000", "color": "#990033"}
        ]
    )
)

map.render("map_charts.html")
