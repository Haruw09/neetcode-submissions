class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        cur = []
        string_len = len(s)
        def backtrack(start: int) -> None:
            if start == string_len:
                result.append(cur.copy())
                return

            for i in range(start, string_len):
                new = s[start:i + 1]
                if new == new[::-1]:
                    cur.append(new)
                    backtrack(i + 1)
                    cur.pop()

            return

        backtrack(0)
        return result

                
