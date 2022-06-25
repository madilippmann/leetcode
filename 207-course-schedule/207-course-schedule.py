from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # print(adj_list)
        
        
        for course in adj_list.keys():
            stack = []  
            visited = set()
            for prereq in adj_list[course]:
                stack.append((prereq, course))

            while stack:
                cur, start = stack.pop()
                
                if cur in visited:
                    continue
                    
                if cur == start:
                    return False
                visited.add(cur)
                
                # visited.add(cur)
                if cur in adj_list:
                    for prereq in adj_list[cur]:
                        stack.append((prereq, start))

                    
        return True
            
            