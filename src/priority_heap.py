"""Max / PRIORITY Heapy mcheap."""


class Priority_Heap():
    """A heap."""
    def __init__(self):
        """Initialize a heap."""
        self.heap = []

    def push(self, item):
        """Add value to heap."""
        if isinstance(item['priority'], int):
            self.heap.append(item)
            current = self.heap[-1]
            if self.heap.index(current) == 0:
                return
            elif self.heap.index(current) % 2 == 0:
                parent = self.heap[int((self.heap.index(current) - 2) / 2)]
            else:
                parent = self.heap[int((self.heap.index(current) - 1) / 2)]
            while current['priority'] > parent['priority']:
                self.heap[self.heap.index(current)], self.heap[self.heap.index(parent)] = self.heap[self.heap.index(parent)], self.heap[self.heap.index(current)]
                if self.heap.index(current) == 0:
                    break
                elif self.heap.index(current) % 2 == 0:
                    parent = self.heap[int((self.heap.index(current) - 2) / 2)]
                else:
                    parent = self.heap[int((self.heap.index(current) - 1) / 2)]


    def pop(self):
        """Remove top of heap."""
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        to_remove = self.heap.pop()
        try:
            current = self.heap[0]
        except IndexError:
            return None
        try:
            child_one = self.heap[int((self.heap.index(current) * 2) + 1)]
        except IndexError:
            child_one = {'priority': current['priority']-1}
            # current['priority'] - 1
        try:
            child_two = self.heap[int((self.heap.index(current) * 2) + 2)]
        except IndexError:
            child_two = {'priority': current['priority']-1}
            # current['priority'] - 1
        temp = [current, child_one, child_two]
        temp = sorted(temp, key=lambda k: k['priority'])
        # print(temp)
        while temp[-1] is not current:
            self.heap[self.heap.index(temp[-1])], self.heap[self.heap.index(current)] = self.heap[self.heap.index(current)], self.heap[self.heap.index(temp[-1])]
            try:
                child_one = self.heap[int((self.heap.index(current) * 2) + 1)]
            except IndexError:
                child_one = {'priority': current['priority']-1}
            try:
                child_two = self.heap[int((self.heap.index(current) * 2) + 2)]
            except IndexError:
                child_two = {'priority': current['priority']-1}
            temp = [current, child_one, child_two]
            temp = sorted(temp, key=lambda k: k['priority'])
        return to_remove
