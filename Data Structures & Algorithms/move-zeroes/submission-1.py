class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = 0
        i = 0
        while i < len(nums):
            while first_zero < len(nums) and nums[first_zero] != 0:
                first_zero += 1
            
            i = first_zero + 1
            while i < len(nums) and nums[i] == 0:
                i += 1

            if i < len(nums):
                nums[first_zero], nums[i] = nums[i], nums[first_zero]

        return None
        