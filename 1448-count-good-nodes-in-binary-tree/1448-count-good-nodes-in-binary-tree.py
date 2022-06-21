# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        
        stack = [(root, root.val)]
        
        while stack:
            
            node, max_val = stack.pop()
            
            if node.left:
                if node.left.val >= max_val:
                    res += 1
                    stack.append((node.left, node.left.val))
                else:
                    stack.append((node.left, max_val))
            
            if node.right:
                if node.right.val >= max_val:
                    res += 1
                    stack.append((node.right, node.right.val))
                else:
                    stack.append((node.right, max_val))
            
                
        return res
        
        