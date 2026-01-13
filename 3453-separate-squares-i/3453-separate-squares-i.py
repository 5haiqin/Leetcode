class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        half_area = sum(l * l for _, _, l in squares) / 2

        events = []
        for _, y, l in squares:
            events.append((y, True, l))       # start of vertical span
            events.append((y + l, False, l))  # end of vertical span

        events.sort(key=lambda e: e[0])

        area_below = 0
        width = 0
        prev_y = events[0][0]

        for y, is_start, l in events:
            dy = y - prev_y
            potential = area_below + width * dy

            if potential >= half_area:
                return prev_y + (half_area - area_below) / width

            area_below = potential
            width += l if is_start else -l
            prev_y = y

        return prev_y