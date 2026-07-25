class Solution:
    @staticmethod
    def square_dist(coords: list[int]) -> int:
        return coords[0] ** 2 + coords[1] ** 2

    def partition(self, nums: list, left: int, right: int) -> int:
            first_greater = left
            pivot_dist = self.square_dist(nums[right])
            for cur in range(left, right):
                if self.square_dist(nums[cur]) <= pivot_dist:
                    nums[cur], nums[first_greater] = nums[first_greater], nums[cur]
                    first_greater += 1

            nums[right], nums[first_greater] = nums[first_greater], nums[right]
            return first_greater

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left = 0
        right = len(points) - 1
        while left <= right:
            cur_partition = self.partition(points, left, right)
            if cur_partition > k:
                right = cur_partition - 1
            elif cur_partition < k:
                left = cur_partition + 1
            else:
                break

        return points[0:k]
        