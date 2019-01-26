class Node:
    """
    Class to represent one node in a parse tree
    """

    def __init__(self, tree, tree_id, pos):
        self.tree = tree
        self.tree_id = tree_id
        self.pos = pos

    def __str__(self):
        string = "id " + str(self.tree_id) + "\n"
        string += "pos " + str(self.pos) + "\n"
        try:
            string += "\nx " + str(self.x) + "\n"
        except AttributeError:
            return string

        try:
            string += "m " + str(self.m) + "\n"
            string += "h " + str(self.h) + "\n"
        except AttributeError:
            return string

        return string

    def __repr__(self):
        return self.__str__()

    def set_x(self, x):
        self.x = x

    def set_h(self, m, h):
        self.m = m
        self.h = h
