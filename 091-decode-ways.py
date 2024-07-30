class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        self.dfs(s, 0, memo)
        return memo[0]

    def dfs(self, s, index, memo):
        if index == len(s):
            return 1
        if index > len(s):
            return 0

        if index in memo:
            return memo[index]

        memo[index] = 0
        if s[index] == '0':
            memo[index] = 0
            return 0
        memo[index] += self.dfs(s, index + 1, memo)
        if s[index] == '1' or (index + 1 < len(s) \
            and s[index] == '2' and int(s[index + 1]) < 7): 
            memo[index] += self.dfs(s, index + 2, memo)
        return memo[index]