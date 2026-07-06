class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.cur_min = val

        diff = val - self.cur_min
        self.stack.append(diff)
        if diff < 0:
            self.cur_min = val

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.cur_min -= diff

        if not self.stack:
            self.cur_min = None

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.cur_min
        return self.stack[-1] + self.cur_min

    def getMin(self) -> int:
        return self.cur_min