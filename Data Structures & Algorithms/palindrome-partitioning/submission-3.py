class Solution:
    def partition(self, s: str) -> List[List[str]]:
        string_len = len(s)
        palindromes = [
            [False] * string_len
            for _ in range(string_len)
        ]

        for start in range(string_len - 1, -1, -1):
            for end in range(start, string_len):
                palindromes[start][end] = (
                    s[start] == s[end]
                    and (
                        end - start <= 2
                        or palindromes[start + 1][end - 1]
                    )
                )

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

                
