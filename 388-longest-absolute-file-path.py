class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        print(lines)
        stack = []
        res = 0
        
        for line in lines:
            i = 0
            level = 1
            while i + 1 < len(line) and line[i] == '\t':
                i += 1
                level += 1

            while len(stack) >= level:
                stack.pop()
            stack.append(len(line) - i)
            if '.' in line:
                res = max(res, sum(stack) + level - 1)

        return res

# 注意
# 1. \t 和 \n 在字符里面都是占用一个位置而不是两个
# 2. 这个题目要求仅求文件的长度，也就是要带点，不然不要求长度