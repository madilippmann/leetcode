class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        localMax = globalMax = 1 if nums[0] == 1 else 0
        
        for i in range(1, len(nums)):
            if nums[i] == 1 and nums[i-1] == 1:
                localMax += 1
            elif nums[i] == 1 and nums[i-1] == 0:
                localMax = 1
            
            globalMax = max(globalMax, localMax)
            
        return globalMax