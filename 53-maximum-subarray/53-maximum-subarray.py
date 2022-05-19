class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # create empty list to store max values
        dp = [0] * len(nums)
        
        # iterate through nums
        for i, num in enumerate(nums):
            # check if last stored maximum value is greater than the current number
            # assign dp[i] to greater of the two
            dp[i] = max(dp[i-1] + num, num)
    
        # retrun max of dp list
        return max(dp)
    
    
    
    
    
    
    
    
#     NAIVE SOLUTION
#     def maxSubArray(self, nums: List[int]) -> int:
#         max = float('-inf')
        
#         for i in range(len(nums)):
#             sum = nums[i]
#             for j in range(i, len(nums)):
#                 if i != j:
#                     sum += nums[j]
                
#                 if sum > max: max = sum
                    
#         return max