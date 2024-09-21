


class SolutionBackTracking:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        if not s or not wordDict:
            return []
        res = []
        self.dfs(s, wordDict, 0, [], res)
        return res

    def dfs(self, s, word_set, start, path, res):
        if start == len(s):
            return res.append(' '.join(path))
        
        for i in range(start, len(s)):
            word = s[start:i + 1]
            if word in word_set:
                path.append(word)
                self.dfs(s, word_set, i + 1, path, res)
                path.pop()
        return