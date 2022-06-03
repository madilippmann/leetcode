class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        - initialize res of []
        - iterate through string and check if s[startIndex:startIndex + len(p)] is an anagram of p
            - add index of start of anagram substrings to res
            
        - make anagram helper: create count dictionary of s and p and see if they're equal
        
        '''
        if len(s) < len(p): return []
        
        pDict = dict()
        sDict = dict()
        
        for i in range(len(p)):
            pDict[p[i]] = pDict.get(p[i], 0) + 1
            sDict[s[i]] = sDict.get(s[i], 0) + 1

        res = []
    
        if len(p) == 1:
            for i in range(len(s)):
                if s[i] == p: res.append(i)
        
            return res
        
        for i in range(len(s[:-len(p) + 1])):
            if i != 0:
                sDict[s[i - 1]] = sDict.get(s[i -1]) - 1
                if sDict[s[i - 1]] == 0: del sDict[s[i - 1]] 
                sDict[s[i + len(p) - 1]] = sDict.get(s[i + len(p) - 1], 0) + 1
            if sDict == pDict:
                res.append(i)
        
        return res
        
