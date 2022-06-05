class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        
        squareSum = 1
        
        while squareSum not in memo:
            memo.add(squareSum)
            squareSum = 0
            
            while n:
                squareSum += (n % 10)**2
                n //= 10

            
            n = squareSum
            
        return squareSum == 1
        