from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_dur = 0
        ans = ''
        prev = 0

        for i in range(len(releaseTimes)):
            d = releaseTimes[i] - prev
            if d > max_dur or (d == max_dur and keysPressed[i] > ans):
                max_dur = d
                ans = keysPressed[i]
            prev = releaseTimes[i]

        return ans
