class SolutionMemo:
    """
    This memo method will eventually overtime
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        memo = {}
        for i in range(len(envelopes)):
            self.dfs(envelopes, i, memo)
        return max(memo.values())
    
    def dfs(self, envelopes, index, memo):
        if index in memo:
            return memo[index]

        memo[index] = 1
        for i in range(len(envelopes)):
            if envelopes[i][0] < envelopes[index][0] and \
               envelopes[i][1] < envelopes[index][1]:
                memo[index] = max(
                    memo[index], 
                    1 + self.dfs(envelopes, i, memo),
                )
        return memo[index]

