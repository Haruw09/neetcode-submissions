class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(nums: list[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            prev_prev = nums[0]
            prev = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                cur = max(prev_prev + nums[i], prev)
                prev_prev = prev
                prev = cur

            return max(prev_prev, prev)

        return max(rob_line(nums[:len(nums) - 1]), rob_line(nums[1:len(nums)]))