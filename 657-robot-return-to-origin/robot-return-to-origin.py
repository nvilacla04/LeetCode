class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dx = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
        dy = {'U': 1, 'D': -1, 'R': 0, 'L': 0}
        return sum(map(dx.get, moves)) == 0 and sum(map(dy.get, moves)) == 0