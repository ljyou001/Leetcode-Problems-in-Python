class Solution_enum_middle_point:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(len(s)):
            left, right = i - 1, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.find_palin(s, i, i)
            res += self.find_palin(s, i, i + 1)
        return res

    def find_palin(self, s, left, right):
        res = 0
        while left > -1 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res