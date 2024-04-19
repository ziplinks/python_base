from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts

line = Line()
line.add_xaxis(["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"])
line.add_yaxis("人流量", [10, 50, 86, 23, 56, 150, 86])
# 设置配置项
line.set_global_opts(
    title_opts=TitleOpts(title="这是一个非常显眼的标题", pos_left="center", pos_top="2%"),
    legend_opts=LegendOpts(pos_top="6%"),
    toolbox_opts=ToolboxOpts(is_show=True)
)
line.render()
