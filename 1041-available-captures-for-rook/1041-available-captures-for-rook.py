class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ans = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i, j = r + dr, c + dc
            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 'p':
                    ans += 1
                    break
                if board[i][j] == 'B':
                    break
                i += dr
                j += dc
        return ans
