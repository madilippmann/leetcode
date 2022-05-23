# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True
        elif not p or not q : return False
        elif p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        check if a root exists for both p and q 
            - if both p and q don't have a root 
                - RETURN TRUE
            - if p has root and q doesn't have root or q has root and p doesn't have root: RETURN FALSE
                - the trees aren't identical in depth
        
        check if root.left and root.right values are the same for p and q
            - if q.left != p.left or q.right != p.right: return false
            
        
        traverse each node form current root
        recursively call with left and right nodes
        
        - left = isSameTree(p.left, q.left)
        
        - right = isSameTree(p.right, q.right)
        
        
        if not right or not left: return false
        else: return true
        
    TEST 1
    P---------------
            1
        2       3
    4
    Q---------------
            1
        2       3
    4
    ----------------
    
    isSameTree(p, q) 1
    
        isSameTree(p.left, q.left) 2
             RETURN TRUE isSameTree(4, 4)
                isSameTree(None, None) left
                    return True
                isSameTree(None, None) right
                    return True
            isSameTree(None, None)
                return True
    
        isSameTree(p.right, q.right) 3
        
        '''
#         if not p and not q: return True
#         elif not p or not q: return False
        
#         if p.val != q.val: return False
        
        
#         left = self.isSameTree(p.left, q.left)
#         right = self.isSameTree(p.right, q.right)
        
#         if not right or not left: return False
#         else: return True
        
        