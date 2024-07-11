class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        match = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for i in range(len(digits)):
            tmp = []
            for j in res:
                for k in match[digits[i]]:
                    tmp.append(j + k)
            res = tmp
        return res


MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, [], res)
        return res

    def dfs(self, digits, index, path, res):
        if len(path) == len(digits):
            return res.append(''.join(path))
        for char in MAPPING[digits[index]]:
            path.append(char)
            self.dfs(digits, index + 1, path, res)
            path.pop()

