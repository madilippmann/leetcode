class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = dict()
        
        for i, num in enumerate(nums):
            if num in numDict and abs(i - numDict[num]) <= k: 
                return True
            numDict[num] = i
            
        
        return False