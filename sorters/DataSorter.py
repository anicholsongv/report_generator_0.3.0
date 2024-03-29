"""
Methods for sorting queried data
"""

from collections import OrderedDict
from ConfigReader import ConfigReader


class DataSorter:

    def __init__(self, data):
        self.CR = ConfigReader()
        self.data = data

    def data_dict_sorter(self):
        # Takes dictionary. Turns into list of tuples (orderedDict) to have large numbers on first
        # Check for underscores and remove empty keys
        shaved_data_dict = {k.replace("_", " "): v for k, v in self.data.items() if k is not ''}
        sorted_data_dict = sorted(shaved_data_dict.items(), key=lambda kv: kv[1], reverse=True)
        # Converts back to Dictionary (Ordered)
        sorted_data_dict = OrderedDict(sorted_data_dict)

        return sorted_data_dict

    def folder_counter(self):
        # Takes a list of Tuples
        # Get folder path, exclude share name
        tuple_data = [(k.rsplit('/', 1)[0].split(f'{self.CR.scanned_share_name}', 1)[-1], v)
                      for (k, v) in self.data]
        # Count and sort documents in to folders
        counted_dict = {}
        for k, v in tuple_data:
            if k not in counted_dict.keys():
                counted_dict[k] = v
            else:
                counted_dict[k] += v
        # Create Ordered Dictionary
        finished_dict = OrderedDict(reversed(sorted(counted_dict.items(), key=lambda i: i[1])))
        return finished_dict
