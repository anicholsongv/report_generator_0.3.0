"""
Methods for sorting queried data
"""

from collections import OrderedDict


class DataSorter:

    def __init__(self, data):
        self.data = data

    def data_dict_sorter(self):
        # Takes dictionary. Turns into list of tuples to have large numbers on top
        sorted_data_dict = sorted(self.data.items(), key=lambda kv: kv[1], reverse=True)

        # Converts back to Dictionary (Ordered)
        sorted_data_dict = OrderedDict(sorted_data_dict)
        return sorted_data_dict

    def folder_counter(self):
        # Takes a list of Tuples, gets file paths minus scanned share
        # Get folder path, exclude share name
        finance_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                                 for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        finance_folder_dict = {}
        for k, v in self.data:
            if k not in data_dict.keys():
                data_dict[k] = v
            else:
                data_dict[k] += v
        # Create Ordered Dictionary
        data_dict = OrderedDict(reversed(sorted(data_dict.items(), key=lambda i: i[1])))
        return data_dict
