class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        
        while left <= right:
            cur = (left + right) // 2
            sum_val = 0
            
            sum_val = sum(num <= cur for num in nums)
            if sum_val > cur:
                dup = cur
                right = cur - 1
            else:
                left = cur + 1
        
        return dup