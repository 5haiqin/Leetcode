from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            S = p + 1
            d = S & -S
            
            a = p - (d >> 1)
            ans.append(a)
        
        return ans
