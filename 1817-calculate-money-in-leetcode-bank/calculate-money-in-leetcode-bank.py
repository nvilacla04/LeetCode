class Solution:
    def totalMoney(self, n: int) -> int:
        q = n//7 
        r = n%7

        return (r * (q + 1) + r * (r - 1) // 2) + (q * (7 * q + 49) // 2)