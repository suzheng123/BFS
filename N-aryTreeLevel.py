"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]

                    1
                 /  |  \
                3   2   4
               / \
              5   6 

              [[1],[3,2,4],[5,6]]
        """
        if not root:
            return []
        
        stack = [root]
        tree = []
        while stack:
            level =  []
            temp_stack = []
            for node in stack:
                level.append(node.val)                
                for child in node.children:
                    temp_stack.append(child)
            stack = temp_stack            
            tree.append(level)
        
        return tree