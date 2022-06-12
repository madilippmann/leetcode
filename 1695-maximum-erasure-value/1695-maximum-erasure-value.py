class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        
        [4,2,4,5,6]
        [4,6,6,11,17]
        
        '''
        l, r = 0, 1
        global_max = nums[l]
        counts = {nums[0]: 0}
        
        sums = [nums[0]]
        
        for i in range(1, len(nums)):
            sums.append(sums[i-1] + nums[i])
        
        while l < r and r < len(nums):
            if nums[r] in counts and counts[nums[r]] >= l:
                l = counts[nums[r]] + 1

            counts[nums[r]] = r
            global_max = max(global_max, sums[r] - sums[l - 1] if l > 0 else sums[r])            
            r += 1
            
        return global_max
        
        
        
        
        
        
        '''
        O(n**2) solution
        
        if not nums: return 0
        
        l, r = 0, 1
        
        maxSum, curSum = nums[l], nums[l]
        subset = set([nums[l]])

        while r < len(nums) and l < r:
            if nums[r] not in subset:
                subset.add(nums[r])
                curSum += nums[r]
                maxSum = max(maxSum, curSum)
                r += 1
            else:
                l += 1
                r = l + 1
                curSum = nums[l]
                subset = set([nums[l]])
        
        return maxSum
        '''