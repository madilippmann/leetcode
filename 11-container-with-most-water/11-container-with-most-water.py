class Solution:
    def maxArea(self, height: List[int]) -> int:
        globalMax = float('-inf')
        
        l, r = 0, len(height) - 1
        
        while l < r:        
            localMax = (r-l) * min(height[l], height[r])
            globalMax = max(localMax, globalMax)
            
            if height[l] <= height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
                           
                
        return globalMax