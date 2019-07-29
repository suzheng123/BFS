"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
        1
       / \
      2   3  

    2 -> 3 -> 1
    """
    def postorderTraversal(self, root):
        if not root:
            return []
        
        parent = [root]
        stack = []
        tree = []
        
        while parent:
            node = parent.pop()
            stack.append(node)
            
            if node.left:
                parent.append(node.left)
            if node.right:
                parent.append(node.right)
        
        while stack:
            tree.append(stack.pop().val)
            
        return tree