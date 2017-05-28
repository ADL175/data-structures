"""Implement the Node class and Linked_List class"""
import sys


class Node(object):
    """Creates sub class of Node."""
    def __init__(self, value, next_up=None, behind=None):
        self.value = value
        self.next = next_up
        self.behind = behind


class Linked_List(object):
    """Creates a doubly linked list."""
    def __init__(self, optional_values=[]):
        """Initialize the class instance."""
        self.head = None
        self.tail = None
        self.length = 0
        for x in optional_values:
            self.push(x)

    def push(self, value):
        """Adds new Head to head of DLL."""
        self.head = Node(value, self.head)
        if self.length == 0:
            self.tail = self.head
        self.length += 1
        if self.head.next is not None:
            self.head.next.behind = self.head

    def append(self, value):
        """Adds new node to tail of DLL."""
        self.tail = Node(value, None, self.tail)
        if self.length == 0:
            self.head = self.tail
        self.length += 1
        if self.tail.behind is not None:
            self.tail.behind.next = self.tail

    def pop(self):
        """Pop the specific node, assign it's next to head, and return popped node."""
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        if self.head:
            self.head.behind = None
        return popped

    def shift(self):
        """Removes and returns tailnode."""
        shifted = self.tail
        self.tail = self.tail.behind
        self.length -= 1
        if self.tail:
            self.tail.next = None
        return shifted

    def size(self):
        """Returns length of DLL."""
        return self.length

    def search(self, val):
        """Search for val, return node that has it."""
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return "haha, nothing here"
        return temp

    def remove(self, val):
        """Removes a specific node from DLL."""
        if self.head.value is val:
            self.head = self.head.next
            self.head.behind = None
            self.length -= 1
        current_node = self.head
        while current_node:
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

    def __len__(self):
        """Returns the length of the list."""
        return self.length
