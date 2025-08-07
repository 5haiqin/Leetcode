from itertools import accumulate
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.pref = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right + 1] - self.pref[left]
