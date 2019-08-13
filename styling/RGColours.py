"""
A class of styling to be used throughout the Report Generator
"""


class RGColours:
    def __init__(self):
        self.gv_aqua = 'rgba(44, 186, 148, 1)'
        self.gv_pink = 'rgba(201, 79, 95, 1)'
        self.gv_blue = 'rgba(31, 131, 192, 1)'
        self.gv_yellow = 'rgba(203, 163, 51, 1)'
        self.gv_navy = 'rgba(32, 39, 51, 1)'
        self.gv_purple = 'rgba(125, 78, 160, 1)'
        self.gv_gold = 'rgba(188, 164, 120, 1)'
        self.gv_jade = 'rgba(180, 240, 142, 1)'
        self.gv_orange = 'rgba(237, 190, 120, 1)'
        self.gv_turquoise = 'rgba(179, 219, 255, 1)'

    # List of ten colours for use when the colours are used in order
    def gv_colour_list(self):
        return [self.gv_blue, self.gv_gold, self.gv_aqua, self.gv_pink, self.gv_purple,
                self.gv_yellow, self.gv_navy, self.gv_jade, self.gv_orange, self.gv_turquoise]

    def gv_aqua(self):
        return self.gv_aqua

    def gv_pink(self):
        return self.gv_pink

    def gv_blue(self):
        return self.gv_blue

    def gv_yellow(self):
        return self.gv_yellow

    def gv_navy(self):
        return self.gv_navy

    def gv_purple(self):
        return self.gv_purple

    def gv_gold(self):
        return self.gv_gold

    def gv_jade(self):
        return self.gv_jade

    def gv_orange(self):
        return self.gv_orange

    def gv_turquoise(self):
        return self.gv_turquoise
