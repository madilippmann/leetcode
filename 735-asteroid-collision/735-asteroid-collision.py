class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        res = [10, 10, 2]
        [10, 2, 5, -5, -1, -5, 10, 2]
        '''
        res = []
        
        for asteroid in asteroids:
            res.append(asteroid)
            
            while len(res) > 1 and res[-2] > 0 and res[-1] < 0:
                if abs(res[-2]) == abs(res[-1]):
                    res.pop()
                elif res[-2] < abs(res[-1]):
                        res[-2], res[-1] = res[-1], res[-2]
                res.pop()
        
        
        return res