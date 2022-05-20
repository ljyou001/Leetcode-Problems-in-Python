class Solution:
    def reverseVowels(self, s: str) -> str:
        exlist = 'aeiouAEIOU'
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] not in exlist:
                i += 1
            if s[j] not in exlist:
                j -= 1
            if s[i] in exlist and s[j] in exlist:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)