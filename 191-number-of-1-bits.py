class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        res = 1
        while n > 1:
            if n % 2 == 1:
                res += 1
            n = n >> 1
            # use >> can divide by 2 quickly
        return res