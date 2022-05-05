class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        res = ListNode()
        res.next = head
        cur = res
        while cur.next != None and cur.next.next != None:
            newhead = head.next.next
            nxt = head.next
            nxt.next = head
            head.next = newhead
            cur.next = nxt
            cur = cur.next.next
            head = cur.next
        return res.next