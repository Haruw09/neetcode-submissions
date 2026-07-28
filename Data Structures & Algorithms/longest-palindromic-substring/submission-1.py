class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        i = 0
        best_left = 0
        best_right = 0
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 2 > best_right - best_left:
                best_left = left + 1
                best_right = right - 1
        
        return s[best_left:best_right + 1].replace('#', '')
