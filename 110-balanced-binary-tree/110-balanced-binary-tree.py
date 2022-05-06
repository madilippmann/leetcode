# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)
        
        if not leftBalanced or not rightBalanced: return False
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # print(leftDepth, rightDepth, 0 <= abs(leftDepth - rightDepth) <= 1)
        
        return 0 <= abs(leftDepth - rightDepth) <= 1

    
        
    
    
    def maxDepth(self, root: Optional[TreeNode], depth=1) -> int:
        '''
        base case: if not root: return None
        recurisve call for left and right nodes
        assign return values to variables
        compare which return is greater and ultimately return the greater of those two values
        
        '''
        
        # base case
        if not root: return 0
        
        # recursive case
        if  root.left:
            left = self.maxDepth(root.left, depth + 1)
        else: left = depth
            
        if root.right: 
            right = self.maxDepth(root.right, depth + 1)
        else: right = depth
        
        if left >= right: return left
        else: return right
        