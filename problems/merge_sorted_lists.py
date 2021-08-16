"""
Problem 21 - Merge Two Sorted Lists.

Success

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l2 and not l1:
            return None
        if not l2:
            return l1
        if not l1:
            return l2
        
        if l1.val < l2.val:
            resp = ListNode(val = l1.val)
            l1 = l1.next
            
        else:
            resp = ListNode(val = l2.val)
            l2 = l2.next
        
        while True:
            
            nL1 = l1 is None
            nL2 = l2 is None
            
            if nL1 and nL2:
                break
            elif nL1:
                val = l2.val
                l2 = l2.next
            elif nL2:
                val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            
            cache = resp
            
            while cache.next:
                cache = cache.next
            
            cache.next = ListNode(val)
                
        return resp
        