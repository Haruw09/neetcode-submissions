class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest_seq = 1
        for num in nums:
            if num - 1 in nums:
                continue
            cur_seq = 1
            while (num + cur_seq) in nums:
                cur_seq += 1
            longest_seq = max(cur_seq, longest_seq)
        return max(cur_seq, longest_seq)