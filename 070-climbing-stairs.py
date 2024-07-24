

class SolutionMemorizationSearch:
    
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n == 0:
            return 1
        if n < 0 :
            return 0

        if n in memo:
            return memo[n]

        memo[n] = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
        
        return memo[n]


class SolutionMemorizationSearch:
    """
    static variable: not recommend, but can accelerate
    """
    memo = {}
    def climbStairs(self, n: int) -> int:
        return self.dfs(n)

    def dfs(self, n):
        if n == 0:
            return 1
        if n < 0 :
            return 0

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dfs(n - 1) + self.dfs(n - 2)

        return self.memo[n]

class SolutionReversedForLoop:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n] = 1
        if n - 1 > -1: 
            dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]

class SolutionForLoop:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class SolutionCircularArray:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 3
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]
        return dp[n % 3]