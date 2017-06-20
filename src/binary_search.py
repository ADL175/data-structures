"""Creates a binary tree with search methods."""

class Node(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):

    def __init__(self, iterable=None):

        self._root = None
        self._size = 0
        if iterable:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.insert(element)

    def insert(self, val):
        if type(val) no in [float, int]:
            raise TypeError('You can only put in numbers.')

        # if tree is empty
        if not self._root:
            # new value should be at the tree's root
            self._root = Node(val)
            # the size of the tree increases by 1
            self._size += 1

        else:
            curr = self._root
            while curr:
                if val > curr.val:  # if new val > root val
                    if curr.right:  # if right child exists
                        curr = curr.right # move pointer to that child
                    else:
                        curr.right = Node(val)  # set empty right child of current node to be new node
                        self._size += 1
                        return
                elif val < curr.val:  # if new val is less than root val
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(val)
                        self._size += 1
                        return
                else: # if the new val is equal to root value
                    return


    def search(self, val):
        if type(val) no in [float, int]:
            raise TypeError('You can only put in numbers.')

        curr = self._root
        while curr:
            if val > curr.val:  # if new val > root val
                if curr.right:  # if right child exists
                    curr = curr.right  # move pointer to that child
                    continue
                else:
                    return
            elif val < curr.val:  # if new val is less than root val
                if curr.left:
                    curr = curr.left
                    continue
                else:
                    return
            else: # if the new val is equal to root value
                return curr
