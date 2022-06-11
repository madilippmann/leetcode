class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Insert it where it best fits
        
        iterate through again and merge intervals
        '''
        
        intervals = [newInterval] + intervals
        
        l, r = 0, 1
        
        while l < r and r < len(intervals):
            if intervals[l][0] > intervals[r][0] and intervals[l][0] > intervals[r][1]:
                intervals[l], intervals[r] = intervals[r], intervals[l]

            
            elif intervals[r][0] <= intervals[l][0] <= intervals[r][1] or intervals[l][1] >= intervals[r][0]:
                intervals[r][0] = min(intervals[l][0], intervals[r][0])
                intervals[r][1] = max(intervals[l][1], intervals[r][1])
                intervals[l] = [-1,-1]
            
            l = r
            r += 1
        
        return [interval for interval in intervals if interval != [-1,-1]]
        
        
        
        
        
#         for i in range(len(intervals)):
#             if i < len(intervals) - 1 and newInterval[0] > intervals[i][1] and newInterval[1] < intervals[i+1][0]:
#                 intervals.insert(i+1,newInterval)
#                 return intervals
#             elif i < len(intervals) and newInterval[0] > > intervals[i][1] and newInterval[1] > intervals[i+1][0]:
                
#                 break
#             elif i == 0 and newInterval[1] < interval[i][0]:
#                 intervals.insert(0, newInterval)
#                 return intervals
#             elif i == len(intervals) - 1 and newInterval[0] > intervals[i][1]:
#                 intervals.append(newInterval)
#                 return intervals
            
#         j = i + 1
#         while j < len(intervals) and newIntervals[1] > intervals[j][0]:
            
#             j += 1
            
            
        
       