class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O': 
                    tilesToFlip = self.islandTraversal(board, row, col)
                    if tilesToFlip and len(tilesToFlip):
                        for tileRow, tileCol in tilesToFlip:
                            board[tileRow][tileCol] = 'X'
                            
                        
                    
    def islandTraversal(self, board, startRow, startCol):
        '''
        return visited set
        '''
        dirs = [        [-1, 0], 
                [ 0,-1],       [ 0,+1],
                        [+1, 0]]
        
        visited = set()
        visited.add((startRow, startCol))
        stack = [(startRow, startCol)]

        
        while len(stack):
            row, col = stack.pop()
            
            if (row <= 0 or col <= 0 or row >= len(board) - 1 or col >= len(board[0]) - 1) :
                return False
            
            for dRow, dCol in dirs:
                if not (row+dRow, col+dCol) in visited and board[row+dRow][col+dCol] == 'O':
                    visited.add((row, col))
                    stack.append((row + dRow, col + dCol))

        return list(visited)
                
            
            
        
    
    
        