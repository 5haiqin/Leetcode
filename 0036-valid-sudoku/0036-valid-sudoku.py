from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # Row sets
        cols = [set() for _ in range(9)]  # Column sets
        boxes = [set() for _ in range(9)] # 3x3 box sets
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue  # Skip empty cells
                
                box_index = (r // 3) * 3 + (c // 3)  # Find box index
                
                # Check if num is already in row, column, or box
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False
                
                # Add num to respective sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True  # If no conflicts, it's valid
