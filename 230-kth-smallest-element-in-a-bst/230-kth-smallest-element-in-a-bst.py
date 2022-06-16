# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        time complexity: O(n)
        space complexity: variables - O(1), recursive call stack - O(n), average case will be max depth of tree - 
                
        in-order traversal

        
        base case:
        if no node
            return False
        when k <= 0:
            return val of current node
        
        
        
        left = recursively call left node
        k -= 1

        right = recursively call the right node
        
       if left != False:
            return left
        elsif right != False;
            return right
        else:
            return False

        
        
        go as far left as possible then go right
        subtract from k with each call
        
        call _kthSmallest
        return k
        
        
        6 - 1 - 1 - 1 - 1 - 1 - 1
        '''
        self.k = k
        self.res = None
        def _kthSmallest(node):
            if not node: 
                return 

            _kthSmallest(node.left)
            self.k -= 1

            if self.k == 0:
                self.res = node.val
                return
            _kthSmallest(node.right)

        
        _kthSmallest(root)
        return self.res