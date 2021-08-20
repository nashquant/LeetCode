"""
Problem 24 - Swap Pairs on LL

Sucess
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
            
    def swapSingle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head.next
        cache = node.next

        node.next = head
        head.next = cache
        
        return node
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: return None
        if head.next is None: return head
        
        new_head = head.next
        node, prev = head, None
        
        while True:
            head = self.swapSingle(node)
            if prev is not None:
                prev.next.next = head
            node = head.next.next
            
            if node is None or node.next is None:
                break

            prev = head
            
        return new_head



"""
Below is some code I used to debug and find my own solution
"""


from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @staticmethod
    def printf(head: Optional[ListNode]):

        while head:
            print(f"{head.val}", end=" ")
            head = head.next
            
    @staticmethod
    def swapSingle(head: Optional[ListNode]) -> Optional[ListNode]:

        node = head.next
        cache = node.next

        node.next = head
        head.next = cache
        
        return node
        
    @classmethod
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: return None
        if head.next is None: return head
        
        new_head = head.next
        node, prev = head, None
        
        while True:
            head = self.swapSingle(node)
            if prev is not None:
                prev.next.next = head
            node = head.next.next
            
            if node is None or node.next is None:
                break

            prev = head
        
        self.printf(new_head)
            
        return new_head

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

head = one

ans = Solution.swapPairs(head)




