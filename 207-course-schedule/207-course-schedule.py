# from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        visited = set()
    
        # Build adjacency list
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
            
        
        def dfs(course):
            if course in visited:
                return False
            
            if adj_list[course] == []:
                return True
                
            visited.add(course)
            
            for prereq in adj_list[course]:
                if not dfs(prereq): 
                    return False
                
            visited.remove(course)
            
            adj_list[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return 
            
        return True
    
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = defaultdict(list)
#         visited = set()
        
#         # Build adjacency list
#         for course, prereq in prerequisites:
#             adj_list[course].append(prereq)
                

#         def dfs(start_course):
#             print(start_course)
#             stack = []  
            
#             for prereq in adj_list[start_course]:
#                 stack.append((prereq, start_course))

#             while stack:
#                 course, start = stack.pop()
                
#                 if course in visited:
#                     continue
                    
#                 if course == start:
#                     return False
#                 visited.add(course)
                
#                 if course in adj_list:
#                     for prereq in adj_list[course]:
#                         stack.append((prereq, start))
            
#             return True
        
#         for course in adj_list.keys():
#             if not course in visited:
#                 if not dfs(course):
#                     return False
#         print(adj_list, visited)
#         return True

                
        
#         for course in adj_list.keys():
#             stack = []  
#             visited = set()
#             for prereq in adj_list[course]:
#                 stack.append((prereq, course))

#             while stack:
#                 cur, start = stack.pop()
                
#                 if cur in visited:
#                     continue
                    
#                 if cur == start:
#                     return False
#                 visited.add(cur)
                
#                 if cur in adj_list:
#                     for prereq in adj_list[cur]:
#                         stack.append((prereq, start))

                    
#         return True  