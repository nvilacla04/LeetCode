class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        max_new = -1
        for num, count in freq.items():
            if count == 1:
                max_new = max(max_new, num)
        return max_new