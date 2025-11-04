class Solution:
    from collections import Counter
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(k for k in freq.keys() if freq[k] == 1)