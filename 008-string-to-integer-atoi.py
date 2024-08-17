class Solution:
    def myAtoi(self, s: str) -> int:
        DIGITS = set('0123456789')
        sign = 1
        res = 0
        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0

        if i < len(s) and s[i] == '+':
            i += 1
        elif i < len(s) and s[i] == '-':
            sign = -1
            i += 1

        MAX_VAL = 2**31 - 1
        MIN_VAL = 2**31 
        while i < len(s) and s[i] in DIGITS:
            res = res * 10 + ord(s[i]) - ord('0')
            if sign == 1 and res > MAX_VAL:
                return MAX_VAL
            elif sign == -1 and res > MIN_VAL:
                return -MIN_VAL
            i += 1
        return res * sign