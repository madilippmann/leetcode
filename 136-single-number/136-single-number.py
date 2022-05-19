class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = ''
        while len(nums):
            end = nums.pop()
            if end not in nums and str(end) not in s:
                return end
            
            else: s += str(end)
        
