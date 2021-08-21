"""
Problem 25 - Reverse Nodes in k-Group

Sucess - Still very slow though

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseK(self, head: Optional[ListNode], k: int)->Optional[ListNode]:
        
        nxt = head
        dct = {}
        
        for i in range(k):
            if nxt is None:
                return head, None, None
            else:
                dct[i] = nxt
            
            nxt = nxt.next
            
        new_h = dct[k-1]
        new_t = dct[0]
        outer = new_h.next
        
        for i in range(k-1, 0,-1):
            dct[i].next = dct[i-1]
            
        dct[0].next = outer
            
        return new_h, new_t, outer
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        new_head, new_tail, new_next = self.reverseK(head, k)
        if new_head is head:
            return head
        
        node = new_next
        last_tail = new_tail
        while node:
            _head, _tail, node = self.reverseK(node, k)
            last_tail.next = _head
            last_tail = _tail
            
        return new_head
            
            
            
