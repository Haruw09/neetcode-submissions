import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first_max = heapq.heappop(stones)
            second_max = heapq.heappop(stones)
            if first_max - second_max:
                heapq.heappush(stones, first_max - second_max)
        
        return -stones[0] if stones else 0