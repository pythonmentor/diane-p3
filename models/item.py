from position import Position

class Item:
    def __init__(self, name, position):
        self.name = name
        self.position = Position(x, y)

    def get_position(self):
            return self.position