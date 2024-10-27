# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not n:
            return 0

        left = 0
        right = n

        while left + 1 < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid
        return left if isBadVersion(left) else right