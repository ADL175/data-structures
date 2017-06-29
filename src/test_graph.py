"""Test definitions for tje graph data structure."""

import pytest
import graph

PARAMS_TABLE_ADD_NODE = [
    ([1, 2, 3, 4, 5, 6]),
    (["A", False, "3"]),
    ([])
]

PARAMS_TABLE_ADD_EDGE = [
    ([1, 2, 58], [[2, 58]]),
    (["A", "B", 9], [["B", 9]])
]
PARAMS_TABLE_EDGES = [
    ([1, 2, 58]),
    (["A", "B", 9])
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
    """Test the add_node method."""
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
    """Test the node method."""
    test_graph = graph.Graph()
    for val in data:
        print(val)
        test_graph.add_edge(data[0], data[1], data[2])
    assert len(test_graph.edges()) == len(data)


@pytest.mark.parametrize("data, delete_me", PARAMS_TABLE_DEL_NODE)
def test_delete_node(data, delete_me):
    """Test the add_node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    test_graph.del_node(delete_me)
    assert delete_me not in test_graph.nodes()

@pytest.mark.parametrize("data, delete_me", PARAMS_TABLE_DEL_EDGE)
def test_delete_edge(data, delete_me):
    """Test the add_node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    test_graph.del_node(delete_me)
    assert delete_me not in test_graph.nodes()
