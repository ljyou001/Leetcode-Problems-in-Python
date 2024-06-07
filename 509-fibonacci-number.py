class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        n1 = 0
        n2 = 1

        for _ in range(2, n + 1):
            old_n2 = n2
            n2 = n1 + n2
            n1 = old_n2

        return n2            