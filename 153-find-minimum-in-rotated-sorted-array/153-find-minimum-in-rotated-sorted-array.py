class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (r + l) // 2
            print(mid, nums[l], nums[r])
            
            if nums[l] <= nums[r]:
                return nums[l]
            elif r - l == 1:
                return min(nums[l], nums[r])
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
            
        
        return nums[l]
            