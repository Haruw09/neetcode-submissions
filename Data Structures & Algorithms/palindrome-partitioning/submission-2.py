class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left: int, right: int) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        string_len = len(s)
        palindromes = [
            [False] * string_len
            for _ in range(string_len)
        ]
        for start in range(string_len):
            for end in range(start, string_len):
                palindromes[start][end] = is_palindrome(start, end)

        result = []
        cur = []
        
        def backtrack(start: int) -> None:
            if start == string_len:
                result.append(cur.copy())
                return

            for end in range(start, string_len):
                if palindromes[start][end]:
                    cur.append(s[start:end + 1])
                    backtrack(end + 1)
                    cur.pop()

            return

        backtrack(0)
        return result

                
