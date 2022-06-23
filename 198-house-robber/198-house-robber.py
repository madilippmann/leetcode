class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        nums = [2, 7, 9, 3, 1]
        dp = [0, 0, 0, 2, 7, 11, 10, 12]
        
        """
        dp = ([0] * 3) + nums
        
        for i in range(3, len(dp)):
            dp[i] = dp[i] + max(dp[i-2], dp[i-3])
            
        return max(dp[-1], dp[-2])
    
    
            
        