class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        return list(num_set)[0]

class Solution2:
    """
    @param a: An integer array
    @return: An integer
    """
    def single_number(self, a: List[int]) -> int:
        from collections import Counter
        num_list = Counter(a)
        for key, val in num_list.items():
            if val == 1:
                return key