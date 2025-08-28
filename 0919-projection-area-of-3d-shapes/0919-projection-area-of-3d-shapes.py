class Solution:
    def projectionArea(self, g: List[List[int]]) -> int:
        n = len(g)
        a = 0  # total area

        for i in range(n):
            mr = 0  # max in row
            mc = 0  # max in column
            for j in range(n):
                if g[i][j]:
                    a += 1
                mr = max(mr, g[i][j])
                mc = max(mc, g[j][i])
            a += mr + mc

        return a
