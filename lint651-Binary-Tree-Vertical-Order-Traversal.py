# Similar to 987

# Difference: 987 require to sort the values at the same point

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        dic = {}
        queue = collections.deque([(root, 0, 0)])
        while queue:
            cur, row, col = queue.popleft()
            if cur:
                if col in dic:
                    dic[col].append(cur.val)
                else:
                    dic[col] = [cur.val]
                queue.append((cur.left, row + 1, col - 1))
                queue.append((cur.right, row + 1, col + 1))
        return [dic[i] for i in sorted(dic.keys())]