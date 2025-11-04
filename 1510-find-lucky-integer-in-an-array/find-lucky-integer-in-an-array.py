class Solution:
    from collections import Counter
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        curr = -1
        for k in freq.keys():
            if k == freq[k]:
                same = k
                if same > curr:
                    curr = same
        return curr