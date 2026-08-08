from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for i in range(len(nums)):
            idx = bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
        
        return len(tails)