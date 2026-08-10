class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        len_nums = len(nums)
        def find_perm(start: int) -> None:
            if start == len_nums:
                result.append(nums.copy())
                return

            for i in range(start, len_nums):
                nums[start], nums[i] = nums[i], nums[start]
                find_perm(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

            return

        find_perm(0)
        return result