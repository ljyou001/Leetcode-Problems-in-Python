# LINT 135

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # You need to sort candidates if forces acending order output in unsorted candidates
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, start, path, res):
        if target < 0:
            return
        if target == 0:
            return res.append(deepcopy(path))
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, target - nums[i], i, path, res)
            path.pop()