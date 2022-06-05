# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        
        while cur:
            cur.a = True
            cur = cur.next
            
        cur = headB
        
        while cur:
            if hasattr(cur, 'a'):
                return cur
            cur = cur.next
            
        return
            
        
        