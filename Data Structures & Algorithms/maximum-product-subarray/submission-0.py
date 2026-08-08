class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        result = nums[0]
        for num in nums[1:]:
            prev_min = min_prod
            prev_max = max_prod
            min_prod = min(num, num * prev_min, num * prev_max)
            max_prod = max(num, num * prev_min, num * prev_max)
            result = max(result, max_prod)

        return result