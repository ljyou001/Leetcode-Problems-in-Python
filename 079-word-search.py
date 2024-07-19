DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != word[0]:
                    continue
                if self.dfs(board, word[1:], set([(row, col)]), row, col):
                    return True
        return False

    def dfs(self, board, word, visited, x, y):
        if not word:
            # print('true')
            # res = True
            # Immutable values cannot be passed just like res list [] before
            return True
        
        first_char = word[0]
        for dx, dy in DIRECTIONS:
            newx, newy = x + dx, y + dy
            if not self.is_valid(board, visited, newx, newy):
                continue
            if board[newx][newy] == first_char:
                visited.add((newx, newy))
                if self.dfs(board, word[1:], visited, newx, newy):
                    return True
                visited.remove((newx, newy))
        return False

    def is_valid(self, board, visited, x, y):
        if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
            return False
        if (x, y) in visited:
            return False
        return True