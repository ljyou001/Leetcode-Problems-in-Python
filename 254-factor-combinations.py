# LINT 1308

class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        res = []
        self.dfs(n, 2, [], res)
        res.pop()
        return res

    def dfs(self, n, start, path, res):
        if n == 1:
            return res.append(path[:])
        if n < 1:
            return

        for i in range(start, n + 1):
            if n % i != 0:
                continue
            path.append(i)
            self.dfs(int(n / i), i, path, res)
            path.pop()


class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        res = []
        factors = self.find_all_factors(n)
        self.dfs(n, factors, 0, [], res)
        return res

    def find_all_factors(self, n):
        return [
            i 
            for i in range(2, n) 
            if n % i == 0 
        ]

    def dfs(self, n, factors, start, path, res):
        if n == 1:
            return res.append(path[:])
        if n < 1:
            return

        for i in range(start, len(factors)):
            if n % factors[i] != 0:
                continue
            path.append(factors[i])
            self.dfs(n // factors[i], factors, i, path, res)
            path.pop()