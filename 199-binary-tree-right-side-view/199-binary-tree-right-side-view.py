# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        
        queue = deque([(root, 0)])
        visited_levels = set()
        
        while queue:
            node, level = queue.pop()
            print(node.val)    
            if not level in visited_levels:
                res.append(node.val)
                visited_levels.add(level)
            
            if node.right:
                queue.appendleft((node.right, level + 1))
            if node.left:
                queue.appendleft((node.left, level + 1))
        
        return res