"""Implement Priority Queue."""

from priority_heap import Priority_Heap

class Priority_Q():
    def __init__(self):
        self.heap = Priority_Heap()

    def pop(self):
        """Removes and returns head with highest priority."""
        if len(self.heap.heap) > 0:
            return self.heap.pop()
        else:
            return None

    def insert(self, value, neighbors, priority=float('inf')):
        """Inserts value into PriorityQ."""
        new_item = {'value': value,
                    'dist': priority,
                    'prev': None,
                    'neighbors': neighbors}
        self.heap.push(new_item)

    def peek(self):
        """Returns value of highest priority item."""
        return self.heap.heap[0]
    def decrease_priority(self, value, new_priority, prev):
        for node in self.heap.heap:
            if node['value'] == value:
                if node['dist'] > new_priority:
                    self.heap.heap.remove(node)      
                    new_item = {
                        'value': value,
                        'dist': new_priority,
                        'prev': prev,
                        'neighbors': node['neighbors']
                    }
                    self.heap.push(new_item)

if __name__ == '__main__':
    new_PQ = Priority_Q()
    new_PQ.insert(1, 2)
    new_PQ.insert('poo', 20)
    new_PQ.insert('shoe', 245)
    new_PQ.insert('zoo', 77)
    new_PQ.insert('palasd', 'asdf')
    new_PQ.decrease_priority('zoo', 1)
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
    print(new_PQ.pop())
