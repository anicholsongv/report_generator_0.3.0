"""
Draws Pie Charts using plotly
"""

import plotly.graph_objs as go
import plotly.io as pio
from sorters.DataSorter import DataSorter
from styling.RGColours import RGColours


class PieChartDrawer:
    output_dir = "../data/dist/"

    def __init__(self, info_dict):
        self.RGC = RGColours()
        self.gv_colours = self.RGC.gv_colour_list
        self.data_dict = info_dict['data']
        self.description = info_dict['description']


    def pie_chart(self):
        # if the data has 2 entries make the hole in the middle bigger
        graph_title = self.description
        DS = DataSorter(self.data_dict)
        sorted_dict = DS.data_dict_sorter()
        gv_colours = self.gv_colours()
        graph_labels = list(sorted_dict.keys())
        graph_values = list(sorted_dict.values())
        graph_data = [go.Pie(
            values=graph_values,
            labels=graph_labels,
            marker=dict(colors=gv_colours[:len(graph_values)]),
            hole=.4
        )]
        graph_layout = go.Layout(title=graph_title, autosize=True, width=500, height=500,
                                    margin=go.layout.Margin(l=50, r=50, b=100, t=100, pad=4),
                                    font=dict(family="Lato Regular", size=14))
        pie_chart = go.Figure(data=graph_data, layout=graph_layout)
        file_name_string = str(graph_title.replace(" ", "_")) + '_pie_chart'
        pio.write_image(pie_chart, f'{self.output_dir}{file_name_string}.svg', format='svg')

        print(file_name_string, "successfully created")

        return f'{self.output_dir}{file_name_string}.svg'




