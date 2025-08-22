class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        m = 0.0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    a = x2 - x1
                    b = y2 - y1
                    c = x3 - x1
                    d = y3 - y1
                    area = abs(a * d - b * c) / 2
                    if area > m:
                        m = area
        return m
