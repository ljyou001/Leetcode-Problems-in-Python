# LINT 960 

class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DataStream:

    def __init__(self):
        self.key_node = {}
        self.key_count = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def append_node(self, node):
        prv = self.tail.prev
        prv.next = node
        self.tail.prev = node
        node.prev = prv
        node.next = self.tail

    def add(self, num):
        if num in self.key_count:
            self.key_count[num] += 1
            if num in self.key_node:
                self.remove_node(self.key_node[num])
                del self.key_node[num]
            return
        self.key_count[num] = 1
        node = Node(num)
        self.key_node[num] = node
        self.append_node(node)
        
    def firstUnique(self):
        return self.head.next.val

        # cur = self.head.next
        # while self.key_count[cur.val] > 1:
        #     cur = cur.next
        # return cur.val