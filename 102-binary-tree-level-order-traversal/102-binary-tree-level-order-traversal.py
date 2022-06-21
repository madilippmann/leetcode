# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = [[]]
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.pop()
            
            if level >= len(res) - 1:
                res.append([])
            
            res[level].append(node.val)
            
            if node.left:
                queue.appendleft((node.left, level+1))
        
            if node.right:
                queue.appendleft((node.right, level+1))

        print(res)
        res.pop()
        return res