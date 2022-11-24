class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        chars = [[] for i in range(numRows)]
        row = 0
        go_down = 1
        for i in s:
            if row == numRows - 1:
                go_down = -1
            elif row == 0:
                go_down = 1
            
            chars[row].append(i)
            
            row += go_down
        
        string = ''
        for i in chars:
            string += ''.join(i)
        return string