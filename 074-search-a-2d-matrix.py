class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid
        row = left
        if matrix[right][0] <= target:
            row = right

        left = 0
        right = len(matrix[0]) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid
            elif matrix[row][mid] > target:
                right = mid
            else:
                return True
        
        if matrix[row][left] == target or matrix[row][right] == target:
            return True
        return False