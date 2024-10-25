class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] >= target:
                right = mid
        index = right
        if nums[left] == target:
            index = left

        res = []
        while index < len(nums) and nums[index] == target:
            res.append(index)
            index += 1
        return res