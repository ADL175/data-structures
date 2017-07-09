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
    ([1, 2], [2]),
    (["A", "B"], ["B"])
]
PARAMS_TABLE_EDGES = [
    ([[1, 4], [1, 2], [4, 2]])
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
    test_graph.add_edge(data[0], data[1])
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
        test_graph.add_edge(val[0], val[1])
    assert len(test_graph.edges()) == len(data)


def test_repeat_edges():
    """Test if error is raised when an edge is added that already exists."""
    test_graph = graph.Graph()
    test_graph.add_edge(2, 3)
    with pytest.raises(KeyError):
        test_graph.add_edge(2, 3)


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
    test_graph.add_edge('A', 'C')
    test_graph.add_edge('A', 'B')
    test_graph.add_edge('B', 'A')
    test_graph.add_edge('A', 'D')
    test_graph.add_edge('C', 'E')
    test_graph.add_edge('E', 'C')
    test_graph.add_edge('E', 'B')
    test_graph.add_edge('B', 'D')
    test_graph.add_edge('B', 'F')
    test_graph.add_edge('F', 'D')
    assert test_graph.neighbors("A") == ['C', 'B', 'D']


def test_no_neighbors():
    """Test if neighbors function raises error if given a value not in graph."""
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C')
    test_graph.add_edge('A', 'B')
    with pytest.raises(KeyError):
        test_graph.neighbors(2)


def test_adjacent():
    """Test adjacent method return boolean and key error for non existent node."""
    test_graph = graph.Graph()
    test_graph.add_edge('A', 'C')
    test_graph.add_edge('A', 'B')
    test_graph.add_edge('B', 'A')
    test_graph.add_edge('A', 'D')
    test_graph.add_edge('C', 'E')
    test_graph.add_edge('E', 'C')
    test_graph.add_edge('E', 'B')
    test_graph.add_edge('B', 'F')
    test_graph.add_edge('F', 'D')
    assert test_graph.adjacent("A", "C") is True
    assert test_graph.adjacent("B", "D") is False
    with pytest.raises(KeyError):
        test_graph.adjacent("A", "Z")
    with pytest.raises(KeyError):
        test_graph.adjacent("Z", "A")

