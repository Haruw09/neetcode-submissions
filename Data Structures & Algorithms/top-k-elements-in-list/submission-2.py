class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        result = []
        for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
            previous = key
            result.append(key)
            if len(result) == k:
                return result