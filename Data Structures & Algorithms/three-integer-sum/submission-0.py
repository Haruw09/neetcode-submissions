class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        counts = dict()

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        result = []
        
        for i in range(len(nums)):
            num_1 = nums[i]
            if i > 0 and num_1 == nums[i - 1]:
                continue
            counts[num_1] -= 1
            for j in range(i + 1, len(nums)):
                num_2 = nums[j]
                if counts[num_2] < 1 or (j > i + 1 and nums[j - 1] == num_2):
                    continue
                else:
                    counts[num_2] -= 1
                    num_3 = -(num_1 + num_2)
                    if num_3 >= num_2 and counts.get(num_3, 0) > 0:
                        result.append([num_1, num_2, num_3])
                        counts[num_2] += 1
                    else:
                        counts[num_2] += 1
            counts[num_1] += 1
        
        return result

