class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(f'{len(string)}#{string}')
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        end = 0
        while end < len(s):
            if s[end] == '#':
                number = int(s[start:end])
                start = end + 1
                end = end + number + 1
                word = s[start:end]
                result.append(word)
                start = end
            else:
                end += 1
        return result

