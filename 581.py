class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        sorted_list = sorted(nums)
        left = 0
        right = len(nums) - 1
        res_left = 0
        while left <= right:
            if sorted_list[left] != nums[left]:
                break;
            left = left + 1
        while left <= right:
            if sorted_list[right] != nums[right]:
                break;
            right = right - 1
        return right - left + 1