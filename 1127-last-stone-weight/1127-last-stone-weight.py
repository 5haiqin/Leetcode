import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x != y:
                heapq.heappush(h, -(x - y))
        return -h[0] if h else 0
