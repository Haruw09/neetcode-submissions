class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = [0] * 128
        for char in t:
            need[ord(char)] += 1

        best_start = -1
        left = 0
        best_len = float('inf')
        need_num = len(t)

        for right in range(len(s)):
            if need[ord(s[right])] > 0:
                need_num -= 1
            
            need[ord(s[right])] -= 1

            while need_num == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                need[ord(s[left])] += 1
                if need[ord(s[left])] > 0:
                    need_num += 1
                left += 1

        if best_len == float('inf'):
            return ''
        return s[best_start:best_start + best_len]
