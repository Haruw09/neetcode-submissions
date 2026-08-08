class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        reachable = [False] * (len(s) + 1)
        reachable[0] = True
        for start in range(len(s)):
            if not reachable[start]:
                continue
            for word in wordDict:
                if start + len(word) <= len(s) and s.startswith(word, start):
                    reachable[start + len(word)] = True

        return reachable[-1]