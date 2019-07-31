
"""Create an svg image of graph based on a dictionary"""


import plotly.graph_objs as go
import plotly.io as pio
from repository.DataSorter import DataSorter


class HorizGraphDrawer:
    output_dir = "../data/dist/"

    def __init__(self, data_dict, graph_title, extra_title):
        self.data_dict = data_dict
        self.graph_title = graph_title
        self.extra_title = extra_title
        self.gv_colours = ['#1F83C0', '#BCA478', '#2CBA94', '#C94F5F', '#7D4EA0', '#CBA333', '#202733']


    def horizontal_gv_bar(self):
        # Horiz bar graph with largest on top with gv colours
        graph_title = str(self.graph_title)
        extra_title = str(self.extra_title)
        data_dict = DataSorter.data_dict_sorter(self.data_dict)
        gv_colours = self.gv_colours
        x_data = list(data_dict.values())
        y_data = list(data_dict.keys())

        # Graph values and how they are represented
        graph_data = [go.Bar(
            x=x_data,
            y=y_data,
            text=x_data,  # Puts data on the bars
            textposition='auto',
            orientation='h',
            marker=dict(color=gv_colours[:len(data_dict)]),
        )]

        # Graph visual structure
        graph_layout = go.Layout(title=graph_title,autosize=True, width=800,height=500,
                                       margin=go.layout.Margin(l=80, r=80, b=100, t=100, pad=4),
                                    font=dict(family="Lato", size=12),
                                 yaxis=dict(autorange="reversed", automargin=True),
                                 xaxis=dict(tickformat=',d', automargin=True))

        # Create graph
        bar_graph = go.Figure(data=graph_data, layout=graph_layout)

        # Convert to svg
        file_name_string = extra_title + str(graph_title.replace(" ", "")[:5]) + '_bar_graph'
        pio.write_image(bar_graph, f'{self.output_dir}{file_name_string}.svg', format='svg')

        print(file_name_string, "successfully created")

        return {'graph_file_name': f'{file_name_string}.svg'}

