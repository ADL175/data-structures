"""Creates a Graph data structure, featuring graph traversal and two shortest path algorithms."""
import timeit
import random

class Graph(object):
    """Define the Graph class structure."""

    def __init__(self):
        """Make an empty dictionary."""
        self.graph_dict = {}

    def add_node(self, value):
        """Check if node of given value exists in dictionary.If not, add it with an empty list."""
        try:
            self.graph_dict[value]
        except KeyError:
            self.graph_dict[value] = []

    def add_edge(self, val1, val2):
        """Ensure that nodes of val1 and val2 exist (creating them if they don't.Then make an edge connecting val1 to val2."""
        if [val1, val2] not in self.edges():
            self.add_node(val1)
            self.add_node(val2)
            self.graph_dict[val1].append(val2)
        else:
            raise KeyError("Edge already exists.")

    def nodes(self):
        """Return a list of all keys in dictionary."""
        return list(self.graph_dict.keys())

    def edges(self):
        """Return a list of all edges in dictionary."""
        to_return = []
        for keys, values in self.graph_dict.items():
            for i in values:
                to_return.append([keys, i])
        return to_return

    def del_node(self, val):
        """Delete a node from the graph, and from all edge pointers."""
        try:
            del self.graph_dict[val]
            for keys, values in self.graph_dict.items():
                for i in values:
                    if i == val:
                        values.remove(i)
        except KeyError:

            raise KeyError("No such node exists.")

    def del_edge(self, val1, val2):
        """Delete an edge from graph."""
        try:
            for node in self.graph_dict[val1]:
                if node == val2:
                    self.graph_dict[val1].remove(node)
        except KeyError:

            raise KeyError("No such node exists.")

    def has_node(self, val):
        """Check if graph has a given node in it."""
        try:
            self.graph_dict[val]
            return True

        except KeyError:

            return False

    def neighbors(self, val):
        """Return all nodes connected to given node."""
        try:
            return self.graph_dict[val]
        except KeyError:

            raise KeyError("No such node exists.")

    def adjacent(self, val1, val2):
        """Return True if edge exists, else return false."""
        try:
            self.graph_dict[val2]
            return len(list(filter(lambda node: node[0] == val2, self.graph_dict[val1]))) > 0
        except KeyError:

            raise KeyError("Value given not in graph.")