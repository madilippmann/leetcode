class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
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