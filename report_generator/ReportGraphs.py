
"""Create an svg image of graph based on a dictionary"""

import collections
import plotly.graph_objs as go
import plotly.io as pio


class PlotlyGraph:

    def __init__(self, data_dict, graph_title, extra_title):
        self.data_dict = data_dict
        self.graph_title = graph_title
        self.extra_title = extra_title
        self.gv_colours = ['#1F83C0', '#BCA478', '#2CBA94', '#C94F5F', '#7D4EA0', '#CBA333', '#202733']

    def data_dict_sorter(self):
        # Sorts dict into list of tuples to have large numbers on top
        sorted_data_dict = sorted(self.data_dict.items(), key=lambda kv: kv[1], reverse=True)

        # Converts back to Dictionary (Ordered)
        sorted_data_dict = collections.OrderedDict(sorted_data_dict)
        return sorted_data_dict

    def horizontal_gv_bar(self):
        # Horiz bar graph with largest on top with gv colours
        graph_title = str(self.graph_title)
        extra_title = str(self.extra_title)
        data_dict = self.data_dict_sorter()
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
        pio.write_image(bar_graph, f'{file_name_string}.svg', format='svg')

        print(file_name_string, "successfully created")
        return f'{file_name_string}.svg'

    def horizontal_gv_bar_image(self):
        # Horiz bar graph with largest on top with gv colours
        graph_title = str(self.graph_title)
        extra_title = str(self.extra_title)
        data_dict = self.data_dict_sorter()
        gv_colours = self.gv_colours
        x_data = list(data_dict.values())
        y_data = list(data_dict.keys())
        y_data[1] = y_data[1] + " "

        # Graph values and how they are represented
        graph_data = [go.Bar(
            x=x_data,
            y=[i.rsplit('/', 1)[-1] for i in y_data],
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
        pio.write_image(bar_graph, f'{file_name_string}.svg', format='svg')

        print(file_name_string, "successfully created")
        return f'{file_name_string}.svg'
