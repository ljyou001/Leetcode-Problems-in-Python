# 0, 1, 6 <-> 9, 8

# 010 len 3 mid 1
# 1111 len 4 mid 2

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def is_strobogrammatic(self, num: str) -> bool:
        if not num:
            return True

        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left = right = 0
        if len(num) % 2 == 1:
            left = right = len(num) // 2
        else:
            left = len(num) // 2 - 1
            right = len(num) // 2
        
        while left > -1:
            if num[left] in mapping and num[right] in mapping \
                and num[left] == mapping[num[right]]:
                left -= 1
                right += 1
                continue
            return False
        return True