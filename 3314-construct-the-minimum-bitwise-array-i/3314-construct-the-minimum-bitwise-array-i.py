from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for a in nums:
            if a == 2:
                ans.append(-1)
                continue

            v = (a + 1) & -(a + 1)
            ans.append(a - (v >> 1))

        return ans
