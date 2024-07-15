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
        cur_ori = head

        while cur_ori:
            cur.next = RandomListNode(cur_ori.label)
            mapping[cur.next.label] = cur.next
            cur_ori = cur_ori.next
            cur = cur.next

        cur_ori = head
        cur = dummy.next
        while cur_ori:
            if cur_ori.random:
                random_label = cur_ori.random.label
                cur.random = mapping[random_label]
            cur = cur.next
            cur_ori = cur_ori.next

        return dummy.next