class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        cumulative_sum = 0
        sum_index_map = {0: -1}
        
        for i, num in enumerate(nums):
            cumulative_sum += 1 if num == 1 else -1
            
            if cumulative_sum in sum_index_map:
                length = i - sum_index_map[cumulative_sum]
                max_length = max(max_length, length)
            else:
                sum_index_map[cumulative_sum] = i
                
        return max_length
            