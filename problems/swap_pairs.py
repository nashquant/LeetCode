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



