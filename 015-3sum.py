class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[j] + nums[k] + nums[i]
                
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1  #!!! Do not forget this, otherwise infinity in the loop
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < right and nums[left+1] == nums[left]:
                        left += 1
                    left += 1
                    right -= 1
                elif three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
            while i + 1 < len(nums) - 2 and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return res
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else: 
                    right -= 1
        return res