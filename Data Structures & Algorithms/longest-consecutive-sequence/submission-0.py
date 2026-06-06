class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        prev = nums[0]
        longest_seq = 1
        curr_seq = 1
        for num in nums[1:]:
            if num == prev:
                continue
            if num - prev == 1:
                curr_seq += 1
            else:
                longest_seq = max(curr_seq, longest_seq)
                curr_seq = 1
            prev = num
        return max(curr_seq, longest_seq)