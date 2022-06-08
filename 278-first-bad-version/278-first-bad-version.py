# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        BV = 1
        
        r = 1
        l = 0
        mid = 1
        
        '''
        
        l, r = 0, n
        mid =(r - l) // 2
        visited = set()
        
        lowestBadVersion = n        
        
        while mid > 0 and not mid in visited and l < r:
            print(f"MID: {mid} LEFT: {l} RIGHT: {r} BAD: {isBadVersion(mid)}")
            visited.add(mid)
            
            if isBadVersion(mid):
                lowestBadVersion = mid
                r = mid
                mid -= (r - l) // 2 
                
                
            else:
                l = mid
                mid += (r - l) // 2 
                 
        return lowestBadVersion
    
            