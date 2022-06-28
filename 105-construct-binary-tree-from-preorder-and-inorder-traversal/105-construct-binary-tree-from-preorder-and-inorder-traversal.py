# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 
        
        node = TreeNode(preorder[0])
        
        inorder_left = inorder[:inorder.index(preorder[0])]
        inorder_right = inorder[inorder.index(preorder[0])+1:]

        preorder_left = preorder[1:len(inorder_left) + 1]
        preorder_right = preorder[1 + len(preorder_left):]
        
        node.left = self.buildTree(preorder_left, inorder_left)
        node.right = self.buildTree(preorder_right, inorder_right)
        
        
        return node