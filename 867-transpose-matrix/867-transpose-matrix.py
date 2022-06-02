class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        transposed = [[None] * len(matrix) for col in range(len(matrix[0])) ]
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                transposed[j][i] = matrix[i][j]
                
        return transposed