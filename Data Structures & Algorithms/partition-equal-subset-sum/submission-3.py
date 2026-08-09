class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for cur_sum in range(target, num - 1, -1):
                dp[cur_sum] |= dp[cur_sum - num]

            if dp[target]:
                return True

        return False
