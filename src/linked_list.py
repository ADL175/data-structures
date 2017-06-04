import sys


class Node(object):
    def __init__(self, value, next_up):
        self.value = value
        self.next = next_up


class Linked_List(object):
    def __init__(self, optional_values=[]):
        self.head = None
        self.length = 0
        if isinstance(option, (tuple, list)):
            for x in optional_values:
                self.push(x)

    def __len__(self):
        return self.size()

    def __print__(self):
        return self.display()

    def push(self, value):
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        if self.length is 0:
            raise IndexError('List is empty')
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped.value

    def size(self):
        return self.length

    def search(self, val):
        if self.length is 0:
            return None
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return None
        return temp

    def remove(self, node_to_be_removed):
        if isinstance(node_to_be_removed, Node):
            if self.head is node_to_be_removed:
                self.head = self.head.next
            else:
                current_node = self.head
                while current_node:
                    if current_node.next is node_to_be_removed:
                        self.length -= 1
                        current_node.next = current_node.next.next
                        break
                    current_node = current_node.next
                if current_node is None:
                    raise IndexError("Node not found.")
        else:
            return "not a node"

    def display(self):
        current_node = self.head
        the_list = []
        while current_node:
            the_list.append(current_node.value)
            current_node = current_node.next
        sys.stdout.write('('),
        for i in range(len(the_list)-1):
            sys.stdout.write('{}, '.format(the_list[i]))
        sys.stdout.write(str(the_list[-1]))
        sys.stdout.write(')')

if __name__ == '__main__':
    LL = Linked_List()
    LL.search(5)
    LL.push(5)
    remove_this = LL.head
    LL.push(4)
    LL.push(3)
    print(LL.remove([remove_this]))
