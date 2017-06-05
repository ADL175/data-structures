"""Test definitions for PQ."""

import pytest
import graph

PARAMS_TABLE_ADD_NODE = [
    ([1, 2, 3, 4, 5, 6]),
    (["poop", False, "3"])
]

PARAMS_TABLE_ADD_EDGE = [
    ([1, 2], [2]),
    (["poop", "soup"], ["soup"])
]

@pytest.mark.parametrize("data", PARAMS_TABLE_ADD_NODE)
def test_add_node(data):
    """Test the add_node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
        assert test_graph.graph_dict[val] == []


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_ADD_EDGE)
def test_add_node(data, result_one):
    """Test the add_node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    test_graph.add_edge(data[0], data[1])
    assert test_graph.graph_dict[data[0]] == result_one


@pytest.mark.parametrize("data", PARAMS_TABLE_ADD_NODE)
def test_node(data):
    """Test the node method."""
    test_graph = graph.Graph()
    for val in data:
        test_graph.add_node(val)
    assert test_graph.nodes() == data
