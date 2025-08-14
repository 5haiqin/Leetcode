class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        peri = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: 
                    peri += 4
                    if i > 0 and grid[i-1][j] == 1:   
                        peri -= 2
                    if j > 0 and grid[i][j-1] == 1:  
                        peri -= 2
        return peri
