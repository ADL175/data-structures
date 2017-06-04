"""Implement Priority Queue."""

from priority_heap import Priority_Heap

class Priority_Q():
    def __init__(self):
        self.heap = Priority_Heap()

    def pop(self):
        """Removes and returns head with highest priority."""
        if len(self.heap.heap) > 0:
            return self.heap.pop()['value']
        else:
            return None

    def insert(self, value, priority=0):
        """Inserts value into PriorityQ."""
        if isinstance(priority, int) is False:
            priority = 0
        new_item = {'value': value,
                    'priority': priority}
        self.heap.push(new_item)

    def peek(self):
        """Returns value of highest priority item."""
        return self.heap[0]


if __name__ == '__main__':
    new_PQ = Priority_Q()
    new_PQ.insert(1,2)
    new_PQ.insert('poo',20)
    new_PQ.insert('shoe',245)
    new_PQ.insert('zoo',77)
    new_PQ.insert('palasd', 'asdf')
    new_PQ.insert('zoo', 'sdfasdfasdfsdf')
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    # print(new_heap.pop())
    # print(new_heap.pop())
    # print(new_heap.pop())
    # print(new_heap.pop())
    # print(new_heap.pop())
    # print(new_heap.pop())
