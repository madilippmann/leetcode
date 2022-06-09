class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        
        visited = set()
        queue = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    
        while queue:
            row, col, level = queue.pop(0)
            
            minutes = max(level, minutes)
            
            for dR, dC in ((-1,0), (0,-1), (0,1), (1,0)):
                nR, nC = row + dR, col + dC
                
                if (0 <= nR < len(grid) and
                   0 <= nC < len(grid[0]) and
                   (nR, nC) not in visited and
                    grid[nR][nC] == 1):
                    
                    grid[nR][nC] = 2
                    visited.add((nR, nC))
                    queue.append((nR, nC, level + 1))
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
                
        return minutes
        
        
