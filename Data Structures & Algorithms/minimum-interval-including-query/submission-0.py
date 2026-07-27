class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda interval: interval[0])
        sorted_queries = sorted([(query, idx) for idx, query in enumerate(queries)])

        heap = []
        result = [-1] * len(queries)
        interval_idx = 0
        for query, real_idx in sorted_queries:
            while (
                interval_idx < len(intervals) 
                and intervals[interval_idx][0] <= query
            ):
                left, right = intervals[interval_idx]
                heapq.heappush(heap, (right - left + 1, right))
                interval_idx += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                result[real_idx] = heap[0][0]

        return result
