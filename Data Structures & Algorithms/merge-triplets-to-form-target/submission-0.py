class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        max_a, max_b, max_c = 0, 0, 0
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                max_a = max(a, max_a)
                max_b = max(b, max_b)
                max_c = max(c, max_c)

        return [max_a, max_b, max_c] == target