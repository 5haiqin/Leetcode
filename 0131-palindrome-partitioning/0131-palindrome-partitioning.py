from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_pal(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int) -> None:
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if is_pal(part):
                    path.append(part)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
