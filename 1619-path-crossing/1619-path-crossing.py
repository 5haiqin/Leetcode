class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = {(0, 0)}
        for c in path:
            if c == 'N': y += 1
            elif c == 'S': y -= 1
            elif c == 'E': x += 1
            else: x -= 1  # 'W'
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
