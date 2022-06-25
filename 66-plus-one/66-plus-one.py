class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        [9,9]
        [1, 0, 0]
        '''
        
        i = len(digits) - 1
        
        while i >= 0 and digits[i] + 1 > 9:
            digits[i] = 0
            
            if i == 0:
                return [1] + digits

            i -= 1
            
                
        
        
        digits[i] += 1
        return digits