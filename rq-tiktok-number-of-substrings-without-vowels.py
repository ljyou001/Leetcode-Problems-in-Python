VOWELS = set('aeiouAEIOU')

class Solution:
    def numberOfSubstringsWithoutVowels(self, s):
        res = set([])
        for i in range(len(s)):
            if s[i] in VOWELS:
                continue
            self.substring_from_here(s, i, res)
        return list(res)

    def substring_from_here(self, s, start, res):
        right = start
        while right < len(s):
            if s[right] in VOWELS:
                break
            res.add(s[start: right + 1])
            right += 1
