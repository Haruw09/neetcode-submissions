from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        for start in sorted(counts):
            groups_num = counts[start]
            if groups_num == 0:
                continue

            for i in range(start, start + groupSize):
                if i not in counts or counts[i] < groups_num:
                    return False

                counts[i] -= groups_num

        return True
