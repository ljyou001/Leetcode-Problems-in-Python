class Solution:
    def reverseWords(self, s: str) -> str:
        spstr = s.split(" ")
        res = []
        for i in spstr:
            res.append( i[::-1] )
        return " ".join(res)