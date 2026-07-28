class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        first = 1
        second = 1
        for _ in range(n - 1):
            result = first + second
            first = second
            second = result

        return result