class Solution:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split()
        month_str = " JanFebMarAprMayJunJulAugSepOctNovDec"
        mm = str(month_str.index(m) // 3 + 1).zfill(2)
        dd = d[:-2].zfill(2)
        return f"{y}-{mm}-{dd}"
