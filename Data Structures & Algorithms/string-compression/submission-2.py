class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            group_start = read
            while read < len(chars) and chars[read] == chars[group_start]:
                read += 1

            num = read - group_start
            chars[write] = chars[group_start]
            write += 1
            if num > 1:
                str_num = str(num)
                for i in range(len(str_num)):
                    chars[write] = str_num[i]
                    write += 1
            
        return write

