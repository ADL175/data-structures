"""Sourced from Sean Beseler's code during code review."""

from linked_list import LinkedList


class Stack(object):
    """Ojbect inheretence from Linked list to create Stack Data structure."""

    def __init__(self, data=[]):
        """Instantiate new Stack."""
        self._new_linked_list = LinkedList(data)

    def pop(self):
        """Remove and returns node from top of the stack."""
        return self._new_linked_list.pop()

    def push(self, val):
        """Add a new node to the top of stack."""
        return self._new_linked_list.push(val)

    def __len__(self):
        """Return length of stack."""
        return self._new_linked_list.__len__()
