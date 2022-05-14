class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        
        '''
        islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    islands += 1
        
        return islands
    
    
    def dfs(self, grid, startRow, startCol):
        dirs = [        (-1, 0),
                ( 0,-1),        ( 0,+1),
                        (+1, 0)
               ]
        
        visited = set(tuple([startRow, startCol]))
        stack = [(startRow, startCol)]
        
        while len(stack):
            
            row, col = stack.pop()
            
            if grid[row][col] == '1':
                grid[row][col] = '0'
            
            for dRow, dCol in dirs:
                if (row+dRow >= 0 and col+dCol >= 0 and row+dRow <= len(grid) - 1 and col+dCol <= len(grid[0]) - 1) \
                    and not (row+dRow, col+dCol) in visited \
                    and grid[row+dRow][col+dCol] == '1':
                    visited.add((row+dRow, col+dCol))
                    stack.append((row+dRow, col+dCol))
        
        
        return 