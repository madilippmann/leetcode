class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    islandArea = self.dfs(grid, row, col)
                    if islandArea > maxArea: maxArea = islandArea
        return maxArea
    
    
    def dfs(self, grid, startRow, startCol):
        dirs = [        (-1, 0),
                ( 0,-1),        ( 0,+1),
                        (+1, 0)
                ]
    
        visited = set(tuple([startRow, startCol]))
        stack = [(startRow, startCol)]
        area = 0
        
        while len(stack):
            row, col = stack.pop()
            
            area += 1
            grid[row][col] = 0

            for dRow, dCol in dirs:
                if row+dRow >= 0 and col+dCol >= 0 \
                and row+dRow <= len(grid) - 1 and col+dCol <= len(grid[0]) - 1 \
                and grid[row+dRow][col+dCol] == 1 \
                and (row+dRow, col+dCol) not in visited:

                    visited.add((row+dRow, col+dCol))
                    stack.append((row+dRow, col+dCol))
                    
            
        return area