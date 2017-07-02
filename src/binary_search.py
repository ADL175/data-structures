"""Creates a binary tree with search methods."""


class Node(object):

<<<<<<< HEAD
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
=======
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63


class BinarySearchTree(object):

    def __init__(self, iterable=None):

        self._root = None
        self._size = 0
        if iterable:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.insert(element)

    def insert(self, value):
        if type(value) not in [float, int]:
            raise TypeError('You can only put in numbers.')

        # if tree is empty
        if not self._root:
            # new value should be at the tree's root
            self._root = Node(value)
            # the size of the tree increases by 1
            self._size += 1

        else:
            curr = self._root
            while curr:
                if value > curr.value:  # if new value > root value
                    if curr.right:  # if right child exists
                        curr = curr.right # move pointer to that child
                    else:
                        curr.right = Node(value)  # set empty right child of current node to be new node
                        self._size += 1
<<<<<<< HEAD
                        Node.parent = curr
=======
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
                        return
                elif value < curr.value:  # if new value is less than root value
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(value)
                        self._size += 1
<<<<<<< HEAD
                        Node.parent = curr
=======
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
                        return
                else: # if the new value is equal to root value
                    return

    def insert_recursion(self, value):
        """This insertion uses a helper function and recursion."""
        if type(value) not in (float, int):
            raise TypeError("Numbers only")

        self._size += 1
        self._root = self._insert_helper(self._root, value)

    def _insert_helper(self, root, value):
        """Helper function for insert_recursion."""
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self._insert_helper(root.left, value)
        elif value > root.value:
            root.right = self._insert_helper(root.right, value)
        return root

    def search(self, value):
        if type(value) not in [float, int]:
            raise TypeError('You can only put in numbers.')

        curr = self._root
        while curr:
            if value > curr.value:  # if new value > root value
                if curr.right:  # if right child exists
                    curr = curr.right  # move pointer to that child
                    continue
                else:
                    return
            elif value < curr.value:  # if new value is less than root value
                if curr.left:
                    curr = curr.left
                    continue
                else:
                    return
            else: # if the new value is equal to root value
                return curr

    def search_recursion(self, value):
        """This is a search method that uses recursion."""
        if not self._root:
            raise IndexError("The tree is empty")
        if type(value) not in (float, int):
            raise TypeError("numbers only")

        return self._search_helper(self._root, value)

    def _search_helper(self, root, value):
        """Helper function for search recursion."""
        if root.value == value:
            return root
        if value < root.value:
            return self._search_helper(root.left, value)
        elif value > root.value:
            return self._search_helper(root.right, value)

    def breadth(self):
        from que_ import Queue
        return_list = []
        next_up = Queue()
        next_up.enqueue(self._root)
        while next_up.size() > 0:
            temp = next_up.dequeue().value
            if temp.left:
                next_up.enqueue(temp.left)
            if temp.right:
                next_up.enqueue(temp.right)
            return_list.append(temp.value)
        for value in return_list:
            yield value

    def pre_order(self, node=None):
        """Depth. Return starts at root and goes to left-most node."""
        if not node:
            node = self._root
            if not node:
                yield None
        yield node.value
        if node.left:
            for each_value in self.pre_order(node.left):
                yield each_value
        if node.right:
            for each_value in self.pre_order(node.right):
                yield each_value

    def in_order(self, node=None):
        """Depth. Return starts from left-most child to right of tree."""
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_value in self.in_order(node.left):
                yield each_value
        yield node.value
        if node.right:
            for each_value in self.in_order(node.right):
                yield each_value

    def post_order(self, node=None):
        """Depth. Returns deepest left-most children, then parents, then right."""
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_value in self.post_order(node.left):
                yield each_value
        if node.right:
            for each_value in self.post_order(node.right):
                yield each_value
        yield node.value

<<<<<<< HEAD
    # def delete(self, value):
    #     start = self.search(value)
    #
    #     if not start.left and not start.right:
    #         is_root = True if start is self._root else False
    #         if is_root:
    #             size -= 1
    #             self._root = None
    #         else:
    #             if start.parent.val > start.val:
    #                 start.parent.left = None
    #             else:
    #                 start.parent.right = None
    #             size -= 1
    #     elif start.left and start.right:
    #
    #     elif start.left or start.right:

=======
>>>>>>> 7ed7aaa49c41d3b2e7bbe7c97fa97d19ce957e63
poo = BinarySearchTree()
poo.insert(34)
poo.insert(44)
poo.insert(14)
poo.insert(24)
poo.insert(54)
poo.insert(11)
poo.insert(12)
