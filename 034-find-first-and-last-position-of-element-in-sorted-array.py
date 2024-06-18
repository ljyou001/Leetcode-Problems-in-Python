class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.find_first(nums, target), self.find_last(nums, target)]
        
    def find_first(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid 
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
    
    def find_last(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid 
            else:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1