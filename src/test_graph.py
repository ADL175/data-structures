"""Test definitions for the graph data structure."""

import pytest
import graph

PARAMS_TABLE_ADD_NODE = [
    ([1, 2, 3, 4, 5, 6]),
    (["A", False, "3"]),
    ([])
]

PARAMS_TABLE_HAS_NODE = [
    ([1, 2, 3, 4, 5, 6], 2, True),
    (["A", False, "3"], 5, False),
    ([], 4, False)
]

PARAMS_TABLE_ADD_EDGE = [
    ([1, 2, 58], [[2, 58]]),
    (["A", "B", 9], [["B", 9]])
]
PARAMS_TABLE_EDGES = [
    ([[1, 4, 8], [1, 2, 4], [4, 2, 3]])
]

PARAMS_TABLE_DEL_NODE = [
    ([1, 2, 3, 4, 5, 6], 3),
    (["A", False, "3"], 'A')
]

PARAMS_TABLE_DEL_EDGE = [
    ([1, 2, 3, 4, 5, 6], 3),
    (["A", False, "3"], 'A')
]


@pytest.mark.parametrize("data", PARAMS_TABLE_ADD_NODE)
def test_add_node(data):
    """Test the add_node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
        assert test_graph.graph_dict[val] == []


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_ADD_EDGE)
def test_add_edge(data, result_one):
    """Test the add_edge method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    test_graph.add_edge(data[0], data[1], data[2])
    assert test_graph.graph_dict[data[0]] == result_one


@pytest.mark.parametrize("data", PARAMS_TABLE_ADD_NODE)
def test_nodes(data):
    """Test the node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    assert len(test_graph.nodes()) == len(data)


@pytest.mark.parametrize("data", PARAMS_TABLE_EDGES)
def test_edges(data):
    """Test if list of edges is same as amount of data given."""
    test_graph = graph.Graph()
    for val in data:
        print(val)
        test_graph.add_edge(val[0], val[1], val[2])
    assert len(test_graph.edges()) == len(data)


def test_repeat_edges():
    """Test if error is raised when an edge is added that already exists."""
    test_graph = graph.Graph()
    test_graph.add_edge(2, 3, 5)
    with pytest.raises(KeyError):
        test_graph.add_edge(2, 3, 5)


@pytest.mark.parametrize("data, delete_me", PARAMS_TABLE_DEL_NODE)
def test_delete_node(data, delete_me):
    """Add a node, then delete it and test if it is still in graph."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    test_graph.del_node(delete_me)
    assert delete_me not in test_graph.nodes()


def test_delete_empty_node():
    """Test if error is raised when a node that is not in graph is removed."""
    test_graph = graph.Graph()
    with pytest.raises(KeyError):
        test_graph.del_node(2)


@pytest.mark.parametrize("data, delete_me", PARAMS_TABLE_DEL_EDGE)
def test_delete_edge(data, delete_me):
    """Add an edge, then delete it and test if it is still in graph."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    test_graph.del_node(delete_me)
    assert delete_me not in test_graph.nodes()


def test_delete_empty_edge():
    """Test if error is raised when an edge that is not in graph is removed."""
    test_graph = graph.Graph()
    with pytest.raises(KeyError):
        test_graph.del_edge(2, 3)


@pytest.mark.parametrize("data, search, result", PARAMS_TABLE_HAS_NODE)
def test_has_node(data, search, result):
    """Test the has_node method, returns boolean."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    assert test_graph.has_node(search) == result


def test_neighbors():
    """Test if the neighbors method returns list of neighbor."""
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C', 1)
    test_graph.add_edge('A', 'B', -4)
    test_graph.add_edge('B', 'A', -5)
    test_graph.add_edge('A', 'D', 6)
    test_graph.add_edge('C', 'E', 1)
    test_graph.add_edge('E', 'C', 1)
    test_graph.add_edge('E', 'B', 1)
    test_graph.add_edge('B', 'D', 1)
    test_graph.add_edge('B', 'F', 1)
    test_graph.add_edge('F', 'D', 10)
    assert test_graph.neighbors("A") == [['C', 1], ['B', -4], ['D', 6]]


