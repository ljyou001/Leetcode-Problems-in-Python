class Solution:
    def reverse(self, x: int) -> int:
        print(2**31)
        if x < 0:
            res = int( str(x)[1:][::-1] ) * -1
            if res > -2147483647: return res
            else: return 0
        else: 
            res = int( str(x)[::-1] )
            if res < 2147483647: return res
            else: return 0