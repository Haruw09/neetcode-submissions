class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]

            if dp[target]:
                return True

        return dp[target]
