class SolutionSlow:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if not s or len(s) < len(p):
            return res
        p_counter = Counter(p)
        # string_count = Counter(s[:len(p)])
        # if string_count == p:
        #     res.append(0)
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:i+len(p)]) == p_counter:
                res.append(i)
        return res

class SolutionFast:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if not s or len(s) < len(p):
            return res
        p_counter = self.count_string(p)
        s_count = self.count_string(s[:len(p)])
        if s_count == p_counter:
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            s_count[ord(s[i - 1]) - ord('a')] -= 1
            s_count[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if s_count == p_counter:
                res.append(i)
        return res

    def count_string(self, string):
        LENGTH_ALPHABET = 26
        count = [0 for _ in range(LENGTH_ALPHABET)]
        for char in string:
            count[ord(char) - ord('a')] += 1
        return count