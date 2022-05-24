class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()
        
        def _climbStairs(n):
            
            if n == 1: return 1
            elif n == 2: return 2
            
            if memo.get(n): return memo[n]
        
            memo[n] = _climbStairs(n-1) + _climbStairs(n-2)
            
            return memo[n]

#             memo[n-1] =  memo.get(n - 1, _climbStairs(n - 1)) 
#             memo[n-2] = memo.get(n - 2, _climbStairs(n - 2))

#             return memo[n-1] + memo[n-2]

        return _climbStairs(n)
    
