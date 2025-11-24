from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["" for _ in range(3)] for _ in range(3)]
        
        for i, (r, c) in enumerate(moves):
            p = "A" if i % 2 == 0 else "B"
            board[r][c] = p
            
            if (board[r][0] == board[r][1] == board[r][2] == p or
                board[0][c] == board[1][c] == board[2][c] == p or
                board[0][0] == board[1][1] == board[2][2] == p or
                board[0][2] == board[1][1] == board[2][0] == p):
                return p
        
        if len(moves) == 9:
            return "Draw"
        return "Pending"