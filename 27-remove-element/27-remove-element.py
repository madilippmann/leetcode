class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        tail = len(nums)
        
        while i < tail:
            if nums[i] == val:
                nums.pop(i)
                tail -= 1
            else: i += 1