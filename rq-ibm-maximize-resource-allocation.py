class Solution:
    def maximizeResourceAllocation(self, arr, k) -> int:
        if len(arr) < k:
            return -1
        total = sum(arr[0: k])
        max_val = total
        
        for i in range(k, len(arr)):
            total = total + arr[i] - arr[i - k]
            max_val = max(total, max_val)

        return max_val