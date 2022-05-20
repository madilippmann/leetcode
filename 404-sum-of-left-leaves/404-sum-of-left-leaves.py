# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def _sumOfLeftLeaves(root, total):
            if not root: return 0

            left = _sumOfLeftLeaves(root.left, total)
            right = _sumOfLeftLeaves(root.right, total)
            
            
            if root.left and not (root.left.left or root.left.right): return root.left.val + left + right
            else: return left + right
        
        
        return _sumOfLeftLeaves(root, 0)
            