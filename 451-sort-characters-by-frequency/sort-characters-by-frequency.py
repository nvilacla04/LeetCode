class Solution:
    from collections import Counter
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return "".join(ch * cnt for ch, cnt in pairs)