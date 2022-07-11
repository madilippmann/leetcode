class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) == 1: return nums

            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]

            return merge(merge_sort(l), merge_sort(r))


        def merge(l, r):
            merged = []

            i,j = 0, 0
            
            while i < len(l) and j < len(r):
                if r[j] <= l[i]:
                    merged.append(r[j])
                    j += 1
                elif l[i] < r[j]:
                    merged.append(l[i])
                    i += 1

            return merged + l[i:] + r[j:]
        
        return merge_sort(nums)