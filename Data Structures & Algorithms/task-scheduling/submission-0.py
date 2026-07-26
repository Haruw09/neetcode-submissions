from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        max_frequency = max(frequencies.values())
        max_freq_num = sum(frequency == max_frequency for frequency in frequencies.values())
        return max(
            len(tasks),
            (max_frequency - 1) * (n + 1) + max_freq_num
        )