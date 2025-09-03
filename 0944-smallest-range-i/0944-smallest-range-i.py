class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        d = mx - mn - 2*k
        return d if d > 0 else 0
