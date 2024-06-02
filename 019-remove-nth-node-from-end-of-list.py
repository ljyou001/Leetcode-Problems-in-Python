class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        front = dummy
        for _ in range(n):
            front = front.next
        
        behind = dummy
        while front.next:
            front = front.next
            behind = behind.next
        
        behind.next = behind.next.next
        return dummy.next