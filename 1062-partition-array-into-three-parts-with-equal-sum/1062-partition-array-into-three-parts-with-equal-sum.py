class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tot = sum(arr)
        if tot % 3 != 0:
            return False
        tgt = tot // 3
        c = 0
        s = 0
        for x in arr:
            s += x
            if s == tgt:
                c += 1
                s = 0
        return c >= 3
