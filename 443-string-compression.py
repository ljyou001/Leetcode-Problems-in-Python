class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return ''

        res = 0
        left = right = 0
        left_char = chars[left]
        while right < len(chars):
            right_char = chars[right]
            if right_char != left_char:
                res_length = self.handling_comp(chars, res, left, right)
                res += res_length
                left = right
                left_char = chars[left]
            right += 1

        res_length = self.handling_comp(chars, res, left, right)
        res += res_length
        return res

    def handling_comp(self, chars, start, left, right):
        left_char = chars[left]
        if right - left == 1:
            chars[start] = left_char
            return 1
        # else:
        length = right - left
        res = left_char + str(right - left)

        for i in range(len(res)):
            chars[i + start] = res[i]

        return len(res)