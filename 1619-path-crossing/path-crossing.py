class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {"N": [1,0], "S":[-1,0], "E":[0,1], "W":[0,-1]}
        curr = (0,0)
        visited = {curr}


        for direction in path:
            dx, dy = directions[direction]
            curr = (curr[0] + dx, curr[1] + dy)
            if curr in visited:
                return True
            else:
                visited.add(curr)

        if len(path) == len(visited)-1:
            return False