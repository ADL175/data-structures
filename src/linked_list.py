import sys


class Node(object):
    def __init__(self, value, next_up):
        self.value = value
        self.next = next_up


class Linked_List(object):
    def __init__(self, optional_values=[]):
        self.head = None
        self.length = 0
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
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped

    def size(self):
        return self.length

    def search(self, val):
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return "haha, nothing here"
        return temp

    def remove_that_nick_does_not_want(self, val):
        if self.head.value is val:
            self.head = self.head.next
            pass
        current_node = self.head
        while current_node:
            if current_node.next.value is val:
                self.length -= 1
                current_node.next = current_node.next.next
                return
            if current_node is None:
                return "haha, nothing to delete"
            current_node = current_node.next

    def remove(self, node_to_be_removed):
        if self.head is node_to_be_removed:
            self.head = self.head.next
            pass
        current_node = self.head
        while current_node:
            if current_node.next is node_to_be_removed:
                self.length -= 1
                current_node.next = current_node.next.next
                break
            if current_node is None:
                pass
            current_node = current_node.next

    def display_nick_doesnt_want_because_I_assumed_we_wanted_nodes_pointing_at_each_other_but_actually_didnt(self):
        current_node = self.head
        while current_node.next is not None:
            print('({})-->'.format(current_node.value)),
            current_node = current_node.next
        print('({})'.format(current_node.value))

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


new_list = Linked_List()
new_list.push(1)
new_list.push(2)
new_list.push('whisky')
new_list.push(4)
to_be_removed = new_list.head
new_list.push('tango')
new_list.push(6)
new_list.push('foxtrot')
new_list.display()
