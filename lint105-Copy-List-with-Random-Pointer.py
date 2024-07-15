"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        cur = dummy
        mapping = {}
        cur_old = head

        while cur_old:
            cur.next = RandomListNode(cur_old.label)
            mapping[cur.next.label] = cur.next
            cur_old = cur_old.next
            cur = cur.next

        cur_old = head
        cur = dummy.next
        while cur_old:
            if cur_old.random:
                random_label = cur_old.random.label
                cur.random = mapping[random_label]
            cur = cur.next
            cur_old = cur_old.next

        return dummy.next