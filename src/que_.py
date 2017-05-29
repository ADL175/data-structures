import sys


class Node(object):
    """Creates a Node."""
    def __init__(self, value, next_up=None):
        self.value = value
        self.next = next_up
        self.behind = None


class Queue(object):
    """Creates a Queue from value or list."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        """Adds node to end of queue."""
        self.tail = Node(value, self.tail)
        if self.length == 0:
            self.head = self.tail
        if self.tail.next is not None:
            self.tail.next.behind = self.tail
        self.length += 1

    def dequeue(self):
        """Removes node from head of queue."""
        if self.head is None:
            return "Queue is empty."
        head = self.head
        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            self.head.behind.next = None
            self.head = self.head.behind
        self.length -= 1
        return head

    def peek(self):
        """Return value of head."""
        if self.head is None:
            return "Queue is empty."
        return self.head.value

    def size(self):
        """Returns length of queue."""
        return self.length

    def __len__(self):
        """Returns length of queue."""
        return self.size()

new_queue = Queue()

new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)
new_queue.size()
# new_queue.size()
# new_queue.dequeue()
# new_queue.size()
# new_queue.peek()
