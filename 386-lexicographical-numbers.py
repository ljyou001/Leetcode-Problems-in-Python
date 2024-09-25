class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        
        return res

    def dfs(self, num, n, res):
        if num > n:
            return
        res.append(num)
        
        for i in range(0, 10):
            self.dfs(10 * num + i, n, res)
            