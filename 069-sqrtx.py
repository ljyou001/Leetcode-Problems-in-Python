class Solution:
    # lint 141
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid
            else:
                right = mid
        if right * right <= x:
            ans = right
        return ans