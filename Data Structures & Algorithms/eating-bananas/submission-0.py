class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            if sum(math.ceil(pile / mid) for pile in piles) <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result