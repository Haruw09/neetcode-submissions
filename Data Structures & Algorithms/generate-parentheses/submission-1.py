class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = []
        result = []
        def backtrack(opened: int, closed: int) -> None:
            if closed == n and closed == opened:
                result.append(''.join(cur))
                return 
            elif closed == n:
                return

            if opened < n:
                cur.append('(')
                backtrack(opened + 1, closed)
                cur.pop()
            if closed < opened:
                cur.append(')')
                backtrack(opened, closed + 1)
                cur.pop()
        
        backtrack(0, 0)
        return result
