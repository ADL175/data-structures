"""Tests for the linked list data structure."""
import pytest
import linked_list

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
    ([1, 3, 4, 5, 6], 2, None),
    ([1, 2], 3, None)
]

PARAMS_TABLE_REMOVE = [
    (1, 2, 3, 4, 4, 2),
    (2, 3, 4, 5, 5, 3),
    (3, 3, 3, 3, 3, 3)
]
PARAMS_TABLE_DISPLAY = [
    ([], '()'),
    ([1], '(1)'),
    ([1, 2], '(2, 1)'),
    ([1, 2, 3], '(3, 2, 1)')
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_list(data, result_one, result_two):
    """Test to ensure iterable insertion functionality works properly."""
    test_list = linked_list.Linked_List(data)
    assert test_list.head.value == result_one
    assert test_list.head.next.next.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_push(data, result_one, result_two):
    """Test to ensure push function works properly."""
    test_list = linked_list.Linked_List()
    for i in data:
        test_list.push(i)
    assert test_list.head.value == result_one
    assert test_list.head.next.next.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_POP)
def test_pop(data, result_one, result_two):
    """Test to ensure pop function works properly."""
    test_list = linked_list.Linked_List(data)
    assert test_list.pop() == result_one
    assert test_list.pop() == result_two


def test_pop_empty():
    """Test to ensure pop function returns an index error when the list is empty."""
    test_list = linked_list.Linked_List()
    with pytest.raises(IndexError):
        test_list.pop()

@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_size(data, result):
    """Test to ensure size function works properly."""
    test_list = linked_list.Linked_List(data)
    assert test_list.size() == result
    assert len(test_list) == result
    test_list.push("test_push")
    assert test_list.size() == result + 1
    assert len(test_list) == result + 1
    test_list.pop()
    assert test_list.size() == result
    assert len(test_list) == result

@pytest.mark.parametrize("data, search_me, result", PARAMS_TABLE_SEARCH_THERE)
def test_search_where_it_is_there(data, search_me, result):
    """Test to ensure search function works properly when requested node is in list."""
    test_list = linked_list.Linked_List(data)
    assert test_list.search(search_me).value == result


@pytest.mark.parametrize("data, search_me, result", PARAMS_TABLE_SEARCH_NOT_THERE)
def test_search_where_it_is_not_there(data, search_me, result):
    """Test to ensure search function works properly when requested node is not in list."""
    test_list = linked_list.Linked_List(data)
    assert test_list.search(search_me) == result


@pytest.mark.parametrize("a,b,c,d,result_head, result_next", PARAMS_TABLE_REMOVE)
def test_remove(a, b, c, d, result_head, result_next):
    """Test to ensure remove function works properly when requested node is in list."""
    test_list = linked_list.Linked_List()
    test_list.push(a)
    test_list.push(b)
    test_list.push(c)
    remove_me = test_list.head
    test_list.push(d)
    test_list.remove(remove_me)
    assert test_list.head.next.value == result_next
    assert test_list.head.value == result_head


def test_remove_not_there():
    """Test to ensure remove function works properly when requested node is not in list."""
    test_list = linked_list.Linked_List()
    test_list.push('removed_node')
    removed_node = test_list.head
    test_list.pop()
    with pytest.raises(IndexError):
        test_list.remove(removed_node)


def test_remove_wrong_type():
    """Test to ensure remove function works properly when requested node is not a node."""
    test_list = linked_list.Linked_List()
    with pytest.raises(TypeError):
        test_list.remove("removed_node")


@pytest.mark.parametrize("data, result", PARAMS_TABLE_DISPLAY)
def test_display(data, result):
    """Test to ensure display function works properly."""
    test_list = linked_list.Linked_List(data)
    assert test_list.display() == result
