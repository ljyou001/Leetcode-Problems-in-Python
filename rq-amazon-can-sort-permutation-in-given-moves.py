class Solution:
    # https://onlineboard.eu/b/mf6CWRjp
    def canSortPermutation(self, p: List[int], moves: List[int]):
        if not moves:
            return ''
        if not p:
            return '1' * len(p)

        min_swaps = self.get_min_swaps(p)
        print(min_swaps)
        res = ''
        for move in moves:
            if move >= min_swaps and move % 2 == min_swaps % 2:
                res += '1'
            else:
                res += '0'
        return res

    def get_min_swaps(self, p):
        visited = set()
        min_swaps = 0

        for i in range(len(p)):
            if i in visited:
                continue
            
            elements = 0
            j = i
            while j not in visited:
                visited.add(j)
                j = p[j] - 1
                elements += 1
            min_swaps += (elements - 1)
        return min_swaps
