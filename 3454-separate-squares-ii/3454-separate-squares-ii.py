from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        active = []
        total_area = 0.0
        prev_y = events[0][0]

        def union_width(intervals):
            if not intervals:
                return 0
            intervals.sort()
            width = 0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    width += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            width += cur_r - cur_l
            return width

        strips = []

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                w = union_width(active)
                area = w * dy
                strips.append((prev_y, y, w, area))
                total_area += area
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y

        half = total_area / 2
        curr = 0.0

        for y1, y2, w, area in strips:
            if curr + area >= half:
                return y1 + (half - curr) / w
            curr += area

        return prev_y