class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i - 1][1] >= intervals[i][0]:
                new_start = intervals[i - 1][0]
                new_end = max(intervals[i - 1][1], intervals[i][1])
                intervals[i - 1:i + 1] = [[new_start, new_end]]
            else:
                i += 1

        return intervals
            