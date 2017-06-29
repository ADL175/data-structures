"""Test definitions for doubly que_."""

import pytest
import que_

PARAMS_TABLE_LIST = [
    ([1, 2, 3, 4, 5], 1, 5),
    ([5, 4, 3, 2, 1], 5, 1),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "whisky", "quebec"),
    ([False, 2, True, "alpha", [1, 2, 3]], False, [1, 2, 3])
]


PARAMS_TABLE_POP = [
    ([1, 2, 3, 4, 5], 1, 2),
    ([5, 4, 3, 2, 1], 5, 4),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "whisky", "tango"),
    ([False, 2, True, "alpha", [1, 2, 3]], False, 2)
]

PARAMS_TABLE_PEEK = [
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 5),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "whisky"),
    ([False, 2, True, "alpha", [1, 2, 3]], False)
]

PARAMS_TABLE_SIZE = [
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3)
]

PARAMS_TABLE_ITERABLES = [
    ([1,2,3], 3),
    ((1,2,3), 3),
    ({1:1, 2:2, 3:3}, 0)
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_list(data, result_one, result_two):
    """Ensure proper assignment."""
    test_list = que_.Queue(data)
    assert test_list.head.value == result_one
    assert test_list.tail.value == result_two


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_ITERABLES)
def test_list_iterables(data, result_one):
    """Ensure enque only takes list or tuples."""
    test_list = que_.Queue(data)
    assert len(test_list) == result_one



@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_enqueue(data, result_one, result_two):
    """Test the enqueue method."""
    test_list = que_.Queue()
    for i in data:
        test_list.enqueue(i)
    assert test_list.head.value == result_one
    assert test_list.tail.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_POP)
def test_dequeue(data, result_one, result_two):
    """Test the dequeue method."""
    test_list = que_.Queue(data)
    assert test_list.dequeue() == result_one
    assert test_list.dequeue() == result_two

def test_dequeue_empty():
    """Test to ensure dequeue function returns an index error when the list is empty."""
    test_list = que_.Queue()
    with pytest.raises(IndexError):
        test_list.dequeue()


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_PEEK)
def test_peek(data, result_one):
    """Test the peek method."""
    test_list = que_.Queue(data)
    assert test_list.peek() == result_one


@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_size(data, result):
    """Test if list size is properly incremented."""
    test_list = que_.Queue(data)
    assert test_list.size() == result
    test_list.enqueue("test_push")
    assert test_list.size() == result + 1
    test_list.dequeue()
    assert test_list.size() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_len(data, result):
    """Test if list len is properly incremented."""
    test_list = que_.Queue(data)
    assert test_list.__len__() == result
    test_list.enqueue("test_push")
    assert test_list.__len__() == result + 1
    test_list.dequeue()
    assert test_list.__len__() == result
