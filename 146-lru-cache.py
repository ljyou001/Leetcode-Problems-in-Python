# Hashmap + Deque method
# Not the utilized method
class LRUCache:
    def __init__(self, capacity: int):
        from collections import deque
        self.cap = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache[key] 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.cap:
            leftkey = self.queue.popleft()
            del self.cache[leftkey]
        self.queue.append(key)
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Doubly Linked List
# Utilized method

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.keys = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def append(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        self.delete(self.keys[key])
        self.append(self.keys[key])
        return self.keys[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].value = value
            self.delete(self.keys[key])
        self.keys[key] = Node(key, value)
        self.append(self.keys[key])
        if len(self.keys) > self.cap:
            key_to_del = self.left.next.key
            self.delete(self.left.next)
            self.keys.pop(key_to_del)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)