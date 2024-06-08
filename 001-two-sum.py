class Solution_me:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        count = 0
        for i in nums:
            hash_table[i] = count
            count += 1
        count = 0
        for i in nums:
            try:
                if count != hash_table[target-i]:
                    return [count, hash_table[target-i]]
            except:
                pass
            count += 1
        return 0

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_count = {}
        for i in range(len(nums)):
            num_count[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in num_count and \
                i != num_count[target - nums[i]]:
                return [i, num_count[target - nums[i]]]