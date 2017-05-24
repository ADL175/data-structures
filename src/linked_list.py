"""Link list implementation."""


import sys


class Node(object):
    """Define node object."""

    def __init__(self, value, next_up):
        """Instantiate an object with a given value."""
        self.value = value
        self.next = next_up


class Linked_List(object):
    """Define the Link_List class structure"""
    def __init__(self, optional_values=[]):
        """Initialize a List with an optional list parameter"""
        self.head = None
        self.length = 0
        for x in optional_values:
            self.push(x)

    def __len__(self):
        """Return the size of specified node."""
        return self.size()

    def __print__(self):
        """Return the print() functions return value."""
        return self.display()

    def push(self, value):
        """Push a node onto the head of the list."""
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        """Pop a specific node."""
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped

    def size(self):
        """Returns the lenght attribute of instanced object."""
        return self.length

    def search(self, val):
        """See if val exist in the list."""
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return "haha, nothing here"
        return temp

    def remove_that_nick_does_not_want(self, val):
        """Remove node with specified value."""
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
        """Pass a node to and have it removed by reassigning the next link."""
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
        """Prints the value list."""
        current_node = self.head
        while current_node.next is not None:
            print('({})-->'.format(current_node.value)),
            current_node = current_node.next
        print('({})'.format(current_node.value))

    def display(self):
        """Displays the list in a tuple format"""
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
        return ""

    def __str__(self):
        """Overload the str method to be able to work with it."""
        return self.display()

    def cyclical(self):
        temp = self.head
        temp_list = []
        while temp:
            if temp in temp_list:
                print(temp)
                return True
            temp_list.append(temp.next)
            temp = temp.next
        return False


new_list = Linked_List()
new_list.push(1)
new_list.push(2)
new_list.push('whisky')
new_list.push(4)
to_be_removed = new_list.head
new_list.push('tango')
new_list.push(6)
new_list.push('foxtrot')
new_list.push(4)
print(new_list)
print(new_list.cyclical())
new_list.pop()
print(new_list)
print(new_list.cyclical())
print(new_list)
