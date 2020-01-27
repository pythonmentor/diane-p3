class Item:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.status = "not_catched"

    def __eq__(self, other):
        """ Cette fonction permet de comparer si deux positions sont identiques. """
        if self.position.x == other.x and self.position.y == other.y:
            return True