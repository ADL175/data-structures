"""Test module for Stack."""


import pytest
import stack

PARAMS_TABLE_LIST = [
    ([1, 2, 3, 4, 5], 5, 3),
    ([5, 4, 3, 2, 1], 1, 3),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "quebec", "bravo"),
    ([False, 2, True, "alpha", [1, 2, 3]], [1, 2, 3], True)
]


PARAMS_TABLE_POP = [
    ([1, 2, 3, 4, 5], 5, 4),
    ([5, 4, 3, 2, 1], 1, 2),
    (["whisky", "tango", "foxtrot", "bravo", "bravo", "quebec"], "quebec", "bravo"),
    ([False, 2, True, "alpha", [1, 2, 3]], [1, 2, 3], "alpha")
]

PARAMS_TABLE_PUSH_N_POP = [
    (2, 2),
    (5, 5),
    (True, True),
    ("string", "string"),
    ([1, 2, 3], [1, 2, 3])
]

PARAMS_TABLE_LEN = [
    ([1, 2]),
    ([i for i in range(100)]),
    ([]),
    ([False, 2, True, "alpha", [1, 2, 3]])
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_stack(data, result_one, result_two):
    """Test if it's properly being assigned."""
    test_stack = stack.Stack(data)
    assert test_stack._new_linked_list.head.value == result_one
    assert test_stack._new_linked_list.head.next.next.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_push(data, result_one, result_two):
    """Test if the pushed value is the correct one."""
    test_stack = stack.Stack()
    for i in data:
        test_stack.push(i)
    assert test_stack._new_linked_list.head.value == result_one
    assert test_stack._new_linked_list.head.next.next.value == result_two


@pytest.mark.parametrize("data, result", PARAMS_TABLE_PUSH_N_POP)
def test_push_and_pop(data, result):
    """Test push and pop value is the same one."""
    test_stack = stack.Stack()
    test_stack.push(data)
    assert test_stack.pop() == result


def test_pop_empty_stack():
    """Test if pop raises an error when stack is empty."""
    test_stack = stack.Stack()
    with pytest.raises(IndexError):
        test_stack.pop()


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_POP)
def test_pop(data, result_one, result_two):
    """Test if the popped value is the predicted value."""
    test_stack = stack.Stack(data)
    assert test_stack.pop() == result_one
    assert test_stack.pop() == result_two


@pytest.mark.parametrize("data", PARAMS_TABLE_LEN)
def test_len(data):
    """Test if it's properly being assigned."""
    test_stack = stack.Stack(data)
    assert len(test_stack) == len(data)
