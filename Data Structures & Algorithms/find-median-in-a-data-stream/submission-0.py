from heapq import heapify, heappush, heappop


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        heapify(self.max_heap)

        self.min_heap = []
        heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        while len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

        while len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        if not self.min_heap or len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        left = -self.max_heap[0]
        right = self.min_heap[0]
        return (left + right) / 2
        