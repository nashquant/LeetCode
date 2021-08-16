"""
Linked Lists Utils

Still lots of implementation to handle.

"""

from typing import Optional
from numbers import Number


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """
    Implementation Without `self.tail`
    """

    def __init__(self, head: Optional[Node] = None):
        self.head = head

    def addValue(self, val: Number):
        self.addNode(node=Node(val))

    def addNode(self, node: Node):

        if not isinstance(node, Node):
            raise ValueError()

        if self.head is None:
            self.head = node
            return

        else:
            cache = self.head
            while cache.next:
                cache = cache.next

            cache.next = node

    def printf(self):
        """
        This function needs to use
        a cache/buffer aux variable
        in order to traverse the LL
        without modifying self.
        """

        cache = self.head
        while True:
            print(cache.val, end="")
            cache = cache.next

            if cache:
                print(" ---> ", end="")
            else:
                break
