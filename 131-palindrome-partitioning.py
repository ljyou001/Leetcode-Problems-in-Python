class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, start, path, res):
        if start == len(s):
            return res.append(path[:])

        for i in range(start, len(s)):
            prefix = s[start:i + 1]
            if self.is_palindrome(prefix):
                path.append(prefix)
                self.dfs(s, i + 1, path, res)
                path.pop()

    def is_palindrome(self, string):
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True