class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }
        
        def backtrack(i):
            if i in dp:
                return dp[i]
            
            if i >= len(s) or s[i] == "0":
                return 0
            
            res = backtrack(i+1)
            
            if i+1 < len(s) and s[i] == "1" or int(s[i:i+2]) < 27:
                res += backtrack(i+2)
            
            dp[i] = res
            return res
        

        return backtrack(0)
        
    
#  RECURSIVE BACKTRACKING WITHOUT DYNAMIC PROGRAMMING - SLOW BUT WORKING SOLUTION
#     def numDecodings(self, s: str) -> int:
#         self.res = 0
        
#         def backtrack(s):
#             if int(s[0]) == 0:
#                 return
#             elif len(s) == 1:
#                 self.res += 1
#                 return
#             if len(s) == 2:
#                 if int(s[:2]) < 27:
#                     self.res += 1
#                 if int(s[1]) != 0:
#                     self.res += 1
#                 return

            
#             backtrack(s[1:])
            
#             if int(s[:2]) < 27:
#                 backtrack(s[2:])
        

#         backtrack(s)
#         return self.res