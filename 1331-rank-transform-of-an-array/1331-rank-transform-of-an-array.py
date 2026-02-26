class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(set(arr))
        rank_map = {val: i + 1 for i, val in enumerate(unique_sorted)}
        return [rank_map[val] for val in arr]