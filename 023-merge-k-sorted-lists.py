# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_brute_force:
    def mergeKLists(self, lists):
        nodes = []
        head = point = ListNode(0)
        for i in lists:
            while i:
                nodes.append(i.val)
                i = i.next
        for i in sorted(nodes):
            point.next = ListNode(i)
            point = point.next
        return head.next

class Solution_compare_one_by_one:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import sys

        if len(lists) == 0: return None
        res = ListNode()
        cur = res
        while True:
            index = -1
            val = sys.maxsize
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val < val:
                    index = i
                    val = lists[i].val
            if val == sys.maxsize: break
            cur.next = ListNode(val)
            cur = cur.next
            lists[index] = lists[index].next
        return res.next