class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        subset = []
        
        def backtrack(i):
            if i == len(nums):
                if tuple(sorted(subset)) not in subsets:
                    subsets.add(tuple(sorted(subset)))
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)
        
        
        backtrack(0)
        return [list(tup) for tup in list(subsets)]