class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        prev_start, prev_end = intervals[0]
        result = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] < prev_end:
                result += 1
            else:
                prev_start, prev_end = intervals[i]
            i += 1
            
        return result