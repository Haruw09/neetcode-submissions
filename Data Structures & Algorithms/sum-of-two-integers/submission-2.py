class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        max_int = (1 << 31) - 1
        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        return a if a <= max_int else ~(a ^ mask)