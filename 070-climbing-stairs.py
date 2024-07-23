

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


