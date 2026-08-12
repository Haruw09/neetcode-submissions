class Solution:
    def reverse(self, x: int) -> int:
        max_int = (1 << 30) | ((1 << 30) - 1)
        min_int = -max_int - 1

        if x == min_int:
            return 0

        max_cur_result = max_int // 10
        max_cur_x = max_int % 10

        result = 0
        sign = -1 if x < 0 else 1

        x = abs(x)

        while x:
            if result > max_cur_result:
                return 0
            
            if result == max_cur_result:
                if sign == 1 and x % 10 > max_cur_x:
                    return 0
                if sign == -1 and x % 10 > max_cur_x + 1:
                    return 0

            result *= 10
            result += x % 10
            x //= 10

        return result * sign

                