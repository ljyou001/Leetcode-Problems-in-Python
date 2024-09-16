class Solution:
    def maxNumMoves(self, A) -> int:
        if len(A) < 2:
            return 0
        memo = {}
        first_two_sum = A[0] + A[1]
        last_two_sum = A[len(A) - 1] + A[len(A) - 2]
        first_last_sum = A[0] + A[len(A) - 1]

        return max(
            self.dfs(A, 0, len(A) - 1, first_two_sum, memo),
            self.dfs(A, 0, len(A) - 1, last_two_sum, memo),
            self.dfs(A, 0, len(A) - 1, first_last_sum, memo),
        )
    
    def dfs(self, arr, start, end, target, memo):
        if (start, end, target) in memo:
            return memo[(start, end, target)]
        
        if end - start < 1:
            return 0
        if not -1 < start < end < len(arr):
            return 0
        
        res = 0
        if arr[start] + arr[end] == target:
            res = max(res, self.dfs(arr, start + 1, end - 1, target, memo) + 1) 
        if arr[start] + arr[start + 1] == target:
            res = max(res, self.dfs(arr, start + 2, end, target, memo) + 1) 
        if arr[end] + arr[end - 1] == target:
            res = max(res, self.dfs(arr, start, end - 2, target, memo) + 1) 
        
        memo[(start, end, target)] = res
        return res
