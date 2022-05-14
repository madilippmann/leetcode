class Solution:
    def fib(self, n: int) -> int:
        return self._fib(n, {})
        
    def _fib(self, n, memo):
        if n == 0 or n == 1: return n
        
        if memo.get(n): return memo[n]
        
        left = self._fib(n-1, memo)
        right = self._fib(n-2, memo)
        
        memo[n] = left + right
        return memo[n]