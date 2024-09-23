MOD = 10**9 + 7

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        return self.dfs(steps, arrLen, 0, memo)

    def dfs(self, steps, length, now, memo):
        if now < 0 or now >= length:
            return 0
        if steps == 0:
            return 1 if now == 0 else 0
        if (steps, now) in memo:
            return memo[(steps, now)]
        
        memo[(steps, now)] = (
            self.dfs(steps - 1, length, now, memo) +
            self.dfs(steps - 1, length, now + 1, memo) +
            self.dfs(steps - 1, length, now - 1, memo)
        ) % MOD
        
        return memo[(steps, now)]