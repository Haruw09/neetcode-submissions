class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = dict()
        for i in range(len(s)):
            last_occurance[s[i]] = i
        
        i = 0
        result = []
        start = 0
        while i < len(s):
            start = i
            cur_end = last_occurance[s[i]]
            while i <= cur_end:
                cur_end = max(last_occurance[s[i]], cur_end)
                i += 1
            result.append(cur_end - start + 1)

        return result