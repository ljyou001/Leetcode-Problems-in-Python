# Similar to lint 651

# Difference: lint 651 does not require to sort the value at the same point

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        queue = collections.deque([(root, 0, 0)])

        while queue:
            cur, row, col = queue.popleft()
            if cur:
                if col in dic and row in dic[col]:
                    dic[col][row].append(cur.val)
                elif col in dic:
                    dic[col][row] = [cur.val]
                else:
                    dic[col] = {}
                    dic[col][row] = [cur.val]
                queue.append((cur.left, row + 1, col - 1))
                queue.append((cur.right, row + 1, col + 1))

        for col in dic.keys():
            res = []
            for row in sorted(dic[col].keys()):
                res += sorted(dic[col][row])
            dic[col] = res
        return [dic[col] for col in sorted(dic.keys())]