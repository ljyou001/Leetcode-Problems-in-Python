class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        return self.multiple(x, n)
        
    def multiple(self, x, n):
        if n == 0:
            return 1

        if n % 2 == 0:
            sub = self.multiple(x, n // 2)
            return sub * sub
        if n % 2 == 1:
            return self.multiple(x, n - 1) * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return self.multiple(x, n)
        
    def multiple(self, x, n):
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
                n -= 1
            else:
                x *= x
                n //= 2
        return res

