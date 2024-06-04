class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        temp = 0
        for i in s:
            if i == 'E':
                temp += 1
                chair = max(temp, chair)
            else:
                temp -= 1
        return chair