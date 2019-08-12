"""
Methods for sorting queried data
"""

from collections import OrderedDict
import json
from ConfigReader import ConfigReader


class DataSorter:

    def __init__(self, data):
        self.CR = ConfigReader()
        self.data = data

    def data_dict_sorter(self):
        # Takes dictionary. Turns into list of tuples to have large numbers on top
        # Check for empty keys

        sorted_data_dict = sorted(self.data.items(), key=lambda kv: kv[1], reverse=True)
        # Converts back to Dictionary (Ordered)
        sorted_data_dict = OrderedDict(sorted_data_dict)
        sorted_data_dict = {k: v for k, v in sorted_data_dict.items() if v is not None}
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
