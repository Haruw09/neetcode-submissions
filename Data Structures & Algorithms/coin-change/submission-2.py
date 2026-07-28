from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] + [float('inf')] * amount
        for i in range(len(dp)):
            min_coins = dp[i]
            for coin in coins:
                if i - coin >= 0:
                    min_coins = min(min_coins, dp[i - coin] + 1)

            dp[i] = min_coins

        return dp[-1] if dp[-1] != float('inf') else -1