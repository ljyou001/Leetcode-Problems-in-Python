# LINT 010

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        table = {}
        res = []
        for i in nums:
            if i in table.keys():
                table[i] += 1
            else:
                table[i] = 1
        self.backtracking(nums, res, table, [])
        return res
    
    def backtracking(self, nums, res, table, comb):
        if len(nums) == len(comb):
            res.append(list(comb))
            return
        
        for num in table:
            if table[num] > 0:
                comb.append(num)
                table[num] -= 1
                self.backtracking(nums, res, table, comb)
                comb.pop()
                table[num] += 1

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, set(), [], res)
        return res

    def dfs(self, nums, visited_index, path, res):
        if len(path) == len(nums):
            return res.append(deepcopy(path))

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and \
                i - 1 not in visited_index:
                continue
            if i in visited_index:
                continue
            visited_index.add(i)
            path.append(nums[i])
            self.dfs(nums, visited_index, path, res)
            visited_index.remove(i)
            path.pop()

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        visited = [False] * len(nums)
        res = []
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(path) == len(nums):
            res.append(deepcopy(path))
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                continue
            visited[i] = True
            path.append(nums[i])
            self.dfs(nums, visited, path, res)
            visited[i] = False
            path.pop()