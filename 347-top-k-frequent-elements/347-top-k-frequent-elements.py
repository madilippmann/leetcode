class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
            
        count = sorted(list(count.items()), key=lambda tup: tup[1], reverse=True)

        
        for i in range(len(count)):
            count[i]  = count[i][0]
            
        return count[0: k]