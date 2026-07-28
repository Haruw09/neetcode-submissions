class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first_house = nums[0]
        second_house = max(first_house, nums[1])
        for i in range(2, len(nums)):
            third_house = max(first_house + nums[i], second_house)
            first_house = second_house
            second_house = third_house

        return second_house