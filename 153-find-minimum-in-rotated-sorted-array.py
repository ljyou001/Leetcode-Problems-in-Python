class Solution:
    # lint 159
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return nums[left] if nums[left] <= nums[right]\
                else nums[right]