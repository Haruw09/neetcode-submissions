class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        mp = defaultdict(int)
        longest_seq = 1
        for num in nums:
            cur_seq = mp[num - 1] + mp[num + 1] + 1
            mp[num] = cur_seq
            mp[num - mp[num - 1]] = cur_seq
            mp[num + mp[num + 1]] = cur_seq
            longest_seq = max(cur_seq, longest_seq)
        return longest_seq