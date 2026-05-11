class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        mega_nums = []
        for num in nums:
            mega_nums.extend(int(digit) for digit in str(num))
        return mega_nums