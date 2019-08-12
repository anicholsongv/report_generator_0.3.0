"""
Draws Pie Charts using plotly
"""

import plotly.graph_objs as go
import plotly.io as pio
from repository.DataSorter import DataSorter


class PieChartDrawer:
    def __init__(self, info_dict):
        self.data_dict = info_dict['data']
        self.description = info_dict['description']














