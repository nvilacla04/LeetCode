from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_table = Counter(nums)
        max_freq = max(freq_table.values())
        return sum(v for v in freq_table.values() if v == max_freq)