class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * (len(matrix[0]) + 1)]
        for row in range(1, len(matrix) + 1):
            self.prefix.append([0])
            for col in range(1, len(matrix[0]) + 1):
                self.prefix[row].append(
                    matrix[row - 1][col - 1] + \
                    self.prefix[row - 1][col] + \
                    self.prefix[row][col - 1] - \
                    self.prefix[row - 1][col - 1]
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] - \
               self.prefix[row1][col2 + 1] - \
               self.prefix[row2 + 1][col1] + \
               self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# DRAW A PICTURE IF YOU CANNOT UNDERSTAND!