class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        
        for num in nums:
            if num != 0: product *= num
            else: zeroCount += 1
                
        for i in range(len(nums)):
            if zeroCount == 0: nums[i] = product // nums[i]
            elif zeroCount == 1 and nums[i] == 0: nums[i] = product 
            else: nums[i] = 0
                
        return nums
        