"""Graphy mcgraphface"""

class Graph(object):
    """Define the Link_List class structure"""
    def __init__(self):
        """Make an empty dictionary."""
        self.graph_dict = {}


    def add_node(self, value):
        """Check if node of given value exists in dictionary.
        If not, add it with an empty list."""
        try:
            self.graph_dict[value]
        except KeyError:
            self.graph_dict[value] = []

    def add_edge(self, val1, val2):
        """Ensure that nodes of val1 and val2 exist (creating them if they don't.
        Then make an edge connecting val1 to val2."""
        self.add_node(val1)
        self.add_node(val2)
        self.graph_dict[val1].append(val2)

    def nodes(self):
        """Return a list of all keys in dictionary."""
        to_return = []
        for keys, values in self.graph_dict.items():
            to_return.append(keys)
        return to_return

    def edges(self):
        """Return a list of all edges in dictionary."""
        to_return = []
        for keys, values in self.graph_dict.items():
            for i in values:
                to_return.append([keys, i])
        return to_return

    def del_node(self, val):
        """Deletes a node from the graph, and from all edge pointers."""
        try:
            del self.graph_dict[val]
            for keys, values in self.graph_dict.items():
                for i in values:
                    if i == val:
                        values.remove(i)
        except KeyError:
            raise KeyError("No such node exists.")
    def del_edge(self, val1, val2):
        """Deletes an edge from graph."""
        try:
            self.graph_dict[val1].remove(val2)
        except ValueError:
            raise ValueError("No such edge exists.")
    def has_node(self, val):
        """Checks if graph has a given node in it."""
        try:
            self.graph_dict[val]
            return True
        except KeyError:
            return False
    def neighbors(self, val):
        """Return all nodes connected to given node."""
        try:
            to_return = []
            for value in self.graph_dict[val]:
                to_return.append(value)
            return to_return
        except KeyError:
            raise KeyError("No such node exists.")
    def adjacent(self, val1, val2):
        """Return True if edge exists, else return false."""
        try:
            self.graph_dict[val2]
            if val2 in self.graph_dict[val1]:
                return True
            else: 
                return False
        except KeyError:
            raise KeyError("Value given not in graph.")
    def depth(self, val):
        from stack import Stack
        seen = []
        next_up = Stack()
        try:
            while True:
                if val not in seen:
                    seen.append(val)
                    for i in self.graph_dict[val][::-1]:
                        next_up.push(i)
                if len(next_up) == 0:
                    break
                val = next_up.pop().value
            return seen
        except KeyError:
            raise KeyError('Given value does not exist.')
    def breadth(self, val):
        from que_ import Queue
        seen = []
        next_up = Queue()
        try:
            while True:
                if val not in seen:
                    seen.append(val)
                    for i in self.graph_dict[val]:
                        next_up.enqueue(i)
                if next_up.size() == 0:
                    break
                val = next_up.dequeue().value
            return seen
        except KeyError:
            raise KeyError('Given value does not exist.')







if __name__ == '__main__':
    # graphy_mcgraphface = Graph()
    # graphy_mcgraphface.add_node("a node")
    # graphy_mcgraphface.add_node(5)
    # graphy_mcgraphface.add_node("sunshine and rainbows")
    # graphy_mcgraphface.add_edge("sunshine and rainbows", 5)
    # graphy_mcgraphface.add_node(6)
    # graphy_mcgraphface.add_node("Nodey mcnodeface")
    # graphy_mcgraphface.add_node("daisies")
    # graphy_mcgraphface.add_node('the dark abyss')
    # graphy_mcgraphface.add_node(1)
    # graphy_mcgraphface.add_edge(5, 6)
    # graphy_mcgraphface.add_edge(5, 7)
    # graphy_mcgraphface.add_edge(1, "sunshine and rainbows")
    # graphy_mcgraphface.add_edge("Nodey mcnodeface", 5)
    # graphy_mcgraphface.add_edge("Nodey mcnodeface", 66)
    # graphy_mcgraphface.add_edge("sunshine and rainbows", "the dark abyss")
    # graphy_mcgraphface.add_edge("the dark abyss", 7)
    # graphy_mcgraphface.add_edge(7, "Nodey mcnodeface")
    # graphy_mcgraphface.add_edge(2, 6)
    # graphy_mcgraphface.add_edge("the dark abyss", 2)
    # graphy_mcgraphface.add_edge(6, "a node")
    # graphy_mcgraphface.add_edge("a node", "hello")
    # graphy_mcgraphface.add_edge("Horse", 7)
    # graphy_mcgraphface.add_edge("Nodey mcnodeface", 1)
    # graphy_mcgraphface.add_edge("hello", "Horse")
    # # print(graphy_mcgraphface.graph_dict)
    # print(graphy_mcgraphface.edges())
    # print('---------------------')
    # print('depth: ', graphy_mcgraphface.depth(5))
    # print('breadth: ', graphy_mcgraphface.breadth(5))
    graphy_mcgraphface = Graph()
    graphy_mcgraphface.add_edge(1, 2)
    graphy_mcgraphface.add_edge(1, 3)
    graphy_mcgraphface.add_edge(2, 4)
    graphy_mcgraphface.add_edge(2, 5)
    graphy_mcgraphface.add_edge(3, 6)
    graphy_mcgraphface.add_edge(3, 7)
    graphy_mcgraphface.add_edge(4, 8)
    graphy_mcgraphface.add_edge(4, 9)
    graphy_mcgraphface.add_edge(5, 10)
    graphy_mcgraphface.add_edge(5, 11)
    graphy_mcgraphface.add_edge(6, 12)
    graphy_mcgraphface.add_edge(6, 13)
    graphy_mcgraphface.add_edge(7, 14)
    graphy_mcgraphface.add_edge(7, 15)
    # print(graphy_mcgraphface.graph_dict)
    print(graphy_mcgraphface.edges())
    print('---------------------')
    print('depth: ', graphy_mcgraphface.depth(1))
    print('breadth: ', graphy_mcgraphface.breadth(1))