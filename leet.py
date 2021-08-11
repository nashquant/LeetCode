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


class Algoritmhs:
    @staticmethod
    def mergeSortedLLs(
        l1: Optional[LinkedList],
        l2: Optional[LinkedList],
    ) -> Optional[Node]:

        if not l2 and not l1:
            return None
        if not l2:
            return l1
        if not l1:
            return l2

        ans = LinkedList()

        p1 = l1.head
        p2 = l2.head

        while True:

            nL1 = p1 is None
            nL2 = p2 is None

            if nL1 and nL2:
                break
            elif nL1:
                val = p2.val
                p2 = p2.next
            elif nL2:
                val = p1.val
                p1 = p1.next
            elif p1.val < p2.val:
                val = p1.val
                p1 = p1.next
            else:
                val = p2.val
                p2 = p2.next

            ans.addValue(val)

        return ans
