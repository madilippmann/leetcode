class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for c in range(n)] for r in range(m)]
    
#         for r in range(1, len(dp)):
#             dp[r][0] = 1

#         for c in range(1, len(dp[0])):
#             dp[0][c] = 1

        for r in range(1, len(dp)): #len m
            for c in range(1, len(dp[0])): # len n
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[-1][-1]