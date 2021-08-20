"""
Problem 24 - Swap Pairs on LL

Failed - Got this wonderful solution at the discussion session
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:        
      # base case: only swap if subsequent pair of nodes exist
      if not head or not head.next:
          return head

      first, second = head, head.next
      # reverse the current nodes while pointing the first nodes next to the head of the subsequent reveresed list
      second.next, first.next = first, self.swapPairs(second.next)
      return second
