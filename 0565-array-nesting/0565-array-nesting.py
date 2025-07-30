class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            count = 0
            while nums[i] != -1:
                temp = nums[i]
                nums[i] = -1
                i = temp
                count += 1
            max_len = max(max_len, count)
        return max_len
