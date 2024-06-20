class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0
        right = 1 + x
        for _ in range(100):
            mid = (left + right) / 2
            if mid * mid < x:
                left = mid
            else:
                right = mid
        return left