from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        count = 0
        for word in words:
            is_consistent = True
            for ch in word:
                if ch not in allowed_set:
                    is_consistent = False
                    break
            if is_consistent:
                count += 1

        return count
