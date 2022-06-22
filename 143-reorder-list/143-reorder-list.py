# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        slow, fast = head, head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
    
        cur, prev  = slow.next, None
        slow.next = None

        # reverse right half of list
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        
        # merge left and right halves
        left, right = head, prev
        while left and right:
            tmp = left.next
            left.next = right
            right = tmp
            left = left.next
            
        return head
        