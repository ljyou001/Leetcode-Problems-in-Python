class Solution_slow:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) > 2:
            i = 0
            while i < len(nums) - 2:
                j = i + 1
                while j < len(nums) - 1:
                    k = j + 1
                    while k < len(nums):
                        if nums[i] < nums[k] < nums[j]:
                            return True
                        k += 1
                    j +=1
                i += 1
        return False

