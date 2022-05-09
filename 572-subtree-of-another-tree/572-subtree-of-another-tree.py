# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        write helper function to compare two trees
        
        Traverse main tree
        check if root.val is equal to subtree.val
        
        if root.val == subtree.val
            enter tree comparison helper function
            
            that function will recursively go through each node of both trees and return false if each root.val isn't equal
        
            
        '''
        if not root: return False
        
        match = False
        
        if root.val == subRoot.val: 
            match = self.compareTrees(root, subRoot)
        
        if match: return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right
        
    def compareTrees(self, root, subRoot):
        if not root and not subRoot: return True
        elif not root or not subRoot: return False
        
        if root.val != subRoot.val: return False
        
        left = self.compareTrees(root.left, subRoot.left)
        right = self.compareTrees(root.right, subRoot.right)
            
        return left and right
        