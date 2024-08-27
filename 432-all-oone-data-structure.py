class Node:
    def __init__(self, prev=None, nxt=None, count=0, words=set([])):
        self.prev = prev
        self.next = nxt
        self.count = count
        self.words = words

class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node(self.head, None, 0)
        self.head.next = self.tail

        self.key_count = {}
        self.count_node = {}

    def inc(self, key: str) -> None:
        if key not in self.key_count:
            self.key_count[key] = 1
            if 1 in self.count_node:
                self.count_node[1].words.add(key)
            else:
                new_node = self._add_count_node(
                    self.head,
                    self.head.next,
                    1,
                    key,
                )
                self.count_node[1] = new_node
            return
        
        # if key in self.key_count
        ori_count = self.key_count[key]
        self.key_count[key] += 1
        new_count = self.key_count[key]
        self.count_node[ori_count].words.remove(key)

        prv_node = self.count_node[ori_count]
        nxt_node = self.count_node[ori_count].next
        
        if len(self.count_node[ori_count].words) == 0:
            prv_node = self.count_node[ori_count].prev
            self._delete_count_node(ori_count)
            del self.count_node[ori_count]
        
        if new_count in self.count_node:
            self.count_node[new_count].words.add(key)
        else:
            self.count_node[new_count] = self._add_count_node(
                prv_node,
                nxt_node,
                new_count,
                key,
            )
    
    def _add_count_node(self, prv, nxt, count, key):
        new_node = Node(prv, nxt, count, set([key]))
        prv.next = new_node
        nxt.prev = new_node
        return new_node

    def _delete_count_node(self, count):
        node_to_delete = self.count_node[count]
        prv = node_to_delete.prev
        nxt = node_to_delete.next
        prv.next = nxt
        nxt.prev = prv

    def dec(self, key: str) -> None:
        ori_count = self.key_count[key]
        self.key_count[key] -= 1
        new_count = self.key_count[key]

        node = self.count_node[ori_count]
        node.words.remove(key)
        
        if new_count == 0:
            del self.key_count[key]
        else:
            if new_count in self.count_node:
                self.count_node[new_count].words.add(key)
            else:
                self.count_node[new_count] = self._add_count_node(
                    node.prev,
                    node,
                    new_count,
                    key,
                )
        
        if not node.words:
            self._delete_count_node(ori_count)
            del self.count_node[ori_count]
        
        # ori_count = self.key_count[key]
        # self.key_count[key] -= 1

        # node = self.count_node[ori_count]
        # node.words.remove(key)
        # prv_node = node.prev
        # nxt_node = node
        # if not node.words:
        #     nxt_node = node.next
        #     self._delete_count_node(ori_count)
        #     del self.count_node[ori_count]
        
        # if self.key_count[key] == 0:
        #     del self.key_count[key]
        #     return
        
        # # if key still in self.key_count
        # new_count = self.key_count[key]
        # if new_count in self.count_node:
        #     self.count_node[new_count].words.add(key)
        # else:
        #     self.count_node[new_count] = self._add_count_node(
        #         prv_node,
        #         nxt_node,
        #         new_count,
        #         key,
        #     )

    def getMaxKey(self) -> str:
        if not self.tail.prev.words:
            return ''
        res = self.tail.prev.words.pop()
        self.tail.prev.words.add(res)
        return res

    def getMinKey(self) -> str:
        if not self.head.next.words:
            return ''
        res = self.head.next.words.pop()
        self.head.next.words.add(res)
        return res


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()