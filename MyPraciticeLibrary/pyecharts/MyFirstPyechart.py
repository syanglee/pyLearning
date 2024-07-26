from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["审计疑点数", "审计问题数", "审计建议数", "已整改建议数"])
bar.add_yaxis("2018", [20, 10, 6, 4])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render("myFirstChart.html")
