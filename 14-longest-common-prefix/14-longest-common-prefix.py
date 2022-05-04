class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        '''
        
        dictionary of combinations/counts
        
        loop through words
            loop through letters in each word and add to dict
            
        
        loop through dict and return key with greatest value
        
        
        Time: O(n+k) n = length of the list and k = length of word in list
        Space: O(n+k)
        
        '''
        longest = 1
        lcp = ''
        
        if len(strs) == 1: return strs[0]
        elif not len(strs): return lcp

        
        prefixes = dict()
        
        for word in strs:
            for i in range(0, len(word)):
                prefixes[word[0:i+1]] = prefixes.get(word[0:i+1], 0) + 1
        
        # print(prefixes)
        for key in prefixes:
            if (prefixes[key] == len(strs) and len(key) >= len(lcp)):
                # longest = prefixes[key]
                lcp = key
        
        return lcp
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(strs) <= 1: return ''
#         lcp = ''
        
#         for curr in range(1, len(strs)):
#             matching = True
#             pointer = curr
#             index = 0
            
#             while matching and pointer < len(strs[curr-1]) and pointer < len(strs[curr]):
#                 if not strs[curr-1][:j] in strs[curr]: 
#                     matchning = False
#                 else:
#                     print(lcp, j)
#                     lcp = strs[curr][:j+1]
#                 pointer += 1
                    
#         return lcp