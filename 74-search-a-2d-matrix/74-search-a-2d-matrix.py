class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            mid = (r + l) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # do another round of binary search over row and return true if found, false if not found
                l, r = 0, len(matrix[0]) - 1
                
                while l <= r:
                    row_mid = (r + l) // 2
                    
                    if matrix[mid][row_mid] == target: 
                        return True
                    elif target < matrix[mid][row_mid]:
                        r = row_mid - 1
                    elif target > matrix[mid][row_mid]:
                        l = row_mid + 1
                
                return False

                
            elif target <= matrix[mid][0]:
                r = mid - 1
            
            elif target > matrix[mid][-1]:
                l = mid + 1
            
            else: 
                return False