"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        if not root:
            return 0
        return self.find_seq(root)[0]

    def find_seq(self, root):
        if not root:
            return 0, 0, 0
        rootmax, rootminus, rootplus = 0, 0, 0
        
        for child in root.children:
            childmax, childminus, childplus = self.find_seq(child)
            rootmax = max(rootmax, childmax)
            if child.val == root.val + 1:
                rootminus = max(childminus + 1, rootminus)
            if child.val == root.val - 1:
                rootplus = max(childplus + 1, rootplus)
        
        rootmax = max(
            rootminus + rootplus + 1,
            rootmax
        )
        return rootmax, rootminus, rootplus