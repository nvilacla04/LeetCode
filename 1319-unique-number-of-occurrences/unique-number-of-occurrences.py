class Solution:
    from collections import Counter
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        values = []
        freq = Counter(arr)
        for v in freq.values():
            if v not in values:
                values.append(v)
            else:
                return False

        return True