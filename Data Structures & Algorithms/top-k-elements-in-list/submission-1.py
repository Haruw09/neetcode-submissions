class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        result = []
        previous = None
        for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
            if key == previous:
                previous = key
                continue
            else:
                previous = key
                result.append(key)
                if len(result) == k:
                    return result