class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        pointer at end of list
        """
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != 0:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                i += 1
                
                
        