class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        frequencies_and_nums = [[] for _ in range(len(nums) + 1)]
        for num, frequency in counts.items():
            frequencies_and_nums[frequency].append(num)

        result = []
        for i in range(len(frequencies_and_nums) - 1, -1, -1):
            for num in frequencies_and_nums[i]:
                result.append(num)
                if len(result) == k:
                    return result