class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        (1, 1, 1, 0, ..., 1, 0, 0, 0)
        (1, 1, 0, 0, ..., 0, 0, 0, 1)
        
        
        
        sorted = ["a","d", "ab","cd","abc","bcd","abcd"]
        
        
        a: ['d', 'cd', 'bcd'],
        b: ['a', 'd', 'cd'],
        c: ['a', d', 'ab'],
        d: ['a', 'ab', 'abc']
        ab: ['d', ]
        
        '''
        maxProduct = 0
        
        while words:
            cur = words.pop()
            
            for word in words:
                if not set(list(cur)) & set(list(word)):
                    maxProduct = max(maxProduct, len(cur) * len(word))
        
        return maxProduct