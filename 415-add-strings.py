class Solution:
    def str_to_ints(self, str):
        nums = []
        for i in str:
            nums.append(ord(i) - ord('0'))
        return nums[::-1]

    def addStrings(self, num1: str, num2: str) -> str:
        num1 = self.str_to_ints(num1)
        num2 = self.str_to_ints(num2)

        i = 0
        max_len = max(len(num1), len(num2))
        carry = 0
        res = []
        while i < max_len:
            this_res = carry
            if i < len(num1):
                this_res += num1[i]
            if i < len(num2):
                this_res += num2[i]
            if this_res >= 10:
                this_res -= 10
                carry = 1
            else:
                carry = 0
            res.append(this_res)
            i += 1

        if carry == 1:
            res.append(1)

        res = [str(i) for i in res]
        return ''.join(res[::-1])
        