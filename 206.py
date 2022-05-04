class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return None
        if head.next == None:
            return head
        elem = []
        while head != None:
            elem.append(head.val)
            head = head.next
        res = ListNode()
        cur = res
        elem = elem[::-1]
        for i in elem:
            cur.next = ListNode(i) 
            cur = cur.next
        return res.next

class Solution_iter:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

