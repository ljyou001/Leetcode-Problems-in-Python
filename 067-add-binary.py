class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b)) + 1
        a = a[::-1]
        b = b[::-1]
        addnext = 0
        res = ''
        
        for i in range(length):
            sumval = addnext
            if i < len(a):
                sumval += int(a[i])
            if i < len(b):
                sumval += int(b[i])
            addnext = 0
            if sumval > 1:
                addnext = 1
                sumval -= 2
            res += str(sumval)
        return str(int(res[::-1]))