import sys


class Node(object):
    """Creates a Node."""
    def __init__(self, value, next_up=None, behind=None):
        self.value = value
        self.next = next_up
        self.behind = behind


class Deque(object):
    """Creates a Deque from value or list."""
    def __init__(self, optional_values=[]):
        self.head = None
        self.tail = None
        self.length = 0
        self.is_empty = True
        for x in optional_values:
            self.add_first(x)

    def add_last(self, value):
        """Adds node to end of queue."""
        self.tail = Node(value, self.tail)
        if self.length == 0:
            self.head = self.tail
        if self.tail.next is not None:
            self.tail.next.behind = self.tail
        if self.is_empty is True:
            self.is_empty = False
        self.length += 1

    def add_first(self, value):
        """Adds node to head or start of queue."""
        self.head = Node(value, None, self.head)
        if self.length == 0:
            self.tail = self.head
        if self.head.behind is not None:
            self.head.behind.next = self.head
        if self.is_empty is True:
            self.is_empty = False
        self.length += 1

    def delete_last(self):
        """Removes node from tail of queue."""
        if self.tail is None:
            return "Queue is empty."
        tail = self.tail
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail.next.behind = None
            self.tail = self.tail.next
        self.length -= 1
        if self.length == 0:
            self.is_empty = True
        return tail

    def delete_first(self):
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
        if self.length == 0:
            self.is_empty = True
        return head

    # def clear():

    def peek(self):
        """Return value of head."""
        if self.head is None:
            return "Queue is empty."
        return self.head.value

    def peek_back(self):
        """Return value of head."""
        if self.tail is None:
            return "Queue is empty."
        return self.tail.value

    def size(self):
        """Returns length of queue."""
        return self.length

    def __len__(self):
        """Returns length of queue."""
        return self.size()
