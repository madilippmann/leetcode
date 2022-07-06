class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    
                if dp[i]:
                    break
        return dp[0]
                    
        
        
#         def check_word(i):
#             if i > len(s):
#                 return
                        
#             for word in wordDict:
#                 if i in dp:
#                     return dp[i]
#                 elif word == s[i:len(word)]:
#                     dp[i] = check_word(i+len(word))


            
#         check_word(0)     
#         return dp[0]
            
            
            
            
            
            
            
            
            
            
            
            
    
#  Working solution, but time limit exceeded
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)       
        
#         def check_word(l, r):
#             # print(l, r, s[l:r])
#             if l == len(s):
#                 return True
#             elif r > len(s):
#                 return False

#             next_word = False
#             if s[l:r] in words:
#                 next_word = check_word(r, r+1)
                
#             cur_word = check_word(l, r+1)
            
#             return next_word or cur_word

    
#         return check_word(0,1)