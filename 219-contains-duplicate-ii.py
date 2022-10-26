class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict.keys() and i - nums_dict[nums[i]] <= k:
                return True
            nums_dict[nums[i]] = i
        return False
    