from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  # Store unique combinations
        candidates.sort()  # Sort to handle duplicates easily
        
        def backtrack(start, path, target):
            if target == 0:  # If target is met, add to result
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # Stop if the number exceeds target
                
                path.append(candidates[i])  # Choose
                backtrack(i + 1, path, target - candidates[i])  # Recur
                path.pop()  # Undo choice
        
        backtrack(0, [], target)
        return result
