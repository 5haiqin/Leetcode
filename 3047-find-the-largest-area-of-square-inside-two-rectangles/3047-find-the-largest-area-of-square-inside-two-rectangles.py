from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        best = 0

        for i in range(n):
            for j in range(i + 1, n):
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                right = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top = min(topRight[i][1], topRight[j][1])

                w = right - left
                h = top - bottom

                if w > 0 and h > 0:
                    side = min(w, h)
                    best = max(best, side * side)

        return best

