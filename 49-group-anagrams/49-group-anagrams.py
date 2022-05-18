class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        
        for word in strs:
            # turn each word into a an array with its letter count
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord('a')] += 1
                
            if tuple(count) in res:
                res[tuple(count)].append(word)
            else: res[tuple(count)] = [word]
        
        return res.values()
        
    def groupAnagramsTooSlow(self, strs: List[str]) -> List[List[str]]:
        '''
        - initialize a result list that will contain lists with collections of each anagram
        
        - loop through the strs list (i)
            - loop through results list  
                - check if strs[i] isAnagram results[j][0]
                    - append strs[i] to results[j]
                    - else create a new list and append it to res
                
        - return results
        
        write a helper function: isAnagram
            space: O(n)
            time: O(n)
        
            - take in (s, t)
            - check if len(s) != len(t): return False
            - initialize sDict(), tDict()
            - iterate through len(s)
                - add letter count for s and t to sDict and tDict
            - compare sDict to tDict for equality    
        
        
        Edge Cases:
            - len(strs) == 1
            - len(strs[i]) == 0
            
        
        
        Space O(n) prediction: O(n * m * k) - n = len(strs); m = len(results); k = len(strs[i])
        Time O(n) prediction: O(n * m * k) - n = len(strs); m = len(results); k = len(strs[i])
        '''
        '''
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        res = [['eat', 'tea', 'eat'], ['tan', 'nat'], ['bat']] 
        len(s) = 6
        len(res) = 0
        i = 5
        j = 1
        
        
        Input: ['']
        res = [['']]
        
        '''
        
        
        res = []
        
        for i in range(len(strs)):
            if not len(res):
                res.append([strs[i]]) 
            else: 
                addedToRes = False
                for j in range(len(res)):
                    if self.isAnagram(strs[i], res[j][0]):
                        res[j].append(strs[i])
                        addedToRes = True
                if not addedToRes: res.append([strs[i]]) 
                    
        return res
    
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        
        sDict = dict()
        tDict = dict()
        
        for letter in range(len(s)):
            sDict[s[letter]] = sDict.get(s[letter], 0) + 1
            tDict[t[letter]] = tDict.get(t[letter], 0) + 1
        
        return sDict == tDict