# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], maxDiameter=0) -> int:
        memo = {}
        
        def heightOfBinaryTree(root, depth=1): 
            if not root: return 0
            height = 1 + max(heightOfBinaryTree(root.left), heightOfBinaryTree(root.right))
            memo[root] = height
            return height
        
        def _diameterOfBinaryTree(root):
            if not root: return 0
            
            leftDepth = memo.get(root.left, 0)
            rightDepth = memo.get(root.right, 0)
            
            return max(max(maxDiameter, leftDepth + rightDepth), _diameterOfBinaryTree(root.left), _diameterOfBinaryTree(root.right))
            
            
            
        heightOfBinaryTree(root)
        return _diameterOfBinaryTree(root)

        
        
        
        
        
        
        
        
    
#     def diameterOfBinaryTree(self, root: Optional[TreeNode], maxDiameter=0) -> int:
#         '''
#         Find max depth from left node
#         Find max depth from right node
        
#         add depths together for node's maxDiameter
        
#         recurse through whole tree
        
        
#         maxDiameter comparison
#         '''
        
#         if not root: return        

#         leftMax = 0 if not root.left else self.getMaxDepth(root.left)
#         rightMax = 0 if not root.right else self.getMaxDepth(root.right)
        
#         diameter = leftMax + rightMax
        
#         if diameter > maxDiameter: maxDiameter = diameter
        
#         self.diameterOfBinaryTree(root.left, maxDiameter)
#         self.diameterOfBinaryTree(root.right, maxDiameter)
        
#         return maxDiameter + 1
        
        
#     def getMaxDepth(self, root, depth=1):
#         if not root: return 0
        
#         if  root.left:
#             left = self.getMaxDepth(root.left, depth + 1)
#         else: left = depth
            
#         if root.right: 
#             right = self.getMaxDepth(root.right, depth + 1)
#         else: right = depth
        

#         if left >= right: return left
#         else: return right
        
