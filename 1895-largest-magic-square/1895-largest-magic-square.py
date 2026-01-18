from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # prefix sums for rows
        row_sum = [[0]*(n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_sum[i][j+1] = row_sum[i][j] + grid[i][j]

        # prefix sums for columns
        col_sum = [[0]*(m+1) for _ in range(n)]
        for j in range(n):
            for i in range(m):
                col_sum[j][i+1] = col_sum[j][i] + grid[i][j]

        def is_magic(x, y, size):
            s = row_sum[x][y+size] - row_sum[x][y]
            # check rows
            for r in range(x, x+size):
                if row_sum[r][y+size] - row_sum[r][y] != s:
                    return False
            # check cols
            for c in range(y, y+size):
                if col_sum[c][x+size] - col_sum[c][x] != s:
                    return False
            # diagonal 1
            d1 = 0
            for i in range(size):
                d1 += grid[x+i][y+i]
            if d1 != s:
                return False
            # diagonal 2
            d2 = 0
            for i in range(size):
                d2 += grid[x+i][y+size-1-i]
            if d2 != s:
                return False
            return True

        # try sizes descending (largest first)
        for size in range(min(m, n), 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if is_magic(i, j, size):
                        return size
        return 1
