class Solution:
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