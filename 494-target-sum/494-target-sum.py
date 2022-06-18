class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
            return memo[(i, total)]

        return backtrack(0, 0)       
        
        
        
        
        
        
        """
        BRUTE FORCE
        memo = [-nums[0], nums[0]] 

        for num in nums[1:]:
            i, length = 0, len(memo)
            while i < length:
                memo.append(memo[i] - num)
                memo[i] += num
                i += 1
        
        matches = 0
        
        for entry in memo:
            if entry == target:
                matches += 1

        return matches
        """