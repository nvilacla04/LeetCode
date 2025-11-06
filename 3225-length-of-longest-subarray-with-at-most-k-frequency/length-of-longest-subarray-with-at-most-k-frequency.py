class Solution:
    from collections import Counter
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        L = 0 
        best = 0
        freq = {}

        for R,x in enumerate(nums):
            freq[x] = freq.get(x, 0) +1

            #shrink window
            while freq.get(x, 0) > k:
                left = nums[L]
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]
                L += 1

            if R-L+1 > best:
                best = R-L+1 
        return best


