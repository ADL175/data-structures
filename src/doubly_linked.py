<<<<<<< HEAD
import sys


class Node(object):

    def __init__(self, value, next_up=None, behind=None):
=======
"""Implement the Node class and Double Linked_List class."""


class Node(object):
    """Creates sub class of Node."""

    def __init__(self, value, next_up=None, behind=None):
        """Set up Node."""
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        self.value = value
        self.next = next_up
        self.behind = behind


<<<<<<< HEAD
class Linked_List(object):

    def __init__(self, optional_values=[]):
=======
class Double_Linked_List(object):
    """Create a doubly linked list."""

    def __init__(self, optional_values=[]):
        """Initialize the class instance."""
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        self.head = None
        self.tail = None
        self.length = 0
        for x in optional_values:
            self.push(x)

    def push(self, value):
<<<<<<< HEAD
=======
        """Add new Head to head of DLL."""
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        self.head = Node(value, self.head)
        if self.length == 0:
            self.tail = self.head
        self.length += 1
        if self.head.next is not None:
            self.head.next.behind = self.head

    def append(self, value):
<<<<<<< HEAD
=======
        """Add new node to tail of DLL."""
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        self.tail = Node(value, None, self.tail)
        if self.length == 0:
            self.head = self.tail
        self.length += 1
        if self.tail.behind is not None:
            self.tail.behind.next = self.tail

    def pop(self):
<<<<<<< HEAD
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        self.head.behind = None
        return popped

    def shift(self):
        shifted = self.tail
        self.tail = self.tail.behind
        self.length -= 1
        self.tail.next = None
        return shifted

    def size(self):
        return self.length

    def search(self, val):
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return "haha, nothing here"
        return temp

    def remove(self, val):
=======
        """Pop the specific node, assign it's next to head, and return popped node."""
        if self.length is 0:
            raise IndexError('List is empty.')
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        if self.head:
            self.head.behind = None
        return popped.value

    def shift(self):
        """Remove and returns tailnode."""
        if self.length is 0:
            raise IndexError('List is empty.')
        shifted = self.tail
        self.tail = self.tail.behind
        self.length -= 1
        if self.tail:
            self.tail.next = None
        return shifted.value

    def size(self):
        """Return length of DLL."""
        return self.length

    def remove(self, val):
        """Remove a specific node from DLL."""
        if self.length is 0:
            raise IndexError('List is empty.')
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        if self.head.value is val:
            self.head = self.head.next
            self.head.behind = None
            self.length -= 1
        current_node = self.head
        while current_node:
<<<<<<< HEAD
            if current_node.next.value is val:
                if current_node.next is self.tail:
                    self.tail = self.tail.behind
                    self.tail.next = None
                    self.length -= 1
                    return
                else:
                    self.length -= 1
                    current_node.next = current_node.next.next
                    current_node.next.behind = current_node
                    return
            if current_node is None:
                return "haha, nothing to delete"
            current_node = current_node.next
=======
            try:
                if current_node.next.value is val:
                    if current_node.next is self.tail:
                        self.tail = self.tail.behind
                        self.tail.next = None
                        self.length -= 1
                        return
                    else:
                        self.length -= 1
                        current_node.next = current_node.next.next
                        current_node.next.behind = current_node
                        return
            except AttributeError:
                raise IndexError("Node not found")
            current_node = current_node.next

    def __len__(self):
        """Return the length of the list."""
        return self.length
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
