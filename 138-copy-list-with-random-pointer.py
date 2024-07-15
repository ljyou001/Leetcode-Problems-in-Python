"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Compare to lint 105
# This question does not have a ID in it
# You need to use a hash table to map the old to new directly
# Yes, class can be a hash key. Although list cannot.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next: 
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random: 
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]