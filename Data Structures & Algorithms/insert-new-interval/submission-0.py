class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = 0
        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1

        right = left
        merged_left, merged_right = newInterval
        while right < len(intervals) and intervals[right][0] <= newInterval[1]:
            merged_left = min(intervals[right][0], merged_left)
            merged_right = max(intervals[right][1], merged_right)
            right += 1

        intervals[left:right] = [[merged_left, merged_right]]
        return intervals