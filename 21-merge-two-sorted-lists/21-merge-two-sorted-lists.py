# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        tmp for other list
        
        '''
        if not list1: return list2
        elif not list2: return list1
        
        head = list1 if list1.val <= list2.val else list2
        a = head
        b = list1 if list1.val > list2.val else list2
        tmp = None
        
        while a and b:
            if a.next and (a.next.val <= b.val):
                a = a.next
            else:
                tmp = a.next
                a.next = b
                a = a.next
                b = tmp

            
        return head