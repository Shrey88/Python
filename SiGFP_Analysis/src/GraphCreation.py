from openpyxl import load_workbook
from openpyxl.chart import BarChart3D, Reference
from openpyxl.worksheet import worksheet


class GraphCreation(object):

    def __init__(self, ws: worksheet=None):
        if ws is None:
            raise Exception("Worksheet object not provided")
        else:
            self._ws = ws

    def create_graph(self):
        chart = BarChart3D()

        data = Reference(self._ws, min_row=1, min_col=4, max_row=22, max_col=5)
        categories = Reference(self._ws, min_row=2,min_col=2, max_row=22)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        chart.style = 10
        chart.title="SiGFP Summary Report"
        return chart
