# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CodecPreorderTraversal:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        self._serialize(root, res)
        return ','.join(res)

    def _serialize(self, root, res):
        if not root:
            return res.append('N')
        
        res.append(str(root.val))
        self._serialize(root.left, res)
        self._serialize(root.right, res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
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

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))