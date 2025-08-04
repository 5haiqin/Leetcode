class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if i == start:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[start]}->{nums[i]}")
            i += 1
        return res
