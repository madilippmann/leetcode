class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

        
    def add(self, val: int) -> int:
        
        l, r = 0, len(self.nums) 
        
        while l <= r:
            mid = (r + l) // 2

            if mid == len(self.nums):
                mid += 1
                break
            elif val == self.nums[mid] or (mid - 1 >= 0  and self.nums[mid - 1] < val < self.nums[mid]):
                break
            elif val > self.nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        self.nums = self.nums[:mid] + [val] + self.nums[mid:]
        
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)