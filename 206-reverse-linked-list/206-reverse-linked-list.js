/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

/*

[1, 2, 3, 4, 5]

cur - initially set to head
prev - head
next - cur.next

while there are next nodes in list (next)
    cur.next - reassigned to prev
    cur - reassigned to cur.next
    next - cur.next
    

*/


var reverseList = function(head) {

    if (!head) return null;
    let cur = head;
    let prev = null;
    let next = cur.next;
    
    while (cur) {
        next = cur.next;
        cur.next = prev;
        prev = cur;
        cur = next;

    }
    
    return prev
}






























var reverseList2 = function(head) {
    let cur = head;
    let prev = null;
    let next;

    while (cur) {
        next = cur.next;
        cur.next = prev;
        prev = cur;
        cur = next;
    }

    head = prev;
    return head;
};