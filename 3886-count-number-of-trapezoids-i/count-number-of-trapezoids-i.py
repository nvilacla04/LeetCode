from collections import Counter 

class Solution:
   def countTrapezoids(self, points: List[List[int]]) -> int:
        counts = Counter(y for x,y in points)

        segment = []

        for cnt in counts.values():
            if cnt >= 2:
                segment.append(cnt * (cnt - 1)//2)

        if len(segment) < 2:
            return 0

        total_seg_sum = sum(segment)
        sum_sq = sum(s * s for s in segment)
        trapezoids = (total_seg_sum * total_seg_sum - sum_sq) // 2

        return trapezoids % 1000000007

