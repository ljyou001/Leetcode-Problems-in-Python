MAPPING = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
}

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        if num < 0:
            num = 2 ** 32 + num
        return self.transfer(num)

    def transfer(self, num):
        num = abs(num)
        res = deque([])
        mod = 0
        while num > 0:
            mod = num % 16
            res.appendleft(MAPPING[mod])
            num = num // 16
        return ''.join(res)
