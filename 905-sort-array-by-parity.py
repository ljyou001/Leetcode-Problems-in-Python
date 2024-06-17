class Solution_me:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd

class Solution_Github:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)

class SolutionPartition:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 0:
                left += 1
            while left <= right and nums[right] % 2 != 0:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums