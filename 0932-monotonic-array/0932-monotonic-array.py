class Solution:
    def isMonotonic(self, a: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                dec = False
            if a[i] < a[i - 1]:
                inc = False
            if not inc and not dec:
                return False
        return True
