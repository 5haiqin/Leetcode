from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]  # Create n x n matrix
        num, left, right, top, bottom = 1, 0, n - 1, 0, n - 1  # Initialize boundaries
        
        while num <= n * n:
            # Fill top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move top boundary down
            
            # Fill right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move right boundary left
            
            # Fill bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Move bottom boundary up
            
            # Fill left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Move left boundary right
            
        return matrix
