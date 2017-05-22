"""
class Node(object):
    def __init__(self, value, next_up):
        self.value = value
        self.next = next_up
        pass

class Linked_List(object):
        def __init__(self):
            self.head = None
            pass

        def push(self, val):
            self.head = Node(val, self.head)
            pass

"""



class Node(object):
    def __init__(self, value, next_up):
        self.value = value
        self.next = next_up


class Linked_List(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped

    def display(self):
        node = self.head
        # print(node.data)
        # while node is not None:
        #     print(node.data)
        #     node = node.next
        node.data = 1
        print(node.data)

    def size(self):
        return self.length

    def search(val):
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return "haha, nothing here"
        return temp

    def remove(node):
        pass
