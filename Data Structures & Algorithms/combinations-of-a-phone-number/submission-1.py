class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []
        cur = []
        str_len = len(digits)
        def backtrack(idx: int) -> None:
            if idx == str_len:
                if cur:
                    result.append(''.join(cur))
                return

            cur_letters = letters[digits[idx]]
            for letter in cur_letters:
                cur.append(letter)
                backtrack(idx + 1)
                cur.pop()
            
        backtrack(0)
        return result