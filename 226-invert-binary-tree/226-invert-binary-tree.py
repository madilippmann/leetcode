# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
                4
            2       7
          1   3   6   9
        
        
                4
            2       7
          1   3   6   9
          
          pointerLeft = 2
          
          reassign root.left = root.right
          reassign root.right = pointerLeft
          
          Recurse
          invertTree(root.left)
          invertTree(root.right)
          
          return root

        '''

        # base case
        if not root: return 
        
        # Recursive case
        left = root.left
        root.left = root.right
        root.right = left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        