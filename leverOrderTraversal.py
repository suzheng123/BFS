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
    @return: Level order a list of lists of integer
        1
       / \
      2   3  

    1 -> 2 -> 3
    """
    def levelOrder(self, root):
        if not root:
            return []
            
        stack = [root]
        tree = []
        while stack:
            level = []
            level_stack = []
            for node in stack:
                level.append(node.val)
                if node.left:
                    level_stack.append(node.left)
                if node.right:
                    level_stack.append(node.right)
            stack = level_stack
            tree.append(level)
        return tree