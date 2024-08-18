class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_direction(nums, mid) == 'left':
                right = mid
            elif self.get_direction(nums, mid) == 'right':
                left = mid
            else:
                return mid
        if nums[left] > nums[right]:
            return left
        return right

    def get_direction(self, nums, mid):
        if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            return 'peak'
        if nums[mid - 1] < nums[mid]:
            return 'right'
        if nums[mid - 1] > nums[mid]:
            return 'left' 