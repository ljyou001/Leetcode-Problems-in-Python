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