class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict()
        l = r = 0
        longest = 0
        
        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            if (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            
            r += 1
            
        return longest
            
        