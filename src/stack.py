import sys


class Node(object):
    def __init__(self, value, next_up):
        self.value = value
        self.next = next_up


class Stack(object):
    def __init__(self, optional_values=[]):
        self.head = None
        self.length = 0
        for x in optional_values:
            self.push(x)

    def push(self, value):
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped


poop = Stack()
poop.push(4)
poop.push(345)
poop.push(332)
poop.pop()
