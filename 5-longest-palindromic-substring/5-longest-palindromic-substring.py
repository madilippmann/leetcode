class Solution:
    def longestPalindrome(self, s: str) -> str:
        global_longest = s[0]
        
        for i in range(len(s)):   
            
            # check odd length
            l, r = i-1, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(global_longest):
                    global_longest = s[l:r+1]
                l -= 1
                r += 1
            
            # check even length
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(global_longest):
                    global_longest = s[l:r+1]
                l -= 1
                r += 1
            
        return global_longest