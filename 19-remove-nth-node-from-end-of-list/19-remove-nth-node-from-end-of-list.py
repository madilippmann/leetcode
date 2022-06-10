# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''

        
        how many nodes are there
        naiive solution: 
        traverse through linked list and count how many nodes there are 
        - depending on the difference between n and the length of the linked list  we'll traverse again and do one of the three:
        
                - if the nth node is between two nodes: in which case we are going to point cur.next to cur.next.next
                - if the nth node is the last node: point cur to None
                - if the nth node is the first node: return head.next
                
        O(1) space complexity - storing single variable
        O(n) time complexity - traversing entire list 2 
        
        '''
        if not head.next: return None
        
        node_count = 0
        
        cur = head
        
        while cur:
            node_count += 1
            cur = cur.next
            
        nth_node = node_count - n 
        i = 0
        
        cur = head
        
        if n == 1: # removing tail
            print('entered 1')
            while cur and cur.next and cur.next.next:
                cur = cur.next
            cur.next = None
                    
        elif nth_node == 0: # removing head
            head = head.next
            print('entered 2')
            
        else: # removing inner node
            print('entered 3')
            
            while i < nth_node - 1:
                cur = cur.next
                i += 1
            
            cur.next = cur.next.next
            
        return head