class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        strings, res = set(), set()
        for i in range(len(s)-9):
            if s[i:i + 10] in strings:
                res.add(s[i:i + 10])
            strings.add(s[i:i + 10])
        return res