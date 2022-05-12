# Back tracking method
# normally we can use hashtable

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