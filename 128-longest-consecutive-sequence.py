class Solution_sort:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        count = 1
        max_count = 1
        for i in range( len(nums) -1 ):
            if nums[i] != nums[i+1]:
                if nums[i] == nums[i+1] - 1:
                    count = count + 1
                    max_count = max(max_count, count)
                else: 
                    count = 1
        return max_count


class Solution_linear:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = set(nums)
        i = 0
        starts = []
        for i in nums:
            if i-1 not in nums:
                starts.append(i)
        res = starts
        for i in range(len(starts)):
            start = starts[i]
            res[i] = 1
            while start + 1 in nums:
                res[i] += 1
                start += 1
        return max(res)
            