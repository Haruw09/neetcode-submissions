class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        i = 0
        while i < len(path):
            cur = []
            while i < len(path) and (char := path[i]) == '/':
                i += 1

            while i < len(path) and (char := path[i]) != '/':
                cur.append(char)
                i += 1

            cur = ''.join(cur)
            if cur == '..':
                if result:
                    result.pop()
            elif cur and cur != '.':
                result.append(cur)        

            i += 1

        return '/' + '/'.join(result)
                