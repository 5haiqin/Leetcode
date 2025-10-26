class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int, date.split('-'))
        leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
        days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days[:m-1]) + d
