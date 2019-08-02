"""
Queries that join the Classification and Access psql tables

"""


class ClassificationAccessRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table
