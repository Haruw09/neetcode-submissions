class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(left: int, right: int) -> int:
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -=1
                right += 1

            return result

        result = 0
        for i in range(len(s)):
            result += count_palindromes(i - 1, i)
            result += count_palindromes(i, i)

        return result

