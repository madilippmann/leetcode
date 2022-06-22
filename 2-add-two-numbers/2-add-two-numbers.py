# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        depth = 0
        l1_sum = 0
        l2_sum = 0
        
        while l1:
            l1_sum += (l1.val * 10**depth)
            depth += 1
            l1 = l1.next
        
        depth = 0
        
        while l2:
            l2_sum += (l2.val * 10**depth)
            depth += 1
            l2 = l2.next
            
        total_sum = l1_sum + l2_sum
        if total_sum == 0:
            return ListNode(0)
        
        head = None
        
        while total_sum:
            val = total_sum % 10
            total_sum //= 10

            next = ListNode(val)
            
            if not head: 
                head = next
                cur = head
            else:
                cur.next = next
                cur = next
                
        return head
                
            