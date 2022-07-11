class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print(edges)
        """
        UNION FIND ALGORITHM
        
        """
        nodes = [i for i in range(len(edges) + 1)]
        sizes = [1] * (len(edges) + 1)
        
        def find(n):
            p = nodes[n]
            
            while p != nodes[p]:
                nodes[p] = nodes[nodes[p]]
                p = nodes[p]
        
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if sizes[p1] > sizes[p2]:
                nodes[p2] = p1
                sizes[p1] += sizes[p2]
            else:
                nodes[p1] = p2
                sizes[p2] += sizes[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            