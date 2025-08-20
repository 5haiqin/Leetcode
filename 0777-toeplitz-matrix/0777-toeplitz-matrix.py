class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if m[i][j] != m[i-1][j-1]:
                    return False
        return True
