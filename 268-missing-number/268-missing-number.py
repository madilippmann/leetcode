class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Solution #1 O(n) time O(n) space
        s = set(nums)
        
        if 0 not in s: return 0
        elif len(nums) == 1: return 1
        
        cur = 1
        
        while cur in s:
            cur += 1
        
        return cur
    
        '''   
        return sum(range(1, len(nums) + 1)) - sum(nums)
       
        
        
        