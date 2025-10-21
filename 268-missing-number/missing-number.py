class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i, v in enumerate(nums):
            n ^= i^v
        return n