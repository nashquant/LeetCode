from typing import Optional
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    def add(self, val: int):
        if type(val) != int:
            return
        self._add(self.root, val)

    def _add(self, current: TreeNode, val: int):
        if self.root is None:
            self.root = TreeNode(val)

        if current is None:
            current = self.root

        elif val < current.val:
            if current.left is None:
                current.left = TreeNode(val)
            else:
                self._add(current.left, val)

        else:
            if current.right is None:
                current.right = TreeNode(val)
            else:
                self._add(current.right, val)

    def visit(self, node: TreeNode):
        if node is not None:
            print(node.val, end = " ")

    def preorder(self, node: Optional[TreeNode] = None):
        """
        Traverse Visit -> Left -> Right
        """

        node = node or self.root
        
        self.visit(node)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def inorder(self, node: Optional[TreeNode] = None):
        """
        Traverse Left -> Visit -> Right
        """

        node = node or self.root
        
        if node.left:
            self.inorder(node.left)
        self.visit(node)
        if node.right:
            self.inorder(node.right)
    
    def postorder(self, node: Optional[TreeNode] = None):

        """
        Traverse Left -> Right -> Visit
        """

        node = node or self.root
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        self.visit(node)
        
    def inorder_iterative(self):

        """
        Complexity: O(n)
        Aux Space: O(h) -> h = height of the tree
        
        """

        stack = []
        tmp = self.root

        while stack or tmp is not None:
            if tmp is not None:
                stack.append(tmp)
                tmp = tmp.left
            else:
                tmp = stack.pop()
                self.visit(tmp)
                tmp = tmp.right
        
    def preorder_iterative(self):

        """
        
        
        """

        if self.root is None:
            return

        stack = [self.root]

        while stack:
            tmp = stack.pop()
            self.visit(tmp)
            if tmp.right is not None:
                stack.append(tmp.right)
            if tmp.left is not None:
                stack.append(tmp.left)
        
if __name__ == "__main__":
    bst = BST()

    bst.add(7)
    bst.add(3)
    bst.add(5)
    bst.add(2)
    bst.add(9)
    bst.add(6)

    bst.preorder()
    print()
    bst.preorder_iterative()

