class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Remove min(nums[0], nums[-1]) from nums
        
        dp as usual
        
        """
        if len(nums) <= 3: return max(nums)

        
        dp1 = [0, 0, 0] + nums[1:]
        dp2 = [0, 0, 0] + nums[:-1]
        
        
        for i in range(3, len(dp1)):
            dp1[i] = dp1[i] + max(dp1[i-2], dp1[i-3])
            dp2[i] = dp2[i] + max(dp2[i-2], dp2[i-3])

        
        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])