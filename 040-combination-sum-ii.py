class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, set(), 0, [], res)
        return res

    def dfs(self, nums, target, visited, start, path, res):
        if target < 0:
            return
        if target == 0:
            return res.append(path[:])
        
        for i in range(start, len(nums)):
            if i > 0 and nums[i - 1] == nums[i] and i - 1 not in visited:
                continue
            path.append(nums[i])
            visited.add(i)
            self.dfs(
                nums, 
                target - nums[i],
                visited,
                i + 1,
                path, 
                res,
            )
            path.pop()
            visited.discard(i)