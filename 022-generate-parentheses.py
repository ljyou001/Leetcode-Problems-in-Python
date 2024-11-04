class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def generate(open_num, close_num):
            if open_num == close_num == n:
                res.append("".join(stack))
                return

            if open_num < n:
                stack.append('(')
                generate(open_num + 1, close_num)
                stack.pop()

            if close_num < open_num:
                stack.append(')')
                generate(open_num, close_num + 1)
                stack.pop()

        generate(0, 0)
        return res

class SolutionDFS:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ''
        self.dfs(n, n, '', res)
        return res

    def dfs(self, opens, closes, path, res):
        if opens == closes == 0:
            return res.append(path)
        
        if opens > 0:
            self.dfs(opens - 1, closes, path + '(', res)

        if closes > opens:
            self.dfs(opens, closes - 1, path + ')', res)
