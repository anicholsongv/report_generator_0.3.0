
"""Create an svg image of graph based on a dictionary"""


import plotly.graph_objs as go
import plotly.io as pio
from sorters.DataSorter import DataSorter
from styling.RGColours import RGColours


class HorizGraphDrawer:
    output_dir = "../data/dist/"

    def __init__(self, info_dict):
        self.RGC = RGColours()
        self.gv_colours = self.RGC.gv_colour_list
        self.data_dict = info_dict['data']
        self.description = info_dict['description']


    def horizontal_graph(self):
        # Horiz bar graph with largest on top with gv colours
        graph_title = self.description
        DS = DataSorter(self.data_dict)
        sorted_dict = DS.data_dict_sorter()
        gv_colours = self.gv_colours()
        x_data = list(sorted_dict.values())
        y_data = list(sorted_dict.keys())

        # Graph values and how they are represented
        graph_data = [go.Bar(
            x=x_data,
            y=y_data,
            text=x_data,  # Puts data on the bars
            textposition='auto',
            orientation='h',
            marker=dict(color=gv_colours[:len(self.data_dict)]),
        )]

        # Graph visual structure
        graph_layout = go.Layout(title=graph_title, autosize=True, width=800, height=500,
                                 margin=go.layout.Margin(l=80, r=80, b=100, t=100, pad=4),
                                 font=dict(family="Lato", size=12),
                                 yaxis=dict(autorange="reversed", automargin=True),
                                 xaxis=dict(tickformat=',d', automargin=True))

        # Create graph
        bar_graph = go.Figure(data=graph_data, layout=graph_layout)

        # Convert to svg
        file_name_string = str(graph_title.replace(" ", "_")) + '_bar_graph'
        pio.write_image(bar_graph, f'{self.output_dir}{file_name_string}.svg', format='svg')

        print(file_name_string, "successfully created")

        return f'{self.output_dir}{file_name_string}.svg'

