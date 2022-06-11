class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        left_sums, right_sums = {}, {}
        left_running_sum, right_running_sum = 0, 0
        
        i, j = 0, len(nums) - 1
        
        while i < len(nums):
            left_running_sum += nums[i]
            left_sums[left_running_sum] = i + 1
            
            right_running_sum += nums[j]
            right_sums[right_running_sum] = i + 1
            
            
            i += 1
            j -= 1

        # print(left_sums, right_sums)
        
        min_ops = float('inf')
        
        if x in left_sums:
            # print('ENTERED: ', left_sums[x])
            min_ops = min(left_sums[x], min_ops)
        if x in right_sums:
            min_ops = min(right_sums[x], min_ops)
        for k in left_sums:
            if x - k in right_sums and left_sums[k] + right_sums[x-k] < len(nums):
                # print('HAS IT! ', k, x - k)
                min_ops = min(left_sums[k] + (right_sums[x - k]), min_ops)
        
        return min_ops if not min_ops == float('inf') else -1
        