from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        result = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            result += prefix_sum[cur_sum - k]

            prefix_sum[cur_sum] += 1
            prev = cur_sum

        return result

