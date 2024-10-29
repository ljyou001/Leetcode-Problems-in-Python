class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0

        self.res = 0
        self.dfs(s, set(), 0)
        return self.res

    def dfs(self, s, seen, start):
        if len(seen) + (len(s) - start) <= self.res:
            # Pruning：如果剩下的字符都不如已经有的max val结果大
            return
        if start >= len(s):
            self.res = max(len(seen), self.res)
            return
        
        for i in range(start + 1, len(s) + 1):
            seg = s[start: i]
            if seg in seen:
                continue
            # if seg not in seen
            seen.add(seg)
            self.dfs(s, seen, i)
            seen.remove(seg)
