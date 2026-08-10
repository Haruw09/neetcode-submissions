class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left: int, right: int) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        result = []
        cur = []
        string_len = len(s)
        def backtrack(start: int) -> None:
            if start == string_len:
                result.append(cur.copy())
                return

            for i in range(start, string_len):
                if is_palindrome(start, i):
                    cur.append(s[start:i + 1])
                    backtrack(i + 1)
                    cur.pop()

            return

        backtrack(0)
        return result

                
