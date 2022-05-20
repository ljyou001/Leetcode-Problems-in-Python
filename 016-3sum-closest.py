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