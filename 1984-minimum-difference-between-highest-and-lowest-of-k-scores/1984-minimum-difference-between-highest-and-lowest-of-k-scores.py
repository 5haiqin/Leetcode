from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1 or n == 0:
            return 0

        nums.sort()
        ans = float('inf')

        for i in range(n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            ans = min(ans, diff)

        return ans
