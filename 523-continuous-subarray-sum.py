class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        psum = 0
        mods = {0: -1}
        for i in range(len(nums)):
            psum += nums[i]
            mod = psum % k
            if mod in mods and i - mods[mod] > 1:
                return True
            if not mod in mods:
                mods[mod] = i
        return False