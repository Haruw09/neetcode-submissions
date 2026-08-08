class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1

        prev_prev = 1
        prev = 0 if s[1] == '0' else 1
        if 10 <= int(s[0:2]) <= 26:
            prev += prev_prev

        for i in range(2, len(s)):
            cur = 0
            if int(s[i]) != 0:
                cur += prev

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                cur += prev_prev

            prev_prev = prev
            prev = cur

        return prev
            