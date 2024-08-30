

class Status:
    NOUSE = 0
    DELETED = 1

class SolutionIterDP:
    # https://onlineboard.eu/b/1PCUD7IJ
    def maximumSum(self, arr: List[int]) -> int:
        dp = [[float('-inf'), float('-inf')] for _ in range(len(arr) + 1)]
        res = float('-inf')

        for i in range(1, len(arr) + 1):
            dp[i][Status.NOUSE] = max(
                arr[i - 1], 
                dp[i - 1][Status.NOUSE] + arr[i - 1]
            )
            dp[i][Status.DELETED] = max(
                dp[i - 1][Status.NOUSE],
                dp[i - 1][Status.DELETED] + arr[i - 1],
                arr[i - 1],
            )

            res = max(max(dp[i]), res)

        return res

class SolutionIterDPMemUtil:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [
            [float('-inf'), float('-inf')], 
            [float('-inf'), float('-inf')],
        ]
        res = float('-inf')

        for i in range(1, len(arr) + 1):
            dp[i % 2][Status.NOUSE] = max(
                arr[i - 1], 
                dp[(i - 1) % 2][Status.NOUSE] + arr[i - 1]
            )
            dp[i % 2][Status.DELETED] = max(
                dp[(i - 1) % 2][Status.NOUSE],
                dp[(i - 1) % 2][Status.DELETED] + arr[i - 1],
                arr[i - 1],
            )

            res = max(max(dp[i % 2]), res)

        return res