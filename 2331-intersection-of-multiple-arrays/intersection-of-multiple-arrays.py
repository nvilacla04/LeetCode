from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            for i in num:
                counts[i] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)