class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        magazineDict = dict()
        
        for c in magazine:
            magazineDict[c] = magazineDict.get(c, 0) + 1
        
        for c in ransomNote:
            if not c in magazineDict or magazineDict[c] == 0:
                return False
            else:
                magazineDict[c] -= 1
        
        return True