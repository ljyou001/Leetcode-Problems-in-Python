class Solution:
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        res = []
        a.sort()
        self.dfs(a, k, target, 0, [], res)
        return res

    def dfs(self, a, k, target, start, path, res):
        if k == target == 0:
            return res.append(path[:])
        if k < 0 or target < 0:
            return
        
        for i in range(start, len(a)):
            path.append(a[i])
            self.dfs(
                a,
                k - 1,
                target - a[i],
                i + 1,
                path,
                res,
            )
            path.pop()