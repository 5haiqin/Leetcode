class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
        sa, sb = sum(a), sum(b)
        d = (sa - sb) // 2
        s = set(a)
        for x in b:
            if x + d in s:
                return [x + d, x]
