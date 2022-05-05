/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */


var hasCycle = function(head) {

    if (!head) return false;
    
    let shorter = head;
    let faster = head;
    
    while (faster.next && faster.next.next) {
        shorter = shorter.next;
        faster = faster.next.next;
        if (shorter === faster) return true;
    }
    
    return false;
};










var hasCycleOld = function(head) {

    if (!head) return false;
    
    let cur = head;
    

    while (cur && cur.next) {
        if (cur.visited === true) {
            return true;
        }
        cur.visited = true
        cur = cur.next;
    }
    return false;
    
};