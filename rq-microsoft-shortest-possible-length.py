import heapq

class Solution:
    def shortestPossibleLength(self, S: str, K: int) -> int:
        if len(S) <= K or not S:
            return 0
        
        shortest_len = float('inf')
        for i in range(len(S) - K):
            left = S[:i]
            right = S[i + K:]
            new_string = left + right
            shortest_len = min(
                shortest_len,
                len(self.compress_string(new_string))
            )
        return shortest_len

    
    def compress_string(self, string):
        left = 0
        right = 0
        res = ''
        while right < len(string):
            while right < len(string) and string[right] == string[left]:
                right += 1
            length = right - left
            char = string[left]
            if length == 1:
                res += char
            else:
                res += str(length) + char

            left = right
        return res