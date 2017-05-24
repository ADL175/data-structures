import sys


class Node(object):

    def __init__(self, value, next_up=None, behind=None):
        self.value = value
        self.next = next_up
        self.behind = behind


class Linked_List(object):

    def __init__(self, optional_values=[]):
        self.head = None
        self.tail = None
        self.length = 0
        for x in optional_values:
            self.push(x)

    def push(self, value):
        self.head = Node(value, self.head)
        if self.length == 0:
            self.tail = self.head
        self.length += 1
        if self.head.next is not None:
            self.head.next.behind = self.head

    def append(self, value):
        self.tail = Node(value, None, self.tail)
        if self.length == 0:
            self.head = self.tail
        self.length += 1
        if self.tail.behind is not None:
            self.tail.behind.next = self.tail

    def pop(self):
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
