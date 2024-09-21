class SolutionDP:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        n = min(10, n)

        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 9
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)
        return sum(dp)

class SolutionMath:
    def count_numbers_with_unique_digits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res