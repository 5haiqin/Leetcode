from typing import List

class Solution:
    def distanceBetweenBusStops(self, dist: List[int], a: int, b: int) -> int:
        total = sum(dist)
        if a > b:
            a, b = b, a
        d = 0
        for i in range(a, b):
            d += dist[i]
        return min(d, total - d)
