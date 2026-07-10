class TimeMap:

    def __init__(self):
        self.history = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.history:
            self.history[key] = [(timestamp, value)]
        else:
            self.history[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.history:
            return ''

        left = 0
        right = len(self.history[key]) - 1
        res_idx = None

        while left <= right:
            mid = (left + right) // 2
            if self.history[key][mid][0] == timestamp:
                return self.history[key][mid][1]

            elif self.history[key][mid][0] < timestamp:
                res_idx = mid
                left = mid + 1

            else:
                right = mid - 1

        return self.history[key][res_idx][1] if res_idx is not None else ''
