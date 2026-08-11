class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first_free = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[first_free - 1]:
                continue

            nums[first_free] = nums[i]
            first_free += 1

        return first_free