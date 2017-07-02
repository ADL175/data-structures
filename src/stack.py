"""Sourced from Sean Beseler's code during code review."""

from linked_list import Linked_List


class Stack(object):
    """Ojbect inheretence from Linked list to create Stack Data structure."""
    def __init__(self, data=[]):
        self._new_linked_list = Linked_List(data)

    def pop(self):
        return self._new_linked_list.pop()

    def push(self, val):
        return self._new_linked_list.push(val)

    def __len__(self):
        return self._new_linked_list.__len__()
