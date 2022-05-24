import math
class Solution:
    def search(self, nums: List[int], target: int, startIndex=0) -> int:
        
        if not len(nums): return -1
        
        mid = int(len(nums) / 2)

        if nums[mid] == target: return mid + startIndex
        elif nums[mid] < target: return self.search(nums[mid + 1:], target, startIndex + mid + 1)
        elif nums[mid] > target: return self.search(nums[:mid], target, startIndex)
        
        
        
        
        
        
#         l = 0
#         r = len(nums) - 1
#         mid = math.ceil((r - l) / 2)

#         while l < r:

#             # print('left: ', l, ' right: ', r, ' mid: ', mid, 'num: ', nums[mid])
#             if nums[mid] == target: 
#                 # print('-------------')
#                 return mid
#             elif target < nums[mid]: 
#                 r -= mid
#                 mid = l + math.ceil((r - l) / 2)

#             elif target > nums[mid]:
#                 l += mid
#                 mid = l + math.ceil((r - l) / 2)

            
        
#         return mid if mid < len(nums) - 1 and nums[mid] == target else -1