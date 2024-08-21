# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CodecPreorderTraversal:
    def serialize(self, root):
        if not root:
            return ''
        res = []
        self._serialize(root, res)
        return ','.join(res)
        # [1,2,3,null,null,4,5]
        # to ['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']

    def _serialize(self, root, res):
        if not root:
            return res.append('N')
        
        res.append(str(root.val))
        self._serialize(root.left, res)
        self._serialize(root.right, res)

    def deserialize(self, data):
        if not data:
            return None
        data = deque(data.split(','))
        return self._deserialize(data)

    def _deserialize(self, data):
        if not data:
            return None

        thisval = data.popleft()
        node = TreeNode(int(thisval)) if thisval != 'N' else None
        if node:
            node.left = self._deserialize(data)
            node.right = self._deserialize(data)
        return node

class CodecPostorderTraversal:
    def serialize(self, root):
        if not root:
            return ''
        res = []
        self._serialize(root, res)
        return ','.join(res)
        # [1,2,3,null,null,4,5]
        # to ['N', 'N', '2', 'N', 'N', '4', 'N', 'N', '5', '3', '1']

    def _serialize(self, root, res):
        if not root:
            return res.append('N')
        
        self._serialize(root.left, res)
        self._serialize(root.right, res)
        res.append(str(root.val))

    def deserialize(self, data):
        if not data:
            return None
        data = data.split(',')
        return self._deserialize(data)

    def _deserialize(self, data):
        if not data:
            return None

        thisval = data.pop()
        node = TreeNode(int(thisval)) if thisval != 'N' else None
        if node:
            # 根据上面的输出可以看到后续遍历就是从右到左，基本跟前序遍历差不多
            node.right = self._deserialize(data)
            node.left = self._deserialize(data)
        return node

