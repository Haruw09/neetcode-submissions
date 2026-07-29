class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = []
        result = []
        opened = 0
        closed = 0
        def backtrack(cur: list, opened: int, closed: int) -> None:
            if closed == n and closed == opened:
                result.append(''.join(cur))
                return 
            elif closed == n:
                return

            if opened < n:
                if closed < opened:
                    cur.append(')')
                    backtrack(cur, opened, closed + 1)
                    cur.pop()
                cur.append('(')
                backtrack(cur, opened + 1, closed)
                cur.pop()
            else:
                cur.append(')')
                backtrack(cur, opened, closed + 1)
                cur.pop()
        
        backtrack(cur, opened, closed)
        return result
