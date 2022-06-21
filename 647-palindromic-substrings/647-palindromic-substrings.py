class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0
        
        for i in range(len(s)):
            
            # check odd length
            l = r = i
            
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    substrings += 1
                    l -= 1
                    r += 1
                else:
                    break

            
            
            # check even length
            l, r = i, i+1
            
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    substrings += 1
                    l -= 1
                    r += 1
                else:
                    break
                    
        return substrings