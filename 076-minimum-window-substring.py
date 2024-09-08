class SolutionTwoPointerWithMissing:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        missing = len(t)
        t = Counter(t)
        left = right = 0
        res = (-1, -1)
        length = float('inf')

        while right < len(s):
            if s[right] in t:
                t[s[right]] -= 1
                if t[s[right]] >= 0:
                    missing -= 1
            while left <= right and missing == 0:
                print(left, right)
                if right + 1 - left < length:
                    length = right + 1 - left
                    res = (left, right + 1)
                if s[left] in t:
                    t[s[left]] += 1
                    if t[s[left]] > 0:
                        missing += 1
                left += 1
            right += 1
        return s[res[0]: res[1]]

class SolutionTwoPointer:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        t = Counter(t)
        left = right = 0
        s_table = {}
        res = ''
        length = float('inf')
        while right < len(s):
            s_table[s[right]] = s_table.get(s[right], 0) + 1
            while left <= right and self.is_cover(s_table, t):
                if right + 1 - left < length:
                    length = right + 1 - left
                    res = s[left:right + 1]
                s_table[s[left]] -= 1
                left += 1
            right += 1
        return res

    def is_cover(self, s, t):
        for key in t.keys():
            if key not in s:
                return False
            if s[key] < t[key]:
                return False
        return True