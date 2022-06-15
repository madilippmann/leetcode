class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)] 
        
        for r in range(len(dp)):
            dp[r][0] = r 
        
        for c in range(len(dp[0])):
            dp[0][c] = c
            

        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1
            
        
        return dp[-1][-1]
        
        
        
        
        
        
        
        
        
        
#         w1 = ("0" * (len(word2) - 1)) + word1
#         w2 = word2 + ("1" * (len(word1) - 1))
                
#         max_overlaps = 0
        
#         while w1:
#             overlaps = 0

#             for i in range(len(w1)):
#                 if w1[i] == w2[i]:
#                     overlaps += 1

#             max_overlaps = max(max_overlaps, overlaps)
#             print(w1, w2, overlaps)
                    
#             w1 = w1[1:]
#             w2 = w2[:-1]
                

#         print(max_overlaps)
#         return abs(len(word1) - len(word2)) + max_overlaps
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(word1) == len(word2)
            
#         i1, i2 = 0, 0
        
#         d1, d2 = 0, 0
        
#         while i1 < len(word1) and i2 < len(word2):
#             if word1[i1] != word2[i2]:
#                 d1 += 1
#                 i2 += 1
#             else:
#                 i1 += 1
#                 i2 += 1
#         d1 += len(word1) - i1
#         print('AH1', len(word2) - i2)

#         i1, i2 = 0, 0

#         while i1 < len(word1) and i2 < len(word2):
#             if word1[i1] != word2[i2]:
#                 d2 += 1
#                 i1 += 1
#             else:
#                 i1 += 1
#                 i2 += 1
#         print(i1, i2)

#         print('AH', len(word2) - i2)
#         d2 += len(word2) - i2

#         # print(d1, d2)
                
#         return min(d1, d2)
        