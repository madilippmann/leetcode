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
    const nodes = {}

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