class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target: 
                return mid
            
            elif nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: 
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                
        return -1                
                
#             elif nums[mid] > target and nums[mid] > nums[left] and nums[left] <= target:
#                 right = mid - 1
#             elif nums[mid] < target and nums[mid] < nums[right] and nums[right] >= target:
#                 left = mid + 1
#             elif nums[mid] > target and nums[mid] > nums[right]:
#                 left = mid + 1
#             elif nums[mid] < target and nums[mid] < nums[left]:
#                 right = mid - 1
#             else:
#                 return -1
            
