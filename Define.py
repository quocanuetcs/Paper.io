#CONST
WHIDTH = 1500
HEIGHT = 900
STRIDE = 25

class ZoneType():
    def __init__(self, data_x_min = [], data_x_max = [], data_y = []):
        self.data_x_min = data_x_min
        self.data_x_max = data_x_max
        self.data_y = data_y

class XYType():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PlayerColor():
    def __init__(self, head, line, zone):
        self.head = head
        self.line = line
        self.zone = zone

class PlayerType():
    def __init__(self, head, line, zone, color, live):
        self.head = head
        self. line = line
        self. zone = zone
        self.color = color
        self.live = live



