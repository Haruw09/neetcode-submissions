class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_sum = 0
        first_remainder_idx = dict()
        first_remainder_idx[0] = -1

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            if remainder in first_remainder_idx:
                if i - first_remainder_idx[remainder] > 1:
                    return True
            else:
                first_remainder_idx[remainder] = i

        return False
            