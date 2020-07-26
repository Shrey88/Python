""" *
    *   Graph
    * """
from openpyxl.workbook import Workbook
from openpyxl.chart import PieChart, Reference, Series, PieChart3D

wb = Workbook()
ws = wb.active

""" *
    *   let's create a data variable and make it a list.
    *
    *   each list inside the data list corresponds to column
    *   
    * """
data= [
    ['Flavor', 'Solid'],
    ['Vanilla', 1500],
    ['Chocolate', 1700],
    ['Strawberry', 600],
    ['Pumpkin Spice', 950]
]

for rows in data:
    ws.append(rows)

#   create a Pie chart variable
chart = PieChart()

#   we need to inform excel how to use the data and map it to chart
#   we have two types of data, labels and numerical data
labels = Reference(ws, min_col=1, max_row=5, min_row=2)
data = Reference(ws, min_col=2, min_row=1, max_row=5)
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)
chart.title="Ice Cream by Flavor"

#   set the column where you want to add the chart.
ws.add_chart(chart, 'C1')
wb.save(".\\Exercise Files\\Piechart.xlsx")
