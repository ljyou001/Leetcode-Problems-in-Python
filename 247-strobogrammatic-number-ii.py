from typing import List
from collections import deque

MID_POS = set(['0', '1', '8'])
MAPPING = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
             we will sort your return value in output
    """
    def find_strobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        
        res = []
        path = deque()
        self.get_strobogrammatic(n, path, res)
        return res

    def get_strobogrammatic(self, n, path, res):
        if n == 0:
            return res.append(''.join(path))
        if n < 0:
            return
        
        if n % 2 == 1:
            for item in MID_POS:
                path.append(item)
                self.get_strobogrammatic(n - 1, path, res)
                path.pop()
        else:
            for key, value in MAPPING.items():
                if n == 2 and key == '0':
                    continue
                path.appendleft(key)
                path.append(value)
                self.get_strobogrammatic(n - 2, path, res)
                path.pop()
                path.popleft()