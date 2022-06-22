class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, available_nums):
            if len(path) == len(nums):
                res.append(path)
                return 
            
            for i, num in enumerate(available_nums):
                backtrack(path + [num], available_nums[0:i] + available_nums[i+1:])
            
        for i, num in enumerate(nums):
            backtrack([num], nums[0:i] + nums[i+1:])  
        
        return res