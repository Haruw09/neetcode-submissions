class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            num_1 = nums[i]
            if i > 0 and nums[i - 1] == num_1:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = -(nums[left] + nums[right])
                if target < num_1:
                    right -= 1
                elif target > num_1:
                    left += 1
                else:
                    result.append([num_1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result