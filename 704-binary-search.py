#!!! Binary search basic method
# time: O(log(n))
# space: O(1)

class Solution_iteration:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # why <=: to ensure all possible boundry conditions are covered
            mid = (right - left) // 2 + left
            # calcualte the middle point first, 1st point of binary search
            # this is to prevent the left+right overflow
            # 2nd point of binary search: compare with the middle point
            if nums[mid] < target:
                left = mid + 1
                # +1 is to 
                # 1. ensure the search will not stuck in the middle point, if there is no result found
                # 2. ensure the target == nums[-1] can be covered, otherwise, while loop will stuck at nums[-2]
            elif nums[mid] > target:
                right = mid - 1
                # same as -1 above
            else:
                return mid
                # this one is the result matches the target
        
        return -1

class Solution_recursion:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
    def binary_search(self, nums, left, right, target):
        if right < left:
            return -1
        mid = (right - left) // 2 + left
        if nums[mid] < target:
            return self.binary_search(nums, mid + 1, right, target)
            # do not forget, always return a function, otherwise you will get a None result
        elif nums[mid] > target:
            return self.binary_search(nums, left, mid - 1, target)
            # do not forget, always return a function, otherwise you will get a None result
        else:
            return mid
