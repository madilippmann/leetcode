class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
	
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        counts = sorted(counts.items(), reverse=True, key=lambda elem: elem[1])
        return [elem[0] for elem in counts][:k]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = dict()
        
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
            
            
#         count = sorted(list(count.items()), key=lambda tup: tup[1], reverse=True)

#         for i in range(len(count)):
#             count[i]  = count[i][0]
            
#         return count[0: k]