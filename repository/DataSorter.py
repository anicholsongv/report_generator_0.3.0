

import collections

class DataSorter:

    def __init__(self, data_dict):
        self.data_dict = data_dict

    def data_dict_sorter(self):
        # Sorts dict into list of tuples to have large numbers on top
        sorted_data_dict = sorted(self.data_dict.items(), key=lambda kv: kv[1], reverse=True)

        # Converts back to Dictionary (Ordered)
        sorted_data_dict = collections.OrderedDict(sorted_data_dict)
        return sorted_data_dict
