"""

Given the root of a binary tree, invert the tree, and return its root.

Used an auxilliary stack to keep track of traversed but not inverted nodes.

Complexity:
- Time: O(V) - V is # of vertices (each node must be visited.. Assuming constant time for each inverse operation seems reasonable)
- Space: O(h(V)) - h(v) is the height of the tree.. Worst case for the stack is when all nodes of the highest path are stored.

Could implement some tricks to improve space complexity, but why bother??

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return
        
        stack = [root]
        while stack:
            tmp = stack.pop()
            tmp.left, tmp.right = tmp.right, tmp.left
            if tmp.right is not None:
                stack.append(tmp.right)
            if tmp.left is not None:
                stack.append(tmp.left)
                
        return root
