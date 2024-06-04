class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        c = 0
        char = ""
        for i in word:
            if not char:
                char = i
                c = 1
            elif i != char:
                comp += (str(c) + char) if c > 0 else ''
                c = 1
                char = i
            else:
                c += 1
                if c == 9:
                    comp += ("9" + char)
                    c = 0
        if c > 0:
            comp += (str(c) + char)
        return comp