class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numsDict = dict()
        
        for i, num in enumerate(numbers):
            if (target - num) in numsDict:
                return [numsDict[target - num], i+1]
            else: numsDict[num] = i+1
                
            