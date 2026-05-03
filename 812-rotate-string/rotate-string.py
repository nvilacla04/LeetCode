class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if sum(ord(c) for c in s) == sum(ord(c) for c in goal):
            if goal in s+s:
                return True 
            return False
        else:
            return False 