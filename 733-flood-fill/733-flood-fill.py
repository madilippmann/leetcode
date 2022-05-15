class Solution:
    # Recursive Solution     
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        
        def _floodFill(r, c, visited):
            if (r < 0 or r > len(image) - 1) or (c < 0 or c > len(image[0]) - 1) \
            or (r, c) in visited \
            or image[r][c] != oldColor:
                return

            image[r][c] = newColor
            visited.add((r, c))
            
            _floodFill(r-1, c, visited) # Prev row
            _floodFill(r+1, c, visited) # Next row
            _floodFill(r, c-1, visited) # Prev col
            _floodFill(r, c+1, visited) # Next col

            return image
        
        
        return _floodFill(sr, sc, set())
    
    
    # Iterative Solution
    def floodFillIterative(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirs = [
                        (-1, 0),
                ( 0,-1),        ( 0,+1),
                        (+1, 0)
        ]
        
        visited = set(tuple([sr, sc]))
        stack = [(sr, sc)]
        oldColor = image[sr][sc]
    
        while len(stack):
            r, c = stack.pop()
            
            image[r][c] = newColor
            
            for dR, dC in dirs:
                if (0 <= r+dR <= len(image) - 1) and (0 <= c+dC <= len(image[0]) - 1) \
                and image[r+dR][c+dC] == oldColor \
                and (r+dR, c+dC) not in visited:
                    visited.add((r+dR, c+dC))
                    stack.append((r+dR, c+dC))

        return image