class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)
        deletions_num = 0
        first_free = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                deletions_num += 1
                continue

            prev = nums[i]
            nums[first_free] = nums[i]
            first_free += 1

        for _ in range(deletions_num):
            nums.pop()

        return len(nums)