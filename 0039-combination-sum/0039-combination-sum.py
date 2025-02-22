from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # Store all valid combinations
        
        def backtrack(start, path, total):
            if total == target:  # If sum matches target, add to result
                res.append(path[:])
                return
            if total > target:  # If sum exceeds target, stop
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # Choose a number
                backtrack(i, path, total + candidates[i])  # Recur with same index
                path.pop()  # Undo choice (backtrack)
        
        backtrack(0, [], 0)  # Start recursion
        return res
