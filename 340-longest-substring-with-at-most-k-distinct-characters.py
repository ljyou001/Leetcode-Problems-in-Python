class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        # write your code here
        count = {}
        res = 0
        left = 0
        right = 0
        
        while right < len(s):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            while len(count) > k:
                char_to_del = s[left]
                count[char_to_del] -= 1
                if count[char_to_del] == 0:
                    del count[char_to_del]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res