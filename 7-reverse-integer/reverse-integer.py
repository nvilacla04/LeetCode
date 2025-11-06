class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        abs_x = abs(x)

        rev = 0
        while abs_x > 0:
            rev = rev * 10 + abs_x % 10
            abs_x //= 10

        return rev*sign if rev.bit_length() < 32 else 0