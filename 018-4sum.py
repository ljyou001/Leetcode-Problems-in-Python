class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        i = 0
        
        while i < len(nums) - 3:
            start = nums[i]
            res.extend(self.threeSum(nums[i], nums[i+1: len(nums)], target - start))
            while i + 1 < len(nums) and nums[i+1] == start:
                i += 1
            i += 1
        return res
    
    def threeSum(self, start_val, numList, target):
        res = []
        
        for j in range(len(numList)):
            if j > 0 and numList[j-1] == numList[j]:
                continue
            left = j + 1
            right = len(numList) - 1
            while left < right:
                threeSum = numList[j] + numList[left] + numList[right]
                if threeSum == target:
                    res.append([start_val, numList[j], numList[left], numList[right]])
                    left += 1
                    while numList[left] == numList[left - 1] and left < right:
                        left += 1
                elif threeSum < target:
                    left += 1
                elif threeSum > target:
                    right -= 1
        return res