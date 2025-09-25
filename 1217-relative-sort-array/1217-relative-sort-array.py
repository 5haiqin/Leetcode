class Solution:
    def relativeSortArray(self, a: List[int], b: List[int]) -> List[int]:
        cnt = {}
        for x in a:
            cnt[x] = cnt.get(x, 0) + 1

        res = []
        for x in b:
            if x in cnt:
                res += [x] * cnt[x]
                del cnt[x]

        rem = sorted(cnt.items()) 
        for v, f in rem:
            res += [v] * f

        return res
