class Solution:
    def daysBetweenDates(self, d1: str, d2: str) -> int:
        def leap(y: int) -> bool:
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

        def days_in_month(y: int, m: int) -> int:
            md = [31,28,31,30,31,30,31,31,30,31,30,31]
            if m == 2 and leap(y):
                return 29
            return md[m-1]

        def to_days(dt: str) -> int:
            y, m, d = map(int, dt.split('-'))
            total = 0
            for yy in range(1971, y):
                total += 365 + (1 if leap(yy) else 0)
            for mm in range(1, m):
                total += days_in_month(y, mm)
            total += d
            return total

        return abs(to_days(d1) - to_days(d2))
