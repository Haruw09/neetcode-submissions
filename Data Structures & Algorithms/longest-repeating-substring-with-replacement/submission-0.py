class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0
        seen_in_window = dict()

        for right, char in enumerate(s):
            seen_in_window[char] = seen_in_window.get(char, 0) + 1
            max_freq = max(seen_in_window[char], max_freq)

            while (right - left + 1) - max_freq > k:
                seen_in_window[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)
        
        return max_length
