class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        last col of first row added to res
        first col of last row added to res
        
        '''
        invalid, valid = set(), set()
        res = []
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (0 <= (r-1) < len(heights) and 0 <= (c-1) < len(heights[0]) and 
                    (heights[r-1][c] < heights[r][c] and (r-1, c) in valid) or 
                    (heights[r][c-1] < heights[r][c] and (r, c-1) in valid)
                    ):
                    res.append([r,c])
                    valid.add((r,c))                            
                        
                elif (0 <= (r-1) < len(heights) and 0 <= (c-1) < len(heights[0]) and
                    (heights[r-1][c] >= heights[r][c] and (r-1, c) in invalid) and
                    (heights[r][c-1] >= heights[r][c] and (r, c-1) in invalid)):
                    invalid.add((r,c))
                            
                else:
                    if self.dfs(heights, r, c):
                        res.append([r,c])
                        valid.add((r,c))
                    else:
                        invalid.add((r,c))
    
        return res
    
                                                
    def dfs(self, heights, startRow, startCol):
        pacific, atlantic = False, False
        
        stack = [(startRow, startCol)]
        visited = set(tuple([startRow, startCol]))
        
        while stack and (pacific == False or atlantic == False):
            row, col = stack.pop()
            
            if row == 0 or col == 0:
                pacific = True
            
            if row == len(heights) - 1 or col == len(heights[0]) - 1:
                atlantic = True
        
            if pacific and atlantic:
                break
            
            
            for dR, dC in ((-1,0), (0,-1), (0,1), (1,0)):
                if (0 <= row+dR < len(heights) and
                    0 <= col+dC < len(heights[0]) and
                    (row+dR, col+dC) not in visited and
                    heights[row+dR][col+dC] <= heights[row][col]):
                    stack.append((row+dR, col+dC))
                    visited.add((row+dR, col+dC))
        
        
        return pacific and atlantic

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
                