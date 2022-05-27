class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        elif len(nums) == 1: return 1
        
        unique = set(nums)
        sequenceStarts = []        

        longest = 1
        
        for num in unique:
            if num - 1 not in unique:
                length = 1
                cur = num 
            
                while cur + 1 in unique:

                        length += 1
                        cur += 1
                        longest = max(length, longest)

#                 sequenceStarts.append(num)
                
#         for num in sequenceStarts:



        return longest

        