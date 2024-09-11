# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head.next
        prv = head
        while cur:
            gcd = self.get_gcd(cur.val, prv.val)
            node = ListNode(gcd, cur)
            prv.next = node
            cur = cur.next
            prv = prv.next.next
        return dummy.next

    def get_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def get_gcd_1(self, a, b):
        min_val = min(a, b)
        for i in range(min_val, 0, -1):
            if a % i == 0 and b % i == 0:
                return i
        return i