class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        if not words:
            return []

        prefixes = {}
        for word in words:
            self.get_prefixes(word, prefixes)

        res = []
        for word in words:
            score = self.count_prefixes(word, prefixes)
            res.append(score)
        return res
    
    def count_prefixes(self, word, prefixes):
        if not word:
            return 0

        prefix = ''
        score = 0
        for char in word:
            prefix += char
            score += prefixes[prefix]
        return score

    def get_prefixes(self, word, prefixes):
        if not word:
            return
        
        prefix = ''
        for char in word:
            prefix += char
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
        