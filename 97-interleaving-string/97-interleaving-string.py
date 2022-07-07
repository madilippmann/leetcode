class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False for col in range(len(s1) + 1)] for row in range(len(s2) + 1)] 
        
        dp[0][0] = True
        
        def dfs(r, c, s1_i, s2_i, s3_i):
            if s3_i >= len(s3):
                return

            if s2_i < len(s2) and s2[s2_i] == s3[s3_i]:
                if not dp[r+1][c]:
                    dp[r+1][c] = True
                    dfs(r+1, c, s1_i, s2_i+1, s3_i+1)
            if s1_i < len(s1) and s1[s1_i]== s3[s3_i]:
                if not dp[r][c+1]:
                    dp[r][c+1] = True
                    dfs(r, c+1, s1_i+1, s2_i, s3_i+1)

        
        dfs(0,0,0,0,0)
        return dp[-1][-1] == True
        
                