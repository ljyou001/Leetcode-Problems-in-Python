class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            return res.append(path[:])

        path.append(nums[index])
        self.dfs(nums, index + 1, path, res)
        path.pop()
        # Skip all the same element, deduplicate.
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1
        self.dfs(nums, index + 1, path, res) 