class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        # BFS template
        queue = deque([beginWord])
        distance = {beginWord: 1} # handling distance
        while queue:
            cur_word = queue.popleft()
            if endWord == cur_word:
                return distance[cur_word]
            for next_word in self.get_next_word(cur_word, wordList):
                # This is how the graph was composed(linked)
                if next_word in distance:
                    continue
                distance[next_word] = distance[cur_word] + 1
                queue.append(next_word)
        return 0
    
    def get_next_word(self, word, wordList):
        """
        """
        words = []
        ALPHABET = set('qwertyuiopasdfghjklzxcvbnm')
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in ALPHABET:
                if char == word[i]:
                    continue
                if (left + char + right) in wordList:
                    words.append((left + char + right))
        return words