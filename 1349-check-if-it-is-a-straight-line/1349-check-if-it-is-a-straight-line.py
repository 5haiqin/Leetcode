from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        dx1 = x1 - x0
        dy1 = y1 - y0

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if dx1 * (y - y0) != dy1 * (x - x0):
                return False

        return True