def test_no_neighbors():
    """Test if neighbors function raises error if given a value not in graph."""
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C', 1)
    test_graph.add_edge('A', 'B', -4)
    with pytest.raises(KeyError):
        test_graph.neighbors(2)


def test_adjacent():
    """Test adjacent method return boolean and key error for non existent node."""
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C', 1)
    test_graph.add_edge('A', 'B', -4)
    test_graph.add_edge('B', 'A', -5)
    test_graph.add_edge('A', 'D', 6)
    test_graph.add_edge('C', 'E', 1)
    test_graph.add_edge('E', 'C', 1)
    test_graph.add_edge('E', 'B', 1)
    test_graph.add_edge('B', 'F', 1)
    test_graph.add_edge('F', 'D', 10)
    assert test_graph.adjacent("A", "C") is True
    assert test_graph.adjacent("B", "D") is False
    with pytest.raises(KeyError):
        test_graph.adjacent("A", "Z")
    with pytest.raises(KeyError):
        test_graph.adjacent("Z", "A")


def test_depth_breadth_traversal():
    """Test both depth and breadth traversal, returns list."""
    test_graph = graph.Graph()
    test_graph.add_edge(0, 1, 1)
    test_graph.add_edge(0, 2, 4)
    test_graph.add_edge(1, 3, 5)
    test_graph.add_edge(1, 4, 6)
    test_graph.add_edge(2, 5, 1)
    test_graph.add_edge(2, 6, 1)
    test_graph.add_edge(3, 7, 1)
    test_graph.add_edge(3, 8, 1)
    test_graph.add_edge(4, 9, 10)
    test_graph.add_edge(4, 10, 10)
    test_graph.add_edge(5, 11, 10)
    test_graph.add_edge(5, 12, 10)
    test_graph.add_edge(6, 13, 10)
    test_graph.add_edge(6, 14, 10)
    assert test_graph.breadth_first_traversal(0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert test_graph.depth_first_traversal(0) == [0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14]


def test_depth_breadth_traversal_with_improper_value():
    """Test both depth and breadth traversal, expecting error if improper starting point."""
    test_graph = graph.Graph()
    test_graph.add_edge(0, 1, 1)
    test_graph.add_edge(0, 2, 4)
    with pytest.raises(KeyError):
        test_graph.breadth_first_traversal(5)
    with pytest.raises(KeyError):
        test_graph.depth_first_traversal(5)


def test_dijkstra_and_bellman_ford():
    """Test if both algorithms return the correct answer to a shortest path problem."""
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C', 1)
    test_graph.add_edge('A', 'B', 4)
    test_graph.add_edge('B', 'A', 5)
    test_graph.add_edge('A', 'D', 6)
    test_graph.add_edge('C', 'E', 1)
    test_graph.add_edge('E', 'C', 1)
    test_graph.add_edge('E', 'B', 1)
    test_graph.add_edge('B', 'D', 1)
    test_graph.add_edge('B', 'F', 1)
    test_graph.add_edge('F', 'D', 10)
    assert test_graph.dijkstra('A', 'D') == [4, ['A', 'C', 'E', 'B', 'D']]
    assert test_graph.bellman_ford('A', 'D') == [4, ['A', 'C', 'E', 'B', 'D']]


def test_bellman_ford_negative_weights():
    """Test if Bellman Ford algorithm raises an error for a negative value loop.

    Not done for Dijkstra, as that is not an explicit part of Dijkstra's algorithm.
    """
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C', 1)
    test_graph.add_edge('A', 'B', -4)
    test_graph.add_edge('B', 'A', -5)
    test_graph.add_edge('A', 'D', 6)
    test_graph.add_edge('C', 'E', 1)
    test_graph.add_edge('E', 'C', 1)
    test_graph.add_edge('E', 'B', 1)
    test_graph.add_edge('B', 'D', 1)
    test_graph.add_edge('B', 'F', 1)
    test_graph.add_edge('F', 'D', 10)
    with pytest.raises(ValueError):
        test_graph.bellman_ford('A', 'D')
