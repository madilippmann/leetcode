class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = {i:set() for i in range(9)}, {i:set() for i in range(9)}
        
        sub_boxes = dict()
        
        for i in range(3):
            for j in range(3):
                sub_boxes[f"{i}-{j}"] = set()
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                
                if num == '.': continue
                
                if row < 3:
                    box_row = 0
                elif 3 <= row <= 5:
                    box_row = 1
                elif row > 5:
                    box_row = 2
                
                if col < 3:
                    box_col = 0
                elif 3 <= col <= 5:
                    box_col = 1
                elif col > 5:
                    box_col = 2
                    
                box = f"{box_row}-{box_col}"
                
                if num in rows[row] or num in cols[col] or num in sub_boxes[box]:
                    return False
                
                rows[row].add(num)                
                cols[col].add(num)
                sub_boxes[box].add(num)
        
        return True
                