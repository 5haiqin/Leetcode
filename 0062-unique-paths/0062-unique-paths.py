class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array filled with 1s
        dp = [[1] * n for _ in range(m)]
        
        # Loop through the grid starting from (1,1)
        for i in range(1, m):
            for j in range(1, n):
                # Current cell = sum of top and left cells
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the value at the bottom-right corner
        return dp[m-1][n-1]