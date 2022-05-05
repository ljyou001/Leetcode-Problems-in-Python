class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            res = {}
            for j in i:
                if j != "." and j not in res.keys():
                    res[j] = 1
                elif j != "." and j in res.keys():
                    return False
        for i in range(len(board)):
            res = {}
            for j in board:
                if j[i] != "." and j[i] not in res.keys():
                    res[j[i]] = 1
                elif j[i] != "." and j[i] in res.keys():
                    return False
        for x in range(0,3):
            for y in range(0,3):
                new_array = board[3*y][3*x:3*x+3] + board[3*y+1][3*x:3*x+3] + board[3*y+2][3*x:3*x+3]
                # Here about the list, [0,1,2,3,4,5] only when you use [0,3], then you can have [0,1,2], the last pointer is not included, mathmatically [x,y).
                print(new_array)
                res = {} # Put this one outside, otherwise, no elements in res
                for i in new_array:
                    if i != '.' and i not in res.keys():
                        res[i] = 1
                    elif i != '.' and i in res.keys():
                        return False
        return True
