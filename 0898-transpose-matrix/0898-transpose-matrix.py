class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        return [[A[i][j] for i in range(m)] for j in range(n)]
