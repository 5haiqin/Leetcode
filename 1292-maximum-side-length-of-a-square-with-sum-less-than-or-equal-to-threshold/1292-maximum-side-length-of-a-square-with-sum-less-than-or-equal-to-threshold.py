from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )

        def can_fit(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        prefix[i][j]
                        - prefix[i - k][j]
                        - prefix[i][j - k]
                        + prefix[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False

        # Binary search on side length
        low, high = 0, min(m, n)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_fit(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans