class Solution_me:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addnext = 0
        sumval = 0
        res = ListNode()
        cur = res
        while l1 != None and l2 != None:
            sumval = addnext + l1.val + l2.val
            cur.next = ListNode(sumval % 10)
            addnext = sumval // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            sumval = addnext + l1.val
            cur.next = ListNode(sumval % 10)
            addnext = sumval // 10
            cur = cur.next
            l1 = l1.next
        while l2 != None:
            sumval = addnext + l2.val
            cur.next = ListNode(sumval % 10)
            addnext = sumval // 10
            cur = cur.next
            l2 = l2.next
        if addnext != 0:
            cur.next = ListNode(addnext)
        return res.next

class Solution_Github:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addnext = 0
        sumval = 0
        res = ListNode()
        cur = res
        while l1 != None or l2 != None:
            if l1 != None:
                sumval += l1.val
                l1 = l1.next
            if l2 != None:
                sumval += l2.val
                l2 = l2.next
            cur.next = ListNode(sumval % 10)
            addnext = sumval // 10
            cur = cur.next
        if addnext != 0:
            cur.next = ListNode(addnext)
        return res.next