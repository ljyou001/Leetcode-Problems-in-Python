from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""

class Solution:
    """
    @param root: the root of the tree
    @return: Maximum diameter of the N-ary Tree
    """
    def diameter(self, root: UndirectedGraphNode) -> int:
        if not root:
            return 0
        return self.dfs(root)[0]

    def dfs(self, root):
        diameter = 0
        longest = 0
        longest2 = 0
        for child in root.neighbors:
            child_dia, child_longest = self.dfs(child)
            diameter = max(child_dia, diameter)
            if child_longest >= longest:
                tmp = longest
                longest = child_longest
                if tmp > longest2:
                    longest2 = tmp
            elif child_longest > longest2:
                longest2 = child_longest
        
        diameter = max(diameter, longest + longest2)
        return diameter, longest + 1
