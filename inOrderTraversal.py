"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
        1
       / \
      2   3  

    2 -> 1 -> 3

    """
   
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        return self.inorderTraversal(root.left) + [root.val]\
            + self.inorderTraversal(root.right)