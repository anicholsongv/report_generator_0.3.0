"""
Distribution of Categories throughout the classified files
This class creates a graph and sorted dictionary in the init
The dictionary is used to create a table
The svg file path is passed to the html
"""

from rendering.HorizGraphDrawer import HorizGraphDrawer
from sorters.DataSorter import DataSorter
from jinja2 import Template


class CategoryDistributionPage:
    def __init__(self, info_dict):
        self.info_dict = info_dict
        # Create DataSorter Instance
        self.DS = DataSorter(info_dict['data'])
        self.data_dict = self.DS.data_dict_sorter()
        # Create HorizGraphDrawer Instance
        self.HGD = HorizGraphDrawer(self.info_dict)
        self.graph_name = self.HGD.horizontal_graph()

    def html_string_writer(self):
        template = Template("""<p>The distribution of files within their categories are shown below.</p>
                                <figure><img src="{{ graph_name }}" class="pie_charts">
                                <figcaption>The above graph outlines the distribution of Documents that have been 
                                classified by this scan.</figcaption></figure>
                                <div class="information_box">
                                <p>The total count of each category is as follows:</p>
                                    <ul>
                                {% for k, v in data_dict.items() %}
                                        <li>{{ k }}: <b>{{ v }}</b></li>
                                {% endfor %}       </ul>
                                </div>
                                <div class="page_break_div"></div>""")
        return template.render(graph_name=self.graph_name, data_dict=self.data_dict)
