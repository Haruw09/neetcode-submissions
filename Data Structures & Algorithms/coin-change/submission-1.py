from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def coins_need(n: int | float) -> int | float:
            if n == 0:
                return 0

            if n < coins[0]:
                return float('inf')

            return min([coins_need(n - coin) for coin in coins]) + 1

        result = coins_need(amount)
        return result if result != float('inf') else -1