"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: 
            return node
        
        stack = [node]

        nodes = {
            node.val: Node(node.val)
        }
                
        while stack:
            cur = stack.pop()
            cur_clone = nodes[cur.val]
            
            
            for neighbor in cur.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                    
                cur_clone.neighbors.append(nodes[neighbor.val])
        
        return nodes[node.val]
        
        # print(nodes[start_node.val] is node,  nodes[start_node.val].val, node.val)
        # return nodes[start_node.val]
#         if not node: 
#             return node
        
#         stack = [node]
#         visited = set()

#         nodes = {
#             node.val: Node(node.val)
#         }
        
#         start_node = nodes[node.val]
        
#         while stack:
#             cur = stack.pop()
            
#             new_neighbors = []
            
#             for neighbor in cur.neighbors:
#                 if not neighbor.val in nodes:
#                     nodes[neighbor.val] = Node(neighbor.val)
#                 new_neighbors.append(nodes[neighbor.val])
                
#                 if not neighbor.val in visited:
#                     visited.add(neighbor.val)
#                     stack.append(neighbor)

#             nodes[cur.val] = Node(cur.val, new_neighbors)

#         # print(nodes[start_node.val] is node,  nodes[start_node.val].val, node.val)
#         return nodes[start_node.val]