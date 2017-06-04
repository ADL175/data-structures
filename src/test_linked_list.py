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
    ([1, 3, 4, 5, 6], 2, "haha, nothing here"),
    ([1, 2], 3, "haha, nothing here")
]

PARAMS_TABLE_REMOVE = [
    (1, 2, 3, 4, 4, 2),
    (2, 3, 4, 5, 5, 3),
    (3, 3, 3, 3, 3, 3)
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_list(data, result_one, result_two):
    test_list = linked_list.Linked_List(data)
    assert test_list.head.value == result_one
    assert test_list.head.next.next.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_LIST)
def test_push(data, result_one, result_two):
    test_list = linked_list.Linked_List()
    for i in data:
        test_list.push(i)
    assert test_list.head.value == result_one
    assert test_list.head.next.next.value == result_two


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_POP)
def test_pop(data, result_one, result_two):
    test_list = linked_list.Linked_List(data)
    assert test_list.pop().value == result_one
    assert test_list.pop().value == result_two



@pytest.mark.parametrize("data, result", PARAMS_TABLE_SIZE)
def test_size(data, result):
    test_list = linked_list.Linked_List(data)
    assert test_list.size() == result
    test_list.push("test_push")
    assert test_list.size() == result + 1
    test_list.pop()
    assert test_list.size() == result



@pytest.mark.parametrize("data, search_me, result", PARAMS_TABLE_SEARCH_THERE)
def test_search_where_it_is_there(data, search_me, result):
    test_list = linked_list.Linked_List(data)
    assert test_list.search(search_me).value == result


@pytest.mark.parametrize("data, search_me, result", PARAMS_TABLE_SEARCH_NOT_THERE)
def test_search_where_it_is_not_there(data, search_me, result):
    test_list = linked_list.Linked_List(data)
    assert test_list.search(search_me) == result


@pytest.mark.parametrize("a,b,c,d,result_head, result_next", PARAMS_TABLE_REMOVE)
def test_remove(a, b, c, d, result_head, result_next):
    test_list = linked_list.Linked_List()
    test_list.push(a)
    test_list.push(b)
    test_list.push(c)
    remove_me = test_list.head
    test_list.push(d)
    test_list.remove(remove_me)
    assert test_list.head.next.value == result_next
    assert test_list.head.value == result_head
