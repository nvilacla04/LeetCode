class Solution:
    def countElements(self, arr: List[int]) -> int:
        n = set(arr)
        counter = 0
        for i in arr:
            if i+1 in n:
                counter += 1
        return counter
    