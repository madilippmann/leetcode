class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        abccccdd
        
        '''
        longest = 0
        hasSingleLetter = False
        
        counts = dict()
        
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for key in counts:
            if counts[key] % 2 == 0:
                longest += counts[key]
            else:
                longest += counts[key] - 1
                hasSingleLetter = True
                
        
        if hasSingleLetter:
            longest += 1
            
        return longest
        
        
        
        