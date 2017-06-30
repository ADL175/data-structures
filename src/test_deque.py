"""Test definitions for deque."""


import pytest
import deque

PARAMS_TABLE_LIST = [
    ([1, 2, 3, 4, 5], 5, 1),
    ([5, 4, 3, 2, 1], 1, 5),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "quebec", "whisky"),
    ([False, 2, True, "alpha", [1, 2, 3]], [1, 2, 3], False)
]

PARAMS_TABLE_LIST_REV = [
    ([1, 2, 3, 4, 5], 1, 5),
    ([5, 4, 3, 2, 1], 5, 1),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "whisky", "quebec"),
    ([False, 2, True, "alpha", [1, 2, 3]], False, [1, 2, 3])
]

PARAMS_TABLE_POP = [
    ([1, 2, 3, 4, 5], 5, 4),
    ([5, 4, 3, 2, 1], 1, 2),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "quebec", "bravo"),
    ([False, 2, True, "alpha", [1, 2, 3]], [1, 2, 3], "alpha")
]

PARAMS_TABLE_POP_REV = [
    ([1, 2, 3, 4, 5], 1, 2),
    ([5, 4, 3, 2, 1], 5, 4),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "whisky", "tango"),
    ([False, 2, True, "alpha", [1, 2, 3]], False, 2)
]


PARAMS_TABLE_PEEK_BACK = [
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 5),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "whisky"),
    ([False, 2, True, "alpha", [1, 2, 3]], False)
]

PARAMS_TABLE_PEEK = [
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 1),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "quebec"),
    ([False, 2, True, "alpha", [1, 2, 3]], [1, 2, 3])
]

PARAMS_TABLE_SIZE = [
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3)
]

PARAMS_TABLE_SEARCH_THERE = [
    ([1, 2, 3, 4, 5], 5, 5),
    ([1, 1, 1, 1, 1], 1, 1)
]

PARAMS_TABLE_SEARCH_NOT_THERE = [
    ([1, 3, 4, 5, 6], 2, "haha, nothing here"),
    ([1, 2], 3, "haha, nothing here")
]

PARAMS_TABLE_REMOVE = [
    ([1, 17, 2, 3, 4, 2], 4, 17),
    ([2, 18, 3, 4, 5, 3], 5, 18),
    ([3, 3, 3, 3, 3, 3], 3, 3)
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_list(data, result_one, result_two):
    """Ensure proper assignment."""
    test_list = deque.Deque(data)
    assert test_list.head.value == result_one
    assert test_list.tail.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_add_first(data, result_one, result_two):
    """Test the add_first method."""
    test_list = deque.Deque()
    for i in data:
        test_list.add_first(i)
    assert test_list.head.value == result_one
    assert test_list.tail.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST_REV)
def test_add_last(data, result_one, result_two):
    """Test the add_last method."""
    test_list = deque.Deque()
    for i in data:
        test_list.add_last(i)
    assert test_list.head.value == result_one
    assert test_list.tail.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_POP)
def test_delete_first(data, result_one, result_two):
    """Test the delete_first method."""
    test_list = deque.Deque(data)
    assert test_list.delete_first().value == result_one
    assert test_list.delete_first().value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_POP_REV)
def test_delete_last(data, result_one, result_two):
    """Test the delete_last method."""
    test_list = deque.Deque(data)
    assert test_list.delete_last().value == result_one
    assert test_list.delete_last().value == result_two


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_PEEK_BACK)
def test_peek_back(data, result_one):
    """Test the peek_back method."""
    test_list = deque.Deque(data)
    assert test_list.peek_back() == result_one


@pytest.mark.parametrize("data, result_one", PARAMS_TABLE_PEEK)
def test_peek(data, result_one):
    """Test the peek method."""
    test_list = deque.Deque(data)
    assert test_list.peek() == result_one


@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_size(data, result):
    """Test if list size is properly incremented."""
    test_list = deque.Deque(data)
    assert test_list.size() == result
    test_list.add_first("test_push")
    assert test_list.size() == result + 1
    test_list.delete_first()
    assert test_list.size() == result


@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_len(data, result):
    """Test if list __len__ is properly incremented."""
    test_list = deque.Deque(data)
    assert test_list.__len__() == result
    test_list.add_first("test_push")
    assert test_list.__len__() == result + 1
    test_list.delete_first()
    assert test_list.__len__() == result
