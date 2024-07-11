class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, set(), [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(path) == len(nums):
            return res.append(deepcopy(path))
        
        for i in range(len(nums)):
            if i in visited:
                continue
            visited.add(i)
            path.append(nums[i])
            self.dfs(nums, visited, path, res)
            path.pop()
            visited.remove(i)