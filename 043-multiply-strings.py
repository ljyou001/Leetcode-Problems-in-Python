class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.to_int(num1)
        num2 = self.to_int(num2)
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        res = []
        for i in range(len(num1)):
            multip1 = 10 ** i
            n1 = num1[i] * multip1
            for j in range(len(num2)):
                multip2 = 10 ** j
                n2 = num2[j] * multip2
                res.append(n1 * n2)
        
        return str(sum(res))

    def to_int(self, num):
        intlist = []
        for i in num:
            intlist.append(ord(i) - ord('0'))
        return intlist[::-1]