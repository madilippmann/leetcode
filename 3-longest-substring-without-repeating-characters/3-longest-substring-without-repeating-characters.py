class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        elif len(s) == 1: return 1
        
        start = 0
        cur = 1
        
        longest = 1
        substring = set(s[start])
        
        while cur < len(s) and start < cur:
            if s[cur] not in substring:
                substring.add(s[cur])
                cur += 1
                if len(substring) > longest: longest = len(substring)
            else:
                start += 1
                cur = start + 1
                substring = set(s[start])
        
        return longest
            
            
