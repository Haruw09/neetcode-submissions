class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        prev_size = 0
        for i, num in enumerate(nums):
            cur_size = len(result)
            start = prev_size if i > 0 and nums[i] == nums[i - 1] else 0
            end = len(result)
            for j in range(start, end):
                result.append(result[j] + [num])

            prev_size = cur_size

        return result
        