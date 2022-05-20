# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Two pointer - using a slow and a fast pointer
        
        checking if value at each pointer is equal
        
        if not head: return False
        
        slow = head
        fast = head.next
        
        while fast:
            - compare slow.val and fast.val
                - return True if slow.val and fast.val are equal
            - increment slow by 1
            - increment fast by two

        return False
        
        while slow.val != fast.val:
            fast = fast.next.next
            slow = slow.next
            
        time complexity = O(n)
        '''
        
        if not head: return False
        
        slow = head
        fast = head.next
        
        while fast:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
            else: break
            
        return False
        
        