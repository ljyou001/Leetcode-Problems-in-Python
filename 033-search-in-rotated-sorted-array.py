class SolutionBinarySearchWithMin:
    # lint 062
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return self.find_value(nums, target, 0, right)
        min_index = self.find_min_index(nums)
        if target < nums[right]:
            return self.find_value(nums, target, min_index, right)
        elif target > nums[right]:
            return self.find_value(nums, target, left, min_index - 1)
        else:
            return right
        
    def find_min_index(self, nums):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return left if nums[left] <= nums[right] \
                else right

    def find_value(self, nums, target, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
