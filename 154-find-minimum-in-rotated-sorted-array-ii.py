class SolutionLeftSide:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            elif nums[left] > nums[mid]:
                right = mid
            else:
                left += 1

        return min(nums[left], nums[right])

class SolutionRightSide:
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid
            elif nums[right] > nums[mid]:
                right = mid
            else:
                right -= 1
        return min(nums[left], nums[right])