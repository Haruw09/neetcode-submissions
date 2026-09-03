class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(str(len(word)) + '#')
            result.append(word)

        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        p = 0
        result = []
        while p < len(s):
            first_digit = p
            while s[p] != '#':
                p += 1
            
            num = int(s[first_digit:p])
            p += 1
            word = s[p:p + num]

            result.append(word)
            p += num

        return result