import pytest
import binheap



PARAMS_TABLE_HEAP = [
    ([1, 2, 3, 4, 5], 1, 2),
    ([5, 4, 3, 2, 1], 1, 2),
    ([1, 1], 1, 1),
    ([], None, None),
    (['1', 'smile'], None, None),
    ([54, 23, 876, 444444, 3], 3, 23)
]


@pytest.mark.parametrize("data, result_one, result_two", PARAMS_TABLE_HEAP)
def test_list(data, result_one, result_two):
    """Ensure proper assignment."""
    test_heap = binheap.Binary_Heap()
    for i in data:
        test_heap.push(i)
    assert test_heap.pop() == result_one
    assert test_heap.pop() == result_two

