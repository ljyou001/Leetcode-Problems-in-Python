class TrieNode:
    def __init__(self):
        self.leaves = {}
        self.is_end = False

class TrieWithNodeMethod:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if not cur.leaves.get(char):
                cur.leaves[char] = TrieNode()
            cur = cur.leaves[char]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if not cur.leaves.get(char):
                return False
            cur = cur.leaves[char]
        return True if cur.is_end else False
            
    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if not cur.leaves.get(char):
                return False
            cur = cur.leaves[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class TrieHashtableMethod:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if not char in cur:
                cur[char] = {}
            cur = cur[char]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if not char in cur:
                return False
            cur = cur[char]
        return True if '*' in cur else False
            

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if not char in cur:
                return False
            cur = cur[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)