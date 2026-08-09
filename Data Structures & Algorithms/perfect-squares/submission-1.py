from math import sqrt, floor


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for cur_sum in range(1, len(dp)):
            cur_max_root = floor(sqrt(cur_sum)) 
            for root in range(1, cur_max_root + 1):
                dp[cur_sum] = min(dp[cur_sum - root ** 2] + 1, dp[cur_sum])

        return dp[-1]
