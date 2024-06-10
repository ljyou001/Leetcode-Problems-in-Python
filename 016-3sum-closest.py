class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        res = nums[0] + nums[1] + nums[len(nums) - 1]
        bias = abs(res - target)
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                new_bias = abs(three_sum - target)
                if three_sum == target:
                    return target
                elif three_sum < target:
                    left += 1
                    if new_bias < bias:
                        bias = new_bias
                        res = three_sum
                elif three_sum > target:
                    right -= 1
                    if new_bias < bias:
                        bias = new_bias
                        res = three_sum
        return res

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dis = 114514
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == target:
                    return target
                elif threesum < target:
                    j += 1
                    if abs(threesum - target) < dis:
                        dis = abs(threesum - target)
                        res = threesum
                else:
                    k -= 1
                    if abs(threesum - target) < dis:
                        dis = abs(threesum - target)
                        res = threesum
        return res

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[len(nums) - 1]

        for ind in range(len(nums) - 2):
            left = ind + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[ind] + nums[left] + nums[right]
                if abs(three_sum - target) < abs(res - target):
                    res = three_sum
                if three_sum > target:
                    right -= 1
                elif three_sum < target:
                    left += 1
                else:
                    return three_sum
        return res