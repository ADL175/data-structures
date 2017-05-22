
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
        current_node = self.head
        print(current_node.value)
        while current_node:
            print(current_node.value)
            if current_node.next.value is val:
                print(current_node.value)
                self.length -= 1
                current_node.next = current_node.next.next
            if current_node is None:
                return "haha, nothing to delete"
        print(current_node.value)
        return current_node


poop = Linked_List()
poop.push(3)
poop.push(5)
poop.push(4334)
poop.push(87)
poop.size()
