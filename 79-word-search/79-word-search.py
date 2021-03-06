class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def backtrack(r, c, i):
            
            if (r < 0 or c < 0 or 
                r >= len(board) or c >= len(board[0]) or
                board[r][c] != word[i] or
                (r, c) in visited):
                return False
            
            if i == len(word) - 1:
                return True

            visited.add((r, c))
            valid_path = (backtrack(r-1, c, i+1) or
                          backtrack(r+1, c, i+1) or
                          backtrack(r, c-1, i+1) or
                          backtrack(r, c+1, i+1))
            visited.remove((r,c))
            
            return valid_path
           
        if len(word) > len(board) * len(board[0]):
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True

                    
        return False
                    
       
