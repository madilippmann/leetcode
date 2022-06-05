class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1): return False
        
        s1Count, s2Count = dict(), dict()
        
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1
        
        if len(s1) == len(s2) or s1Count == s2Count: 
            return s1Count == s2Count
        
        for i in range(len(s1), len(s2)):
            
            if s2Count.get(s2[i - len(s1)]):
                s2Count[s2[i - len(s1)]] -= 1
                if s2Count[s2[i - len(s1)]] == 0:
                    del s2Count[s2[i - len(s1)]]
            
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

            if s1Count == s2Count:
                return True
            
        return False