class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels) 
        return sum(ch in jewels for ch in stones)
