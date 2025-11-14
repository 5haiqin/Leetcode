class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e = sum(p % 2 == 0 for p in position)
        o = len(position) - e
        return min(e, o)
