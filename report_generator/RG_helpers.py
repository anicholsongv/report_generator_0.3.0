
"""Small usefull functions for parsing various report generator data"""



class RGHelpers(object):
    """A class that parses, sorts and returns dictionaries or integers from psycopg2 queries"""

    def __init__(self):
        self._items = []

    def isEmpty(self):
        if not self._items:
            return True
        else:
            return False

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __str__(self):
        print(self._items)




example = RGHelpers()

example.push(5)
example.push(10)
example.pop()

example.__str__()