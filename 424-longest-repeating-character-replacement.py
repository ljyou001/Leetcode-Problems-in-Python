class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        res = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            major_char, minor_nums = self.parse_count(count)
            while minor_nums > k:
                count[s[left]] -= 1
                major_char, minor_nums = self.parse_count(count)
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

    def parse_count(self, count):
        major_char = ''
        major_nums = 0
        minor_nums = 0
        for char, num in count.items():
            if not major_char or major_nums < num:
                minor_nums += major_nums
                major_char = char
                major_nums = num
            else:
                minor_nums += count[char]
        return major_char, minor_nums