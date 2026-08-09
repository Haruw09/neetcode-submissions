from math import sqrt, floor


class Solution:
    def numSquares(self, n: int) -> int:
        max_root = floor(sqrt(n)) 
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for cur_sum in range(len(dp)):
            cur_max_root = floor(sqrt(cur_sum)) 
            for root in range(cur_max_root + 1):
                dp[cur_sum] = min(dp[cur_sum - root ** 2] + 1, dp[cur_sum])

        return dp[-1]
