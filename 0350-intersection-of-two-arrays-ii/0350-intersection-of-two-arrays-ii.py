from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        res = []
        for x in nums2:
            if c1[x] > 0:
                res.append(x)
                c1[x] -= 1
        return res
