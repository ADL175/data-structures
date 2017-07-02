<<<<<<< HEAD
"""Link list implementation."""


import sys
=======
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63

"""A basic linked list data structure."""


class Node(object):  #pragma no cover
    """A node for the list. Has a value, and points to another node."""

    def __init__(self, value, next_up):
        """Node set up."""
        self.value = value
        self.next = next_up


<<<<<<< HEAD
class Linked_List(object):
    """Define the Link_List class structure"""
    def __init__(self, optional_values=[]):
        """Initialize a List with an optional list parameter"""
=======
class LinkedList(object):
    """Contain methods for working with nodes pointing to each other."""

    def __init__(self, optional_values=None):  #pragma no cover
        """List set up."""
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        self.head = None
        self.length = 0
        if isinstance(optional_values, (tuple, list)):
            for x in optional_values:
                self.push(x)

    def __len__(self):
        """Return Length of list."""
        return self.size()

<<<<<<< HEAD
    def __print__(self):
        """Return the print() functions return value."""
=======
    def __str__(self):  #pragma no cover
        """Print list."""
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
        return self.display()

    def push(self, value):
        """Add node with value to head of list."""
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        """Remove node from head of list."""
        if self.length is 0:
            raise IndexError('List is empty.')
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped.value

    def size(self):
        """Return Length of list."""
        return self.length

    def search(self, val):
        """Return node with given value, else return none."""
        if self.length is 0:
            return None
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return None
        return temp

    def remove(self, node_to_be_removed):
<<<<<<< HEAD
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
=======
        """Remove given node from list."""
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
            raise TypeError("Not a Node.")
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63

    def display(self):
        """Return tuple like string of list."""
        current_node = self.head
        the_list = []
        while current_node:
            the_list.append(current_node.value)
            current_node = current_node.next
<<<<<<< HEAD
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
=======
        to_return = '('
        for i in range(len(the_list)):
            to_return += '{}, '.format(the_list[i])
        if len(to_return) > 1:
            to_return = to_return[:-2]
        to_return += ')'
        return to_return
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
