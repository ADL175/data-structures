"""Test definitions for PQ."""

import pytest
import priorityq

PARAMS_TABLE_INSERT = [
    ([[1, 2], [3, 4], [5, 6]], 5, 3),
    ([["potato", 21], ["shoe", 45], ["poo", 66]], "poo", "shoe"),
    ([["poop", 2], ["3", "string"], ["tree", 69]], "tree", "poop")
]

PARAMS_TABLE_POP = [
    ([[1, 2], [3, 4], [5, 6]], [5, 3, 1]),
    ([["potato", 21], ["shoe", 45], ["poo", 66]], ["poo", "shoe", "potato"]),
    ([["poop", 2], ["3", "string"], ["tree", 69]], ["tree", "poop", "3"])
]

PARAMS_TABLE_PEEK = [
    ([[1, 2], [3, 4], [5, 6]], {"value": 5,
                                "priority": 6}),
    ([["potato", 21], ["shoe", 45], ["poo", 66]], {"value": "poo",
                                                   "priority": 66}),
    ([["poop", 2], ["3", "string"], ["tree", 69]], {"value": "tree",
                                                    "priority": 69})
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_INSERT)
def test_insert(data, result_one, result_two):
    """Test the insert method."""
    new_PQ = priorityq.Priority_Q()
    for i in data:
        new_PQ.insert(i[0], i[1])
    assert new_PQ.heap.heap[0]['value'] == result_one
    assert new_PQ.heap.heap[-1]['value'] == result_two


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_POP)
def test_pop(data, result_one):
    """Test the pop method."""
    new_list = []
    new_PQ = priorityq.Priority_Q()
    for i in data:
        new_PQ.insert(i[0], i[1])
    for i in range(3):
        new_list.append(new_PQ.pop())
    assert new_list == result_one


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_PEEK)
def test_peek(data, result_one):
    """Test the peek method."""
    new_PQ = priorityq.Priority_Q()
    for i in data:
        new_PQ.insert(i[0], i[1])
    assert new_PQ.peek() == result_one
