# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        prev = None
        slow = head
        fast = head
        while True:
            # If at least k 
            count = 0
            while fast and count < k:
                fast = fast.next
                count += 1
            if count < k:
                # Not enough remaining in list
                break
                
            while slow != fast:
                # reverse
                nxt = slow.next
                slow.next = prev
                prev = slow
                slow = nxt

            # result collection
            while prev:
                cur.next = ListNode(prev.val)
                prev = prev.next
                cur = cur.next
            prev = None

        # len(list) < k
        if slow:
            cur.next = slow
        return dummy.next