class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            length = len(res) # if no limit here, the following loop will never end
            for j in range(length): # this will go through all the existing subsets in res, and add the new i to each of them
                newval = copy.deepcopy(res[j]) # need to use the copy, otherwise original value could be changed
                newval.append(i)
                res.append(newval)
        return res
# This is also called cascading method

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, path, res):
        if len(nums) == start:
            res.append(deepcopy(path))
            return
        
        path.append(nums[start])
        self.dfs(nums, start + 1, path, res)
        path.pop()
        self.dfs(nums, start + 1, path, res)