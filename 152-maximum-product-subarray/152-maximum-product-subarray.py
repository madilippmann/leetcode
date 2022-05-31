class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        localMax = 1
        localMin = 1
        globalMax = max(nums)
        
        for num in nums:
            if num == 0:
                localMin = localMax = 1
            else:
                tmp = localMax
                localMax = max(num, localMax * num, localMin * num)
                localMin = min(num, localMin * num, tmp * num)
                globalMax = max(globalMax, localMax)
            
        return globalMax

        












    
    



#         # if len(nums) == 1: return nums[0]
        
#         maxProducts = [1] * len(nums)
        
#         for i, num in enumerate(nums):
#             maxProducts[i] = max(maxProducts[i-1] * num, num)
        
#         print('-----------------------------\n', maxProducts)
#         print(nums)
#         # for i in range(len(nums)):
#         #     if nums[i] < 0 and (i == 0 or nums[i-1] < 0):
#         #         maxProducts[i] *= -1
                    
            
#         return max(maxProducts)