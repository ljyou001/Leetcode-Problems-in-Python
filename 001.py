class Solution_me:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        count = 0
        for i in nums:
            hash_table[i] = count
            count += 1
        print(hash_table)
        count = 0
        for i in nums:
            try:
                if count != hash_table[target-i]:
                    return [count, hash_table[target-i]]
            except:
                pass
            count += 1
        return 0