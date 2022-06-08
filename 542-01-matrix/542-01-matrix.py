class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] != 0:
                    mat[row][col] = '#'
                else:
                    queue.append((row, col))
                    
        while queue:
            dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            r, c = queue.pop(0)
            
            
            for dR, dC in dirs:
                nR, nC = r+dR, c+dC

                if 0 <= nR < len(mat) and 0 <= nC < len(mat[0]) and mat[nR][nC] == '#':
                    mat[nR][nC] = mat[r][c] + 1
                    queue.append((nR, nC))
                    
        return mat
        
#         for row in range(len(mat)):
#             for col in range(len(mat[0])):
#                 if mat[row][col] == 1:
#                     mat[row][col] = float('inf')
                    
        
#         for row in range(len(mat)):
#             for col in range(len(mat[0])):
#                 if mat[row][col] == 0:
#                     # call helper function
#                     self.bfs(mat, row, col)
#         return mat
        
        
    
#     def bfs(self, mat, startRow, startCol):
#         dirs = [        (-1, 0),
#                ( 0,-1),         ( 0, 1),
#                         ( 1, 0)
#                ]
        
#         startLevel = 0
#         queue = [(startRow, startCol, startLevel)]
#         visited = set([startRow, startCol])
        
#         while queue:
#             r, c, level = queue.pop(0)
            
# #             MUTATE MATRIX HERE DO THE THING
#             mat[r][c] = min(mat[r][c], level)
            
#             for (dR, dC) in dirs:
#                 if  (0 <= r + dR < len(mat) and 
#                     0 <= c + dC < len(mat[0]) and  
#                     (r + dR, c + dC) not in visited and 
#                     mat[r+dR][c+dC] != 0):
                    
#                     visited.add((r+dR, c+dC))
#                     queue.append((r+dR, c+dC, level + 1))
            
            
            
        
        
        
        
        
        
#         '''
#         nested for loop to iterate through entire matrix
#         res = []
        
#         for row in rows:
#             for col in cols:
#                 if num == 0:
                    
#                 find minimum distance between current value and nearest zero
        
#         '''
#         res = []
#         memo = dict()

#         for row in range(len(mat)):
#             resRow = []
#             for col in range(len(mat[0])):
#                 nearestZero = self.nearestZero(mat, row, col)
#                 resRow.append(nearestZero)
#                 memo[(row, col)] = nearestZero
#             res.append(resRow)
                    
#         return res
    
    
#     def nearestZero(self, mat, startRow, startCol, memo):
#         startLevel = 0
#         dirs = [        (-1, 0),
#                ( 0,-1),         ( 0, 1),
#                         ( 1, 0)
#                ]
        
#         visited = set([startRow, startCol])
#         queue = [(startRow, startCol, startLevel)]
        
#         '''
#         memo = {
        
#         [(startRow, startCol)]: (16, set(path))

#         }

# minimum of surrounding directions if all direction or if it's zero, it's zero
# '''
        
#         while queue:
#             row, col, level = queue.pop(0)
            
#             if mat[row][col] == 0:
#                 return level
            
#             for dRow, dCol in dirs:
#                 if (row + dRow, col + dCol) in memo:
#                     if (row + dRow, col + dCol) in memo and 
#                         return memo[(row + dRow, col + dCol)] + 1
#                     return memo[(row + dRow, col + dCol)] - 1
#                 elif 0 <= row + dRow < len(mat) and 0 <= col + dCol < len(mat[0]) and (row + dRow, col + dCol) not in visited:
#                     visited.add((row +dRow, col+dCol)) 
#                     queue.append((row +dRow, col+dCol, level + 1))
                    
            
        
        
        
        