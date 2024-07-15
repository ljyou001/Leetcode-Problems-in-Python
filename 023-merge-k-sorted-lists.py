# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionBruteForce:
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

class SolutionCompareOneByOne:
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


class SolutionHeapMethod:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        dummy = ListNode()
        cur = dummy

        for li in lists:
            while li:
                heapq.heappush(heap, li.val)
                li = li.next

        while len(heap) > 0:
            print(cur)
            value = heapq.heappop(heap)
            cur.next = ListNode(val=value)
            cur = cur.next

        return dummy.next
        
class SolutionHeapLargeMem:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        dummy = ListNode()
        cur = dummy
        heap = []

        for i in range(len(lists)):
            if not lists[i]: 
                continue
            heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next
        
        while heap:
            node_value, index = heappop(heap)
            cur.next = ListNode(node_value)
            cur = cur.next
            if not lists[index]:
                continue
            heappush(heap, (lists[index].val, index))
            lists[index] = lists[index].next
            
        return dummy.next