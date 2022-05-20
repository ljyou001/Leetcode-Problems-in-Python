# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(next=head)
        cur = head
        nxt = head.next
        
        while cur.next != None:
            if nxt.val >= cur.val:
                cur = nxt
                nxt = nxt.next
            else:
                tmp = res
                while nxt.val > tmp.next.val: # move the pointer until nxt<temp.next
                    tmp = tmp.next
                cur.next = nxt.next # link cur's next to nxt'next, get the nxt out of the linked list
                nxt.next = tmp.next # link the nxt's next to temp's next
                tmp.next = nxt # insert nxt to temp's next
                nxt = cur.next # get the nxt back to the current.next
        return res.next