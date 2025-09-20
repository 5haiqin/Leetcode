class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(rows):
            for j in range(cols):
                d = abs(i - r0) + abs(j - c0)
                res.append((d, i, j))
        res.sort(key=lambda x: x[0])
        ans = []
        for _, i, j in res:
            ans.append([i, j])
        return ans
