class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        pairs = 0

        for num in nums:
            if num in count:
                pairs += count[num]
                count[num] += 1

            else:
                count[num] = 1
            
        return pairs


    